---
name: ui-generation-director
description: "Generate or refine high-fidelity UI using a Magic Patterns/v0-style pipeline: ground the model in real design rules, components, visual references, incremental preview feedback, interaction GIF previews, and repair passes. Use for UI implementation, redesign, visual polish, screenshot/Figma/site recreation, or design-system-aware frontend work where output quality matters."
---

# UI Generation Director

Treat the base model as one part of the UI system. High-quality output comes from constraining the search space with real design context, working in small visual iterations, and repairing the rendered result.

Do not claim to know private system prompts from Magic Patterns or v0. Reproduce the observable architecture and workflow instead.

## Build the context pack first

Before substantial UI edits, collect the smallest useful context:

- Existing product UI, layout, tokens, CSS variables, typography, icons, and reusable components.
- User-provided screenshots, Figma exports, reference sites, or mockups. Extract hierarchy, geometry, spacing rhythm, type scale, color roles, component anatomy, density, and motion cues.
- Product intent: primary user task, platform, content density, responsive targets, and accessibility constraints.
- Existing component registry. Reuse real components before inventing substitutes.

Represent the result as a compact working brief rather than a long design essay. Prefer semantic tokens such as `surface`, `text-muted`, `accent`, `danger`, spacing steps, radius levels, and typography roles over one-off values.

When available, use `ui-skills-root` to load the smallest relevant UI skill set. `ui-studio-design` is a useful companion for visual craft rules; Apple-targeted work should use `apple-hig` as the platform reference.

## Use an agentic UI loop

For a new screen or meaningful redesign:

1. Inspect the current implementation and rendered UI when possible.
2. Decide the information hierarchy and component composition before decoration.
3. Implement one coherent screen, section, or interaction using the existing design system.
4. Render or preview the result and inspect the actual pixels, not just the source.
5. Run a focused polish pass for spacing, alignment, typography, visual hierarchy, density, and consistency.
6. Run build/type/lint/browser checks appropriate to the change and repair concrete failures.
7. Repeat only for remaining visible or functional defects.

Prefer incremental edits over regenerating an entire surface after every prompt. Preserve working structure while changing the smallest layer that explains the visual problem.

## Show interaction, not only static pixels

When an interaction is part of what the user is evaluating, prefer a short animated GIF preview in addition to a still screenshot when the environment can capture rendered frames.

- Capture the real implemented UI while performing the interaction. Do not mock a separate animation just for the preview.
- Keep one stable viewport and crop across all frames so the GIF does not jump.
- Include a brief idle state, the action itself, and the settled result. For reversible interactions, show the undo/close path when useful.
- Capture enough frames around motion to make easing and state changes readable, then hold the final state briefly.
- Keep the preview short and focused; one GIF should demonstrate one interaction or one tightly related flow.
- Respect reduced-motion behavior in the product. The preview may use the normal-motion mode only when it represents the product's actual default behavior.

Use `scripts/make_interaction_gif.py` to assemble captured PNG/JPEG/WebP frames into a GIF. Read [references/interaction-preview.md](references/interaction-preview.md) when recording an interaction preview or choosing frame timing.

## Route work by task shape

If the environment supports multiple models or specialized agents, route by task rather than brand loyalty:

- Visual first draft or screenshot interpretation: prefer the model strongest at multimodal/UI composition.
- Small copy, spacing, ordering, or syntax edits: prefer a fast edit path.
- Cross-file bugs or ambiguous layout failures: prefer the strongest reasoning/debug path.
- Final repair: deterministic transforms, formatter/linter/type checks, and small fix models are often cheaper and more reliable than regenerating the page.

Do not block the task when model routing is unavailable. The context and iteration pipeline matters more than a specific provider.

## Default quality gate

Before calling a UI complete, check the rendered result for:

- One obvious visual hierarchy: primary action, primary content, supporting content.
- Consistent alignment and spacing rhythm; repeated values should come from tokens.
- Deliberate typography with a small role-based scale and sensible line lengths.
- Components that share geometry, states, radius, border/elevation, and icon treatment.
- Realistic content density instead of empty demo cards or decorative filler.
- Responsive behavior at the requested breakpoints.
- Hover, focus, loading, empty, success, warning, error, disabled, and destructive states where relevant.
- Keyboard/focus/contrast basics and reduced-motion behavior.

Avoid common model-generated UI tells unless the reference explicitly calls for them: gratuitous gradients, glow everywhere, excessive glass, nested card grids, oversized hero copy inside tools, arbitrary rounded rectangles, inconsistent icon families, and random spacing values.

## Focused modes

Use these behaviors when the request calls for them:

- **Inspiration:** create a few meaningfully different visual directions, then pick or combine one before implementation.
- **Polish:** preserve structure and behavior; improve spacing, alignment, hierarchy, typography, color balance, and component consistency from the rendered result.
- **Debug:** reproduce the failure, inspect runtime/build/browser evidence, fix the root cause, then re-render.
- **Reference recreation:** extract the reference's design grammar first, then implement it with the project's real components and tokens.

Read [references/research.md](references/research.md) when explaining the architecture, calibrating this workflow against Magic Patterns/v0, or deciding which pipeline stage would improve output quality.
