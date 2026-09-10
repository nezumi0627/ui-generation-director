# Research basis: Magic Patterns and v0

Updated: 2026-09-11

This reference captures public, official evidence for the workflow in `ui-generation-director`. It is architectural guidance, not a reconstruction of private prompts.

## Magic Patterns

### Design system as persistent generation context

Magic Patterns describes its Design System as a single source of truth containing components, typography/icons, colors, rules, skills, and access/settings. Rules cover defaults such as spacing, visual style, and brand voice; the AI automatically applies rules, tokens, typography/icons, and appropriate components to new designs.

Official sources:

- https://www.magicpatterns.com/docs/documentation/design-systems/overview
- https://www.magicpatterns.com/blog/introducing-design-systems
- https://www.magicpatterns.com/blog/introducing-design-system-agent

This reduces the model's design search space. Instead of inventing colors, spacing, component anatomy, and brand tone on every generation, it receives a bounded vocabulary and reusable building blocks.

### Visual context is first-class

Magic Patterns recommends attaching screenshots. Its docs say screenshots, Markdown specs, and notes are read as first-class prompt context. Figma imports extract colors, typography, spacing, and component structure. Agent Mode can also browse a referenced website and capture its design as context.

Official sources:

- https://www.magicpatterns.com/docs/documentation/editor/how-to-prompt
- https://www.magicpatterns.com/blog/introducing-design-systems
- https://www.magicpatterns.com/blog/agent-mode

The implication is that visual fidelity comes partly from giving the model direct evidence instead of asking it to infer a visual style from a short adjective such as "modern".

### Agent loop instead of single-pass generation

Magic Patterns says Agent Mode builds context as it works, studies the existing design, asks relevant questions, and writes changes incrementally. It also searches and selects custom components. Magic Patterns reports a 40% decrease in errors versus its Legacy mode and a 35% improvement at fixing bugs in its internal benchmarks.

Official source:

- https://www.magicpatterns.com/blog/agent-mode

Treat those percentages as vendor-reported internal benchmark results, not independent measurements.

### Specialized UI skills and editing modes

Magic Patterns exposes reusable prompt behaviors: `/Debug`, `/Inspiration`, and `/Polish`, plus `/Plan` as a chat mode. `/Polish` specifically targets spacing, alignment, and visual hierarchy. Select Mode adds the selected element's context to the chat, narrowing the edit target.

Official source:

- https://www.magicpatterns.com/docs/documentation/editor/how-to-prompt

This is a useful pattern for Codex: make visual cleanup and debugging explicit passes instead of hoping a general generation prompt performs every role equally well.

### Model routing

Magic Patterns' Agent Mode announcement says automatic model routing is enabled by default and describes a multi-model architecture that matches tasks to models. Its V2 API exposes `modelSelector=auto` plus explicit model choices, alongside `designSystemId` and image inputs.

Official sources:

- https://www.magicpatterns.com/blog/agent-mode
- https://www.magicpatterns.com/docs/patterns/v2-create-a-new-design

In July 2026 Magic Patterns announced GPT-5.6 support and said it produced stronger first drafts, followed detailed visual direction with fewer revisions, and used 2.5x fewer credits than Fable 5 on comparable internal tests while still producing polished interactive designs.

Official source:

- https://www.magicpatterns.com/blog/introducing-gpt-5-6

Again, the credit and quality comparison is Magic Patterns' own testing.

## v0 / Vercel

### AI-native design system and component registry

v0 uses `shadcn/ui` as its default component system. Vercel describes the shadcn registry as a structured way to pass components, blocks, tokens, metadata, file content, and styles to AI models. Custom Tailwind config and `globals.css` can provide project-specific tokens and utilities.

Official sources:

- https://v0.dev/docs/design-systems
- https://vercel.com/blog/ai-powered-prototyping-with-design-systems

Vercel's rationale is that open components, composable and consistent APIs, and simple token-based styling are easier for models to predict than opaque or heavily wrapped component libraries.

### Figma and image context

Vercel says v0's Figma integration extracts context from Figma files and supplementary visuals and passes it into the generation process. It recommends componentizing large designs and iterating on smaller pieces rather than trying to generate a whole complex product in one pass.

Official source:

- https://vercel.com/blog/working-with-figma-and-custom-design-systems-in-v0

### Composite model pipeline

Vercel publicly describes v0 as a composite model architecture rather than a raw frontier-model call. Its pipeline includes:

- A system prompt and conversation context.
- Retrieval of relevant documentation, UI examples, uploaded project sources, and Vercel knowledge.
- A high-capability base model for new or large changes.
- A Quick Edit model for narrow edits.
- A custom AutoFix model and deterministic corrections during generation.
- A final repair pass and linter.

Official source:

- https://vercel.com/blog/v0-composite-model-family

The 2025 post reported substantially higher error-free generation rates for its then-current v0 composite models than the listed standalone base models. Treat those numbers as a historical vendor benchmark, useful for architecture evidence rather than a current model leaderboard.

### Dynamic system prompts, streaming transforms, and autofixers

In January 2026 Vercel described three especially impactful reliability layers in the v0 agent:

- Dynamic system-prompt injection for current framework/integration knowledge.
- Curated read-only examples searchable by the agent.
- "LLM Suspense", a streaming manipulation layer that can deterministically rewrite known-bad output such as invalid imports.
- Deterministic and model-driven autofixers for cross-file, AST, dependency, JSX, and TypeScript issues.

Official source:

- https://vercel.com/blog/how-we-made-v0-an-effective-coding-agent

This is strong evidence that v0's quality comes from orchestration around the base LLM, not merely from model identity.

### Project instructions

The v0 project API supports persistent project `instructions`, providing goals or guidance as model context across work in that project.

Official source:

- https://v0.dev/docs/v0-platform-api/projects/projects.create

## Synthesis: why the same GPT can look much better in these products

The public evidence supports seven mechanisms:

1. **Constrained design search space.** Tokens, rules, typography, and component registries replace arbitrary visual invention with a coherent grammar.
2. **Direct visual evidence.** Screenshots, Figma, existing websites, and source code give the model geometry and style information it cannot recover from a vague text prompt.
3. **Reusable components and blocks.** High-quality primitives move difficult details such as accessibility, proportions, and states out of each fresh generation.
4. **Task-specific prompting and retrieval.** Dynamic instructions, skills, docs, code examples, and project context steer the same base model toward the desired stack and visual language.
5. **Incremental agent behavior.** Inspecting, editing, previewing, and refining smaller surfaces reduces compounding errors compared with one-shot page generation.
6. **Post-processing and verification.** Linters, deterministic rewrites, AutoFix models, browser evidence, and visual polish passes correct predictable failures after or during generation.
7. **Model routing.** Products can use a stronger visual model for first drafts and cheaper/faster models or deterministic tools for narrow edits and repair.

The practical conclusion for Codex is to reproduce this surrounding pipeline. A different model can improve first-pass taste, but design-system context, visual grounding, preview feedback, and repair stages are the durable quality multiplier.
