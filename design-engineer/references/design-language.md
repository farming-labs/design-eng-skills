# Technical Product Design Language

Load this reference when the task is a curated technical docs site, OSS/product website, component library, dashboard, studio app, or design-engineering polish pass.

This reference is intentionally portable. It does not depend on private local paths. When the user provides inspiration repos, screenshots, URLs, or local files, inspect those sources directly and translate their patterns into the current project.

## Design Language Brief

The target design language is technical, product-forward, and component-system aware:

- Structure first: borders, rails, grids, gutters, separators, dotted underlines, and inset markers create the layout logic.
- Primitives first: build from reusable buttons, inputs, cards, dialogs, command palettes, copy controls, tables, tabs, and status components instead of one-off page markup.
- Dense but calm: dashboards and docs should be compact, scannable, and useful immediately without feeling crowded.
- Mono as utility: use mono for commands, routes, IDs, status, chips, shortcuts, tabs, timestamps, and technical labels.
- Proof over decoration: show install commands, terminal output, code snippets, diagrams, data, charts, previews, or real workflow states.
- Motion with purpose: hover/press/focus feedback, command/search transitions, copy confirmation, loading status, and restrained background motion.
- High contrast, restrained accents: use black/white or near-neutral foundations, then introduce accent color sparingly for state, focus, or brand.
- Agent/developer ready: include copyable commands, searchable docs, clear empty/error/loading states, and tool-friendly content structure.

## Craft Posture

Good design-engineering is trained through inspection and repetition. Before a serious polish pass, study the best nearby references, name what makes them work, then translate only the useful mechanics into the current product.

- Small details compound: press states, focus states, hover gates, copy confirmation, transform origin, empty states, disabled states, tooltip timing, loading labels, and reduced-motion behavior all add up.
- Beauty is product leverage only when the workflow also gets clearer, faster, or easier to trust.
- Defaults matter: buttons, toasts, dialogs, tables, charts, code blocks, and docs cards should look good before the user customizes anything.
- Review polish in motion, not only in screenshots. Slow down transitions, resize the viewport, try keyboard flows, and check touch behavior when the UI depends on gestures.
- When an interaction is repeated all day, make it immediate. When it is rare and explanatory, motion can carry more personality.

## Public Inspiration Sites

Use these as live design references when network access is available. Inspect them for component behavior, composition, copy rhythm, primitive styling, and motion language. Do not clone them blindly; translate the patterns into the current repo's stack and tokens.

- `https://www.components.build`: open standard for modern, composable, accessible UI components; use as the default engineering standard for reusable component APIs and design-system guidelines.
- `https://designtools.fyi/`: tool directory for comparing design-engineering tools by role, facet, tag, source of truth, price, and size.
- `https://vercel.com`: developer-platform product reference for crisp typography, technical storytelling, docs/product hierarchy, dashboard polish, deployment/status affordances, and restrained visual systems.
- `https://e2b.dev`: AI agent cloud reference for infrastructure/product storytelling, agent runtime concepts, sandbox/developer workflows, and technical diagrams.
- `https://hex.tech`: AI analytics platform reference for data-heavy product UI, collaborative analytics workflows, charts, notebooks, dashboards, and team-oriented product storytelling.
- `https://basement.studio`: digital studio reference for immersive product storytelling, bold art direction, 3D/interactive scenes, motion-rich transitions, and high-impact brand systems that still perform.
- `https://docs.farming-labs.dev`: AI-native docs surface with install commands, agent prompts, framework tabs, themes, code/copy affordances, Ask AI, MCP, llms.txt, search, and agent-readiness ideas.
- `https://farming-labs.dev`: compact Farming Labs brand/origin surface for the broader `@farming-labs/*` ecosystem.
- `https://orm.farming-labs.dev`: technical OSS docs/product site for unified schema, typed runtime, and generator-first ORM tooling.
- `https://farmui.farming-labs.dev`: FarmUI component reference for styled and animated shadcn-based primitives.
- `https://efferd.com`: Efferd section/block library reference for clean, ready-to-use shadcn blocks, responsive section composition, and fast product-page assembly.
- `https://21st.dev`: community React component reference for exploring, copying, and remixing high-quality UI components from designers and developers.
- `https://react-bits.dev`: React Bits reference for animated UI components, interactive backgrounds, shader-like effects, text animations, and reusable React component ideas.
- `https://pixeliconlibrary.com`: open-source pixelated icon library reference for 24px-grid pixel icons when a product needs a deliberate retro/block icon style.
- `https://icon-sets.iconify.design/`: Iconify icon-set catalog for browsing many open-source icon families, variants, grid sizes, palettes, and licenses.
- `https://better-auth.studio`: studio/admin product surface for users, sessions, organizations, events, database, and operational workflows.
- `https://better-auth.farmui.com`: user-provided Better Auth + FarmUI inspiration target; inspect when reachable for auth/product UI composition, component styling, and FarmUI-aligned interaction patterns.
- `https://better-auth.com`: polished auth framework website/docs reference for refined dark UI, docs hierarchy, and technical product storytelling.

