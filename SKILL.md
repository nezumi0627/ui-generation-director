---
name: ui-generation-director
description: "Generate or refine high-fidelity, usable UI using a Magic Patterns/v0-style pipeline plus Apple Human Interface Guidelines: ground the model in real design rules, components, user goals, visual references, incremental preview feedback, interaction GIF previews, UX checks, and repair passes. Use for UI implementation, redesign, visual polish, interaction design, screenshot/Figma/site recreation, or design-system-aware frontend work where output quality matters."
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

## Design the task before the surface

Treat UX as part of generation, not a polish pass. Before deciding colors, materials, or component styling, identify the person's goal, the primary action, the minimum path to completion, and how the interface communicates state and recovery.

Use Apple's current design principles as a decision framework even when the product is not an Apple app:

- **Purpose:** make the person's main reason for being here obvious and spend detail on what matters most.
- **Agency:** keep consequential actions under the person's control; provide clear cancel, back, close, or undo paths when practical.
- **Flexibility:** account for different screen sizes, text sizes, input methods, abilities, and realistic usage contexts.
- **Simplicity:** remove UI that doesn't clarify content, choice, status, or the next action. Add context when its absence would make a simple-looking UI ambiguous.
- **Craft:** treat spacing, alignment, latency feedback, state transitions, copy, hit targets, and edge cases as product quality, not decoration.
- **Delight:** use personality and motion in service of the task rather than as constant spectacle.

For Apple-platform and Apple-inspired work, also preserve **hierarchy, harmony, and consistency**: content and the primary action should read first, geometry should feel related rather than arbitrary, and familiar platform behaviors should stay familiar.

Read [references/apple-hig-ux.md](references/apple-hig-ux.md) when designing an interaction, reviewing usability, choosing motion/feedback, or making an Apple-inspired surface. Apply platform-specific numeric guidance only when the target platform or input method makes it relevant.

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

When elevation is part of the design, judge it in the composed screen rather than on an isolated component. Broad shadows from nearby surfaces can stack into a dark band, especially when a popover sits directly above a card, composer, or toolbar. Prefer a small set of elevation tokens, tighter near-contact shadows plus a softer low-alpha falloff, and surface/border contrast to do part of the separation work. Rebalance dark-mode shadows independently instead of carrying light-mode opacity and blur over unchanged. If a popover has a pointer or tail, keep its fill and border visually continuous with the panel.

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
- Elevation that still reads cleanly where surfaces overlap; shadows should not merge into black bands, halos, or muddy seams in light or dark mode.
- Realistic content density instead of empty demo cards or decorative filler.
- Responsive behavior at the requested breakpoints.
- Hover, focus, loading, empty, success, warning, error, disabled, and destructive states where relevant.
- Keyboard/focus/contrast basics and reduced-motion behavior.
- The primary task is obvious without reading every label, and controls sit near the content or state they affect.
- Every meaningful action gives immediate, proportional feedback; waiting, success, failure, and blocked states never feel like a dead tap.
- Reversible actions have a practical recovery path, and destructive or difficult-to-recover actions are clearly distinguished before commitment.
- Touch targets are comfortable for the target device; on iOS/iPadOS, aim for at least 44×44 pt for ordinary interactive controls.
- Custom controls visibly respond to press/selection and use familiar interaction behavior unless a custom behavior has a clear benefit.
- Menus keep frequent or important actions easy to scan, group related commands, and avoid unnecessary length.
- Interface copy is direct, consistent, and describes what an action will do; multi-step flows use stable terminology.
- Typography remains legible and the hierarchy survives larger text sizes instead of depending on one fixed layout.
- Motion explains state, continuity, or feedback. Decorative motion is restrained, and reduced-motion mode removes unnecessary translation, scale, depth, and blur animation.

Avoid common model-generated UI tells unless the reference explicitly calls for them: gratuitous gradients, glow everywhere, excessive glass, nested card grids, oversized hero copy inside tools, arbitrary rounded rectangles, inconsistent icon families, and random spacing values.

## Focused modes

Use these behaviors when the request calls for them:

- **Inspiration:** create a few meaningfully different visual directions, then pick or combine one before implementation.
- **Polish:** preserve structure and behavior; improve spacing, alignment, hierarchy, typography, color balance, and component consistency from the rendered result.
- **Debug:** reproduce the failure, inspect runtime/build/browser evidence, fix the root cause, then re-render.
- **Reference recreation:** extract the reference's design grammar first, then implement it with the project's real components and tokens.

Read [references/research.md](references/research.md) when explaining the architecture, calibrating this workflow against Magic Patterns/v0, or deciding which pipeline stage would improve output quality. Read [references/apple-hig-ux.md](references/apple-hig-ux.md) for the Apple UX evidence and practical interaction rules.
