# Interaction GIF previews

Use this workflow when the user needs to judge motion, menus, rewriting, drag/drop, hover/focus behavior, transitions, undo, or another interaction that a still image cannot explain well.

## Capture

Capture the actual rendered implementation at one fixed viewport. Store frames in a temporary folder with sortable names such as:

```text
frames/
  000-idle.png
  001-action.png
  002-motion.png
  003-motion.png
  004-result.png
```

For CSS transitions around 150-300 ms, a frame every 60-100 ms is usually enough. For slower 400-800 ms motion, 80-120 ms spacing is usually enough. Hold the initial state for roughly 300-500 ms and the final state for roughly 500-900 ms so the viewer can read what changed.

Prefer 5-20 meaningful frames over recording a long full-screen video. Keep the cursor out of the crop unless pointer location is necessary to understand the interaction.

When small text, thin borders, blur, or shadows need to stay crisp, capture above the final delivery resolution instead of recording directly at GIF size. A browser device scale factor around 2x-3x is often enough. Downsample once with a high-quality filter such as Lanczos after capture; avoid repeated resizing between stages.

If the flow has a reversible action, a useful sequence is:

```text
idle -> open -> choose/action -> result -> undo/close -> restored
```

## Assemble

From the skill directory:

```bash
python scripts/make_interaction_gif.py frames --output interaction.gif
```

Specify per-frame durations in milliseconds when the default timing is not enough:

```bash
python scripts/make_interaction_gif.py frames --output interaction.gif --durations 450,90,90,90,800
```

Use `--max-width 960` to reduce a large capture without changing aspect ratio.

## Quality check

Before sharing the GIF, verify that:

- The first frame makes the starting state obvious.
- The action and visual response are both visible.
- The viewport, crop, and scale stay stable.
- Text remains readable after GIF quantization.
- Fine borders, rounded corners, blur, and shadows do not break into noisy bands after downsampling or palette conversion.
- The loop does not create a confusing jump; use a longer final-frame hold when needed.
- The GIF demonstrates the shipped UI behavior rather than an invented preview-only effect.

If Pillow output shows obvious banding or unstable colors, prefer an ffmpeg palette pass when available: generate one palette from the full frame sequence, then encode with `paletteuse`. This is especially useful for dark UIs, subtle gradients, translucent panels, and soft shadows. Keep the Pillow helper as a portable fallback when ffmpeg is unavailable.