If the user also provides local paths to repos behind these websites, inspect those repos for implementation details. Useful places to look are `components/ui/*`, `app/page.tsx`, `app/globals.css`, `app/global.css`, `docs.config.*`, `components/*command*`, `components/*copy*`, `components/*code*`, `components/*theme*`, `components/*layout*`, dashboard widgets, and shared primitive files. Treat local paths as optional source material, not public package requirements.

## Component Engineering Standard

Use `https://www.components.build` as the baseline standard when creating or refactoring reusable UI primitives, component libraries, registries, or design-system components.

Apply it this way:

- Composition: prefer small cooperating parts over one large prop-heavy component. Use Root, Item, Trigger, Content, Header, Body, Footer, Title, and Description naming where it fits.
- Accessibility: start with semantic HTML, provide keyboard access, visible focus indicators, accessible names, ARIA only when semantic HTML is insufficient, and live regions for dynamic feedback.
- Design tokens: route repeated visual decisions through semantic tokens for color, spacing, radius, typography, border, shadow, and motion.
- State: support controlled and uncontrolled patterns for flexible primitives when the component is intended for reuse.
- Styling: use `cn(...)`, `clsx`, `tailwind-merge`, and CVA-style variants when the repo uses Tailwind/shadcn patterns. Order classes as base, variants, conditional state, then user `className`.
- Types: wrap a single native element per primitive when possible, extend native `React.ComponentProps<...>`, export prop types, and keep consumer override paths open.
- Polymorphism/asChild: use `asChild` or polymorphic rendering only when consumers genuinely need to change the underlying element without losing behavior.
- Data attributes: expose stable `data-*` hooks for state styling such as `data-state`, `data-disabled`, `data-active`, `data-selected`, or `data-orientation`.
- Documentation: document variants, sizes, states, anatomy, examples, and accessibility expectations for shared primitives.
- Publishing: if the output is a component package or registry, keep exports, types, examples, docs, and install paths predictable.

This standard should govern how primitives are built; the visual style below governs how they should feel.

## Component Source Pattern Brief

When implementation source is available from a repo, website source, component registry, screenshot, or user-provided path, use it as source material for component behavior and styling. The recurring patterns to preserve are:

- Shadcn/Radix primitive base: buttons, cards, dialogs, sheets, popovers, commands, tabs, forms, select, checkbox, radio, slider, table, chart, skeleton, toast, and tooltip are built as small forwardRef components with native props, CVA variants, `cn(...)`, and optional `asChild`.
- Button system: use `variant` and `size` APIs, preserve width while loading, support icon buttons, prefer lucide icons, expose focus-visible states, and use tight heights for dense app UIs.
- Card anatomy: export `Card`, `CardHeader`, `CardTitle`, `CardDescription`, `CardContent`, and `CardFooter`; use cards for widgets/repeated items and add rails/corner ticks/grid texture when the visual language needs more structure.
- Command/search: use `cmdk` for command palettes; include search icon, grouped results, separators, empty state, keyboard flow, route/action metadata, and disabled/plugin states.
- Copy controls: use `navigator.clipboard`, lucide `Copy`/`Check`/`Clipboard` icons, copied feedback for roughly 2 seconds, and package-manager menus for install commands.
- Docs primitives: feature cards combine lucide foreground/background icons, mono labels, compact chips, 1px rails, corner ticks, and subtle texture; code/terminal blocks need header, copy, language/title, and overflow safety.
- FarmUI sections: hero and feature sections commonly combine command modules, CTA buttons, GitHub links, preview surfaces, gradients/grid/ripple backgrounds, and section wrappers. Keep these effects restrained and responsive.
- Studio widgets: dense cards carry metric title, value, timeframe, filter, chart/table/list body, loading/error/empty fallback, and customization/drop-target states.
- Icon language: lucide is the default for normal UI actions; Iconify is the fallback catalog for alternate families and variants; custom pixel/block SVGs are reserved for a deliberate pixel/studio style; dot/matrix SVGs are for loaders/status.
- Motion: common sources are Tailwind animation, Framer Motion, keyframes, and hover/transition utilities. Add reduced-motion handling when introducing new motion.

