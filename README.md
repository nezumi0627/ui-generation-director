# UI Generation Director

A Codex skill for producing cleaner, higher-fidelity UI with a Magic Patterns / v0-style workflow plus Apple Human Interface Guidelines: real design-system context, component reuse, task-first UX decisions, visual inspection, focused polish passes, and interaction previews.

## What it adds

- Design-system and component-aware UI generation
- Screenshot / Figma / reference-driven recreation
- Incremental preview and polish loops
- Focused Inspiration / Polish / Debug modes
- Animated GIF previews for real UI interactions
- Guidance based on public Magic Patterns and v0 architecture research
- Apple HIG-based UX guidance for hierarchy, agency, feedback, touch targets, menus, typography, writing, motion, accessibility, and recovery

## Install

Clone the repository into your Codex skills directory:

```bash
git clone https://github.com/nezumi0627/ui-generation-director ~/.codex/skills/ui-generation-director
```

On Windows PowerShell:

```powershell
git clone https://github.com/nezumi0627/ui-generation-director "$HOME\.codex\skills\ui-generation-director"
```

The skill remains available for normal automatic skill selection.

## Interaction GIF previews

Capture the real implemented UI at a fixed viewport while performing the interaction, save frames with sortable names, then assemble them:

```bash
python scripts/make_interaction_gif.py frames --output interaction.gif
```

For deliberate timing:

```bash
python scripts/make_interaction_gif.py frames \
  --output interaction.gif \
  --durations 450,90,90,90,800
```

The helper supports PNG, JPEG, and WebP input frames, per-frame timing, first/last-frame holds, resizing, and looping. It requires Pillow:

```bash
python -m pip install -r requirements.txt
```

See [references/interaction-preview.md](references/interaction-preview.md) for the recommended capture flow and timing.

## Research basis

The skill reproduces publicly observable ideas around Magic Patterns and v0 rather than claiming access to private prompts. The supporting sources and architectural notes are in [references/research.md](references/research.md).

Apple UX guidance is based on current public Human Interface Guidelines and Apple design sessions. See [references/apple-hig-ux.md](references/apple-hig-ux.md).

## License

MIT
