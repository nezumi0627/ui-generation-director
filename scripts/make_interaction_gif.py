#!/usr/bin/env python3
"""Build a compact interaction GIF from a directory of captured UI frames."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError as exc:  # pragma: no cover - user-facing dependency failure
    raise SystemExit(
        "Pillow is required. Install it with: python -m pip install pillow"
    ) from exc


SUPPORTED = {".png", ".jpg", ".jpeg", ".webp"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Assemble captured UI frames into an animated GIF."
    )
    parser.add_argument("frames", type=Path, help="Directory containing image frames")
    parser.add_argument("--output", type=Path, default=Path("interaction.gif"))
    parser.add_argument(
        "--duration",
        type=int,
        default=100,
        help="Default duration per frame in milliseconds (default: 100)",
    )
    parser.add_argument(
        "--durations",
        help="Comma-separated per-frame durations in milliseconds",
    )
    parser.add_argument(
        "--hold-first",
        type=int,
        default=350,
        help="Minimum first-frame duration in milliseconds (default: 350)",
    )
    parser.add_argument(
        "--hold-last",
        type=int,
        default=650,
        help="Minimum final-frame duration in milliseconds (default: 650)",
    )
    parser.add_argument(
        "--max-width",
        type=int,
        default=1200,
        help="Downscale frames wider than this value; 0 disables resizing",
    )
    parser.add_argument("--loop", type=int, default=0, help="GIF loop count; 0 = forever")
    return parser.parse_args()


def frame_paths(directory: Path) -> list[Path]:
    if not directory.is_dir():
        raise SystemExit(f"Frame directory not found: {directory}")
    paths = sorted(
        path for path in directory.iterdir() if path.is_file() and path.suffix.lower() in SUPPORTED
    )
    if not paths:
        raise SystemExit(f"No PNG/JPEG/WebP frames found in: {directory}")
    return paths


def durations_for(count: int, args: argparse.Namespace) -> list[int]:
    if args.duration <= 0 or args.hold_first < 0 or args.hold_last < 0:
        raise SystemExit("Durations must be positive; hold values cannot be negative")

    if args.durations:
        try:
            values = [int(value.strip()) for value in args.durations.split(",")]
        except ValueError as exc:
            raise SystemExit("--durations must contain integers separated by commas") from exc
        if len(values) != count:
            raise SystemExit(
                f"--durations has {len(values)} values but {count} frames were found"
            )
        if any(value <= 0 for value in values):
            raise SystemExit("Every --durations value must be greater than zero")
    else:
        values = [args.duration] * count

    values[0] = max(values[0], args.hold_first)
    values[-1] = max(values[-1], args.hold_last)
    return values


def normalize_frame(image: Image.Image, size: tuple[int, int], max_width: int) -> Image.Image:
    image = image.convert("RGBA")
    if image.size != size:
        raise SystemExit(
            f"All frames must have the same size. Expected {size[0]}x{size[1]}, "
            f"got {image.width}x{image.height}."
        )

    if max_width > 0 and image.width > max_width:
        ratio = max_width / image.width
        image = image.resize(
            (max_width, max(1, round(image.height * ratio))), Image.Resampling.LANCZOS
        )
    return image


def main() -> int:
    args = parse_args()
    paths = frame_paths(args.frames)
    durations = durations_for(len(paths), args)

    with Image.open(paths[0]) as first_source:
        source_size = first_source.size

    frames: list[Image.Image] = []
    for path in paths:
        with Image.open(path) as source:
            frames.append(normalize_frame(source, source_size, args.max_width))

    output = args.output.expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)

    first, *rest = frames
    first.save(
        output,
        save_all=True,
        append_images=rest,
        duration=durations,
        loop=max(0, args.loop),
        disposal=2,
        optimize=True,
    )

    print(f"Created {output} from {len(frames)} frames")
    return 0


if __name__ == "__main__":
    sys.exit(main())