Apply these patterns as guidance, but always adapt them to the target project's current tokens, framework version, accessibility model, and component ownership.

## Inspirational Component Libraries

Use component/block libraries as pattern references for structure and primitive behavior, not as a reason to ignore the target repo's design system.

- components.build (`https://www.components.build`): inspect for component architecture standards, not surface styling; use it to shape APIs, composition, accessibility, state, styling, types, docs, and publishing.
- FarmUI (`https://farmui.farming-labs.dev`): inspect for styled and animated shadcn-style primitives, button treatments, interactive controls, and UI-level motion.
- Efferd (`https://efferd.com`): inspect for section-level blocks such as heroes, feature sections, pricing/comparison sections, testimonials, FAQ, CTA bands, auth forms, dashboards, and product-page composition.
- 21st (`https://21st.dev`): inspect for community-made React components, interaction ideas, component-level polish, and remixable patterns that can be adapted into the target repo's primitives.
- React Bits (`https://react-bits.dev`): inspect for animated backgrounds, shader-style surfaces, cursor/interaction effects, text effects, loaders, and general React UI components.
- shadcn/ui-compatible libraries: translate block structure into the current repo's tokens, radius, borders, type rhythm, icon policy, and accessibility behavior.

When using a block as inspiration:

- keep the section's intent but rewrite copy and content for the product
- adapt spacing, border language, radius, color, and typography to the current design system
- compose from existing primitives first
- include responsive behavior for mobile/tablet/desktop
- preserve accessible labels, semantic landmarks, focus states, and keyboard flows
- avoid adding decorative sections that do not advance the user's product workflow
- use animated backgrounds or shader-like effects only when they support the product story; keep them behind content, responsive, nonblocking, and reduced-motion aware

## Product Archetypes

Use these archetypes to choose the right visual and interaction posture:

- AI-native docs site: strong product signal, searchable docs, command/search patterns, install commands, code/copy affordances, changelog links, agent-facing artifacts such as llms.txt or MCP when relevant.
- Technical OSS docs: dense but readable navigation, framework tabs, CLI showcase, examples near the top, crisp callouts, support matrix or integration cards, code blocks with useful headers and copy controls.
- Graph/data product site: constrained hero, grid/rail structure, retrieval/data model proof, install module, technical chips, subdued animated background, clear citations or data-flow explanation.
- Developer platform: framework/runtime proof, deploy/status flows, dashboard clarity, docs-to-product navigation, changelog/release affordances, and confident system typography.
- AI infrastructure product: agent/runtime concepts, sandbox or execution diagrams, developer workflow proof, security/trust sections, and crisp technical CTAs.
- Analytics platform: notebook/dashboard composition, chart/tooltips, data lineage, collaboration states, filter/date controls, and team workflow narratives.
- Immersive studio/product site: bold art direction, 3D/canvas scenes, interactive scroll, rich transitions, expressive type, and tactile product moments. Use this only when the product benefits from spectacle and performance can be verified.
- Studio/dashboard app: operational shell, side navigation, command palette, status/watch indicators, widgets, tables, charts, filters, copyable IDs, date controls, tight feedback loops.
- Curated product website: first-viewport product identity, real demo or terminal/script proof, restrained 3D/canvas only when it explains the product, crisp mono navigation, visible path into docs or app.

## House Style

The shared visual language is precise, technical, and product-forward:

