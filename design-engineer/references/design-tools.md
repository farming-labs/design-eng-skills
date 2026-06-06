# Design Engineer Tools

Use this reference when selecting tools, inspiration sources, design-to-code workflows, asset sources, or design-system infrastructure for a design-engineering task.

## Live Directory

- `https://designtools.fyi/`: compare design tools by role, facet, tag, source of truth, price, and size.
- Start with the Design Engineer archetype when the job is bridging design and production code.
- Use facets to narrow intent: Contributing Code, UI Craft, Design Systems, Prototyping, UI Generation, Design for AI, UX Design, Design Exploration.
- Re-check live pages before recommending a paid tool, because pricing, features, and AI limits change quickly.

## Selection Principles

- Source of truth matters: prefer production code when the task must ship, Figma when collaboration/design review is the main workflow, and generated code only when the result will be inspected and refactored.
- Code quality beats screenshot similarity. Favor tools that preserve semantic HTML, component boundaries, tokens, accessibility, and idiomatic React/Tailwind.
- Design-system fit beats novelty. Choose tools that can read existing components, tokens, styles, or repo context.
- Local/private constraints matter. For sensitive apps, prefer local-first or repo-local tools over cloud-only upload flows.
- Treat generated UI as a draft unless the tool writes directly into the codebase with a reviewable diff.
- Pick one tool for the job stage. Avoid stacking multiple AI builders unless each one owns a clear step.

## Practical Tool Map

### Codebase Agents And IDEs

Use when the product already lives in code and the design pass should become a real diff.

- Codex: repo-aware implementation, review, verification, and multi-file design-engineering passes.
- Claude Code, Cursor, GitHub Copilot, Gemini, Antigravity: code agents and AI IDEs for implementation, refactors, browser feedback loops, and code review.
- Blueberry-style workspaces: useful when browser preview, terminal, editor, and design context need to live in one surface.

### Visual Design To Code

Use when a team needs a visual surface but still cares about production-ready code.

- Figma: collaboration, variables, Dev Mode, Code Connect, design review, and design-system source material.
- Subframe, Paper, Pencil, Dessn, Noon, Onlook, CSS Studio, Builder.io, Anima, Kombai: code-aware visual editors or design-to-code tools.
- Magic Patterns, Lunagraph, Wonder, Google Stitch, Claude Design, Moonchild, Flowstep: prompt/canvas tools for generating UI directions or flows that still need code review.
- Bolt.new, Lovable, Create/Anything, FlutterFlow, Framer: useful for prototypes or specific platform/site-builder workflows; inspect exported code before treating it as production.

### Components, Blocks, And Design Systems

Use when building a reusable primitive set, registry, product sections, or component library.

- `https://www.components.build`: baseline component architecture and API standard.
- shadcn/ui, Radix UI, CVA, Tailwind, `cn(...)`: default React primitive stack when already present.
- FarmUI, Efferd, 21st, React Bits: component and block inspiration; adapt tokens and accessibility to the current repo.
- Storybook, Ladle, Histoire: component documentation, states, and visual review.
- Tokens Studio, Style Dictionary, Figma Variables: token authoring and token-to-code workflows.

### Inspiration And Product Pattern Research

Use before inventing layouts from memory.

- Mobbin, Nicelydone: real app screens, flows, and SaaS pattern references.
- 21st, React Bits, Efferd, FarmUI: component-level and section-level references.
- Vercel, E2B, Hex, Better Auth, Basement Studio: product, developer-platform, analytics, auth, and immersive storytelling references.
- `designtools.fyi`: use for discovering the current tool landscape and comparing by archetype/facet.

### Motion, 3D, And Visual Systems

Use when the product benefits from movement, demos, or immersive craft.

- animations.dev vocabulary: name motion decisions precisely.
- React Bits: animated components, shader-like surfaces, text effects, and backgrounds.
- LottieFiles, Jitter, Cavalry, Rive: motion assets, animation editing, and export pipelines.
- Shaders, Three.js, React Three Fiber, drei: WebGL and 3D scenes when the visual is part of the product value.
- Basement Studio: reference for high-impact 3D/product storytelling, not a reason to add spectacle by default.

### Icons, Loaders, Type, And Assets

Use when choosing visual assets that must stay consistent with the product system.

- `lucide-react`: default app and docs action icons when installed.
- Iconify: browse many icon families, variants, grids, palettes, and licenses when lucide is not enough.
- Pixel Icon Library: consistent pixel icons when the product uses a deliberate pixel/block language.
- `icons.icantcode.fyi`: quiet dot/matrix loading and status indicators.
- `simple-icons`: brand marks when installed and appropriate.
- Locale, FontBase, Google Fonts, variable-font specimen tools: type exploration and font selection.
- Inkscape, Affinity, GIMP, Midjourney, Flora, Quiver AI: asset creation/editing when the product needs illustrations, SVGs, images, or creative exploration.

## Recommendation Format

When recommending tools, give a short, decision-ready answer:

- Stage: discovery, prototype, production implementation, component system, visual assets, or verification.
- Tool choice: primary tool plus one fallback.
- Why: how it fits source of truth, code quality, collaboration, and constraints.
- Risk: generated-code cleanup, cost, privacy, export quality, lock-in, or accessibility gaps.
- Next action: inspect current repo, create a small spike, import/export one component, or verify a single flow before committing.