- Hard structure: 1px borders, vertical rails, gutters, separators, dashed/dotted details, inset lines, visible grid logic.
- Square geometry: zero or tiny radius for technical surfaces; use larger radius only when the existing system requires it.
- Contrast: black/white or near-black/near-white foundations with muted grays and very restrained accents.
- Typography: Geist Sans and Geist Mono are common. Mono is used for labels, nav, commands, status, chips, IDs, timestamps, and technical affordances.
- Microcopy: short, concrete, and product-specific. Avoid generic "seamless/powerful" filler.
- Texture: pixel textures, repeated-line patterns, subtle noise, grid overlays, or SVG/canvas effects can work when they reinforce the product.
- Density: docs and dashboards should feel useful immediately. Keep first screens rich but readable.
- Actions: copy commands, install snippets, "open docs", search, command palette, changelog links, and GitHub links should be visible where useful.

## Docs And OSS Website Recipes

For docs/product websites:

- Make the product name or literal offer obvious in the first viewport.
- Include a real install command, code snippet, feature proof, search/docs entry, or framework tabs early.
- Use full-width bands and structured sections, not floating marketing cards.
- Prefer tight mono labels above sections and concise explanatory copy below.
- Let the next section peek into the first viewport on landing pages.
- Use feature cards only when each card says something concrete: API, CLI, search, MCP, analytics, schema, integrations, adapters, plugins, or deployment.
- Keep docs affordances practical: sidebar states, page actions, copy buttons, callouts, code block headers, search, llms.txt/MCP/API links when relevant.

Useful local patterns to inspect when they exist in the target repo:

- `components/ui/pixel-card.tsx`
- `components/ui/feature-grid-card.tsx`
- `components/ui/copy-command.tsx`
- `components/ui/code-block.tsx`
- `components/docs-command-search.tsx`
- `components/ui/framework-tabs.tsx`
- `app/global.css` or `app/globals.css`

## Studio And Dashboard Recipes

For dense product apps:

- Build an operational shell first: sidebar, top status, search/command palette, route active states, profile/theme controls, and real content panels.
- Use compact widgets with clear metrics, legends, filters, and timestamps.
- Make tables scannable: stable columns, copyable IDs, status badges, empty/error/loading rows, pagination, search/filter controls.
- Use command palette and keyboard shortcuts for repeated actions.
- Prefer charts that can be read at a glance; use tooltips, muted gridlines, and restrained fills.
- Keep modal/drawer content task-oriented; avoid explanatory marketing text inside tools.
- Preserve data fetching and auth behavior; do not fake interaction unless the task is a static prototype.

Useful local patterns to inspect when they exist in the target repo:

- `frontend/src/components/Layout.tsx`
- `frontend/src/components/CommandPalette.tsx`
- `frontend/src/components/LiveEventMarquee.tsx`
- `frontend/src/pages/Dashboard.tsx`
- `frontend/src/components/dashboard-widgets/*`
- `frontend/src/components/PixelIcons.tsx`
- `frontend/src/index.css`

## Component And Token Guidance

- Keep component APIs small and consistent with local primitives.
- Use `components.build` as the default standard for reusable primitive APIs, anatomy, accessibility, tokenization, state, styling, typing, and docs.
- Prefer `cn(...)`, `class-variance-authority`, `tailwind-merge`, and existing `components/ui/*` variants when present.
- Avoid broad rewrites of shared primitives unless the primitive is the actual problem.
- Define semantic tokens before scattering raw colors through components.
- For black/white themes, introduce hierarchy through opacity, borders, texture, spacing, and typography instead of many hues.
- If a project already uses a theme package, Fumadocs, shadcn/ui, Radix, lucide, or custom primitives, extend those systems rather than bypassing them.

## Primitive Style Contract

Use this contract as the default house style when the current repo has no stronger design system. If the repo already has primitives, align these rules to its tokens and component APIs instead of creating a second system.

### Foundations

- Radius: default to square or tiny radius. Use larger radius only for avatars, pills, maps, charts, or a repo that already has soft geometry.
- Borders: use 1px borders as structure. Prefer border, divider, rail, inset line, or dotted underline before using heavy shadows.
- Shadows: use hard offset shadows or very subtle elevation. Avoid soft floating card stacks.
- Type: body in sans, technical labels in mono. Use mono for commands, IDs, tabs, status, shortcuts, timestamps, and data labels.
- Labels: short, uppercase or small caps when the repo uses that rhythm; keep letter spacing modest and readable.
- Density: technical surfaces should feel compact and intentional, not sparse.
- Focus: every primitive needs visible `focus-visible` treatment that fits the border language.
- Component source: when FarmUI or shadcn-style primitives exist, compose from those primitives first and only create new primitives when the local system is missing the behavior.

### Buttons

- Primary button: solid foreground/background inversion, clear icon when the action benefits from one, stable height, no text wrapping.
- Secondary button: bordered or low-contrast fill, same height as primary, quieter text.
- Ghost button: no border until hover/focus unless it sits in a toolbar.
- Destructive button: explicit destructive label plus danger tone. Do not rely on icon or color alone.
- Loading button: preserve width, disable duplicate submit, include a compact loader plus label such as "Saving" or "Creating".
- Icon button: square hit area, `aria-label`, tooltip for unfamiliar icons, consistent icon size and stroke.
- FarmUI-style button default: border-aware, icon-capable, tight but touch-safe, strong focus-visible, loading-aware, and animated with restrained hover/press feedback.

### Icons

- Prefer `lucide-react` for common interface actions and objects when it is installed: search, copy, check, close, menu, settings, refresh, external link, arrow, user, users, database, calendar, warning, info, lock, key, mail, chart, file, terminal, command, and theme icons.
- Import named lucide icons directly, for example `import { Search, Copy, ExternalLink } from "lucide-react";`.
- Keep lucide icons optically consistent: one size scale per toolbar or row, matching `strokeWidth`, and aligned with text baselines.
- Use icon-only buttons only with `aria-label` and a tooltip for non-obvious actions.
- Use custom pixel/block SVG icons only when the product already has that visual language or the object needs a bespoke symbol.
- Use Pixel Icon Library (`https://pixeliconlibrary.com`) when the project needs a consistent pixelated icon set; keep icons on the 24px grid and align them optically with buttons, badges, and rows.
- Use Iconify (`https://icon-sets.iconify.design/`) when lucide does not provide the right symbol or style, or when the project needs filled, outline, two-tone, multicolor, programming, flag/map, spinner, or alternative UI icon variants.
- When adopting Iconify icons, choose one family per surface, check the icon-set license, preserve grid and viewBox consistency, and match stroke/fill weight to nearby text and controls.
- Use `simple-icons` or official brand SVGs for brand marks when present; do not use lucide for brand logos.
- Use dot/matrix loaders from `https://icons.icantcode.fyi/` for loading/status animation, not as general-purpose action icons.

### Links

- Inline links: underline, dotted underline, or clear color contrast. Avoid barely visible text-only links.
- Technical/action links: pair label with arrow or external-link icon when leaving context.
- Nav links: active state needs text contrast plus structural marker such as rail, inset line, bracket, underline, or background.

### Inputs And Textareas

- Use labels, not placeholder-only fields.
- Keep background close to the app canvas and use border/focus ring for affordance.
- Error state belongs below or next to the field with direct recovery text.
- Textareas need min height, resize policy, and monospace only for code/config input.

### Selects, Comboboxes, And Filters

- Use select for short closed sets, combobox/search for longer sets, segmented control for 2-5 high-frequency modes.
- Show active filters as removable chips when more than one can stack.
- Date/range filters should include presets, custom range, and a visible selected value.

### Checkboxes, Radios, Switches

- Checkbox: multi-select or boolean agreement.
- Radio: mutually exclusive option set.
- Switch: immediate on/off setting. Avoid switches for actions that require confirmation.
- Preserve clear checked, unchecked, disabled, and focus-visible states.

### Badges, Chips, And Status

- Badges should encode state or metadata, not decoration.
- Include text for status; color alone is insufficient.
- Use compact mono chips for technical metadata: framework, adapter, route, version, state, role, or tag.
- Keep badge palettes restrained and mapped to semantic tokens.

### Cards And Panels

- Cards are for repeated items, widgets, modals, or genuinely framed tools.
- Avoid card-in-card nesting. Use separators, headers, bands, rails, or grid lines instead.
- Card header should carry title, metadata/status, and primary action when needed.
- Hoverable cards need visible hover and focus state, not only cursor change.
- Technical cards can use corner ticks, rails, grid texture, pixel/noise texture, or hard offset shadows when that language already exists.

### Tables And Data Rows

- Keep columns stable and scan-friendly.
- Use mono for IDs, versions, paths, amounts, or timestamps when that improves scanning.
- Row actions should be right-aligned or exposed through a predictable menu.
- Loading rows preserve table structure; empty rows include a next action.
- Copyable IDs should have truncation plus copy feedback.

### Tabs And Segmented Controls

- Tabs switch views or panels; segmented controls switch modes or periods.
- Active state should use structural contrast: border, underline, inset marker, or filled segment.
- Keep tab labels short and avoid wrapping inside compact controls.

### Command Palette And Search

- Command/search surfaces should feel like tools: mono shortcut hint, focused input, grouped results, empty state, keyboard support.
- Result rows need icon, title, context/path, and selected/focused state.
- Use command palette for repeated navigation/actions; use page search for content retrieval.

### Code Blocks, Terminals, And Copy Commands

- Code blocks need header, language/title when useful, copy action, and horizontal overflow handling.
- Terminal blocks should preserve prompt, command, output tone, and copy affordance.
- Install command modules should be visible early on technical product pages.
- Copied state should not change layout width.

### Dialogs, Popovers, Tooltips, Toasts

- Dialog: focused task, confirmation, or editor. Include clear title, close affordance, and footer actions.
- Popover: short-lived inline choice, date picker, quick settings, or metadata.
- Tooltip: explain icon-only or uncommon controls. Do not hide critical instructions only in a tooltip.
- Toast: brief confirmation or nonblocking error. Critical recovery belongs inline too.

### Navigation Shells

- Sidebar: clear active route, nested state, scroll behavior, footer/status area when useful.
- Topbar: route context, search/command entry, status/watch indicator, profile/theme controls.
- Mobile nav: preserve primary action and search; do not bury core workflow behind unrelated menus.

### Loaders And Skeletons

- Use skeletons for content structure and compact loaders for actions.
- Technical/agent surfaces should prefer quiet dot-matrix loaders from `https://icons.icantcode.fyi/` when a loader mark is needed.
- Use the dot/matrix source repo, `https://github.com/icantcodefyi/dot-matrix-animations`, when a copied loader needs to be checked, adapted, or credited.
- Loader state needs accessible text or `aria-label`.
- Respect reduced motion; use static dots or skeletons when motion is reduced.

### Charts And Widgets

- Widget frame: title, timeframe/source, value or chart, loading/error/empty fallback.
- Chart: restrained palette, readable tooltip, labels/legend when needed, and no mystery axes.
- Dashboard widgets should be resizable or reflowable without breaking text.

### 3D And Immersive Scenes

- Use Basement Studio-style inspiration (`https://basement.studio`) for bold 3D, interactive scenes, and art-directed motion only when the product's story benefits from it.
- Prefer Three.js or the repo's existing 3D/canvas stack for real 3D scenes; do not fake 3D with heavy decorative gradients when actual inspection or interaction matters.
- Keep the primary scene full-bleed or integrated into the layout, not trapped in a decorative preview card unless the component itself is a card/preview.
- Keep UI controls, text, and CTAs readable above the scene with clear contrast and stable z-index.
- Provide reduced-motion behavior and nonblank fallbacks.
- Verify canvas scenes visually across desktop and mobile: nonblank render, correct framing, no text overlap, acceptable performance, and no console errors.

## Visual System Checklist

Before editing, identify:

- Canvas: dark, light, split, or themeable.
- Structure: rails, gutters, cards, sections, tables, command surfaces, or full-bleed scenes.
- Type: display face, body face, mono face, label case, tracking, and technical microcopy rhythm.
- Shape: radius scale, border style, shadow language, focus ring style.
- State color: success, warning, danger, info, selected, active, disabled.
- Motion: page transitions, hover, loading, content reveal, ambient background.
- Density: marketing, docs, console, dashboard, or editor.
- Proof: code sample, terminal, real data, API route, diagram, product preview, chart, or live interaction.

Encode these in existing tokens/classes where possible before adding new one-off styles.

## Quality Bar

A finished design pass should:

- make the main user workflow clearer
- improve at least one non-happy state
- maintain or improve accessibility and keyboard behavior
- keep responsive layouts stable
- avoid text overlap and layout shift
- pass the repo's normal checks
- be visually verified in a browser when a dev server can run
