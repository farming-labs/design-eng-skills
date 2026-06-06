# Implementation Patterns

Use this reference when building a component library, designing reusable primitives, or improving an app by mining existing source. These patterns are distilled from the provided component sources and public inspiration sites; adapt them to the current repo instead of copying blindly.

## Package Stack Patterns

Common stacks that produced the strongest UI:

- App framework: Next.js for docs/product sites; Vite + React for dense studio/admin apps.
- Styling: Tailwind CSS, usually with `clsx`, `tailwind-merge`, and a local `cn(...)` helper.
- Component APIs: Radix primitives plus shadcn-style wrappers, `@radix-ui/react-slot`, `class-variance-authority`, forwardRef, native props, and `asChild` where useful.
- Icons: `lucide-react` for ordinary UI actions and objects; Iconify for alternate open-source icon families and variants; pixel/block icons only for deliberate pixel/studio language; official brand SVGs or `simple-icons` for brands.
- Command/search: `cmdk` for command palettes and searchable action menus.
- Feedback: `sonner` or toast primitives for nonblocking confirmation; inline feedback for critical errors.
- Charts/data: `recharts`, maps, XYFlow, and number-flow style count animation for dashboards.
- Dates/forms: Radix/select/popover, `react-day-picker`, date helpers, and form primitives.
- Motion: CSS keyframes/Tailwind animation for simple states; Framer Motion/Motion or GSAP for orchestrated animation; Three.js/R3F/drei for real 3D scenes.
- Code rendering: `sugar-high` or syntax highlighter packages for code blocks and terminal samples.
- Docs runtime: docs/theme packages, Fumadocs-style layouts, page actions, search, MCP/llms.txt/docs API affordances when relevant.

## Primitive Implementation Patterns

### Buttons

- Use a `buttonVariants = cva(...)` map for `variant` and `size`.
- Extend native button props and variant props; expose `asChild` when links/actions need button styling.
- Include `default`, `secondary`, `outline`, `ghost`, `link`, `destructive`, and `icon` sizing when the app needs them.
- Keep loading state width stable; use a compact loader plus label or icon.
- Include `focus-visible`, disabled opacity, icon sizing via `[&_svg]`, and no wrapping.

### Cards

- Prefer anatomy exports: `Card`, `CardHeader`, `CardTitle`, `CardDescription`, `CardContent`, `CardFooter`.
- For docs/technical cards, add rails, corner ticks, mono labels, chips, and subtle background icons or texture.
- For dashboards, card header carries label, value/status, timeframe/filter, and action; body carries chart/table/list with loading/error/empty fallback.
- Avoid card-in-card nesting; use separators, section bands, grid lines, or internal headers.

### Command Palettes

- Use `cmdk` with grouped results, search input, icon, empty state, separators, and keyboard flow.
- Results should include icon, title, description/context/path, category, keywords, and disabled states when actions depend on plugins/features.
- Trigger with visible search/command button and shortcut when the app supports shortcuts.

### Copy And Code

- Use `navigator.clipboard.writeText(...)` with copied state around 1-2 seconds.
- Use lucide `Copy`, `Check`, `Clipboard`, `Terminal`, or `Sparkles` icons.
- Keep command text selectable and stable; copied confirmation should not shift layout.
- For install commands, support package-manager menus when useful: npm, pnpm, yarn, bun.
- Code blocks need header/title, language, copy action, and horizontal overflow handling.

### Forms, Filters, And Dates

- Labels are required; placeholders are hints only.
- Use popover/calendar/date-range primitives for date filters.
- Show active filters as removable chips when filters can stack.
- Validate near the field and show pending state on submit.

### Tables And Lists

- Use stable columns, row actions, status badges with text, copyable IDs, loading rows, and empty rows with next actions.
- Dense apps benefit from mono IDs/timestamps and muted borders.
- Row hover should indicate clickability; selected rows need more than color.

### Tabs, Segmented Controls, And Framework Switchers

- Tabs switch panels/views; segmented controls switch compact modes.
- Framework/package-manager tabs work well for docs and install guides.
- Active state should use border/underline/inset/fill, not color alone.

### Dashboard Widgets

- Build widgets as small operational units: title, metric/value, trend, timeframe, filter, body, and fallback states.
- Support resize/reorder/drop targets only when the UX needs customization.
- Charts need readable tooltips, axis/legend clarity, muted gridlines, and no-data/error/loading states.

### Section Blocks

- Product sections should start from purpose: hero, proof, features, workflow, integrations, pricing, comparison, FAQ, changelog, CTA.
- FarmUI/Efferd/21st/React Bits-style blocks can inspire structure, but rewrite copy and adapt tokens.
- Good technical sections often combine a mono label, clear headline, concise proof, command/code module, and one visual artifact.
- Animated backgrounds, beams, grids, ripples, glows, or shaders should support the story and remain behind content.

## Visual Patterns That Work

- 1px borders, rails, gutters, separators, dotted underlines, corner ticks, and inset markers.
- High-contrast black/white or near-neutral foundations with restrained accent color.
- Geist or similar sans/mono pairing; mono for commands, IDs, status, chips, shortcuts, and technical labels.
- Compact chips for frameworks, adapters, versions, states, and integrations.
- Real proof surfaces: terminal command, code block, preview viewport, chart, map, database graph, or event stream.
- Square/zero-radius discipline for docs/studio surfaces; softer `rounded-md/lg` only when the component library already uses softer geometry.
- Texture and motion used as system language: grid, pixel/noise, beam, ripple, marquee, view transition, copy confirmation, and live status.

## Source-Mining Checklist

When analyzing an existing repo before a design pass, inspect:

- `package.json` dependencies and scripts.
- `components/ui/*`, `components/*`, `app/page.tsx`, `app/globals.css`, `app/global.css`, route layouts, dashboard widgets, and docs config.
- Existing `Button`, `Card`, `Command`, `Copy`, `CodeBlock`, `Tabs`, `Dialog`, `Popover`, `Table`, `Chart`, `Skeleton`, and `Toast` implementations.
- Icon imports and whether lucide, Iconify, simple-icons, pixel icons, or custom SVGs are already used.
- Radius and color usage; decide whether the surface is square technical, soft product, or mixed.
- Motion files and missing `prefers-reduced-motion` handling.
- Loading, empty, error, success, disabled, selected, active, hover, focus-visible, and mobile states.

## Quality Bar

A component or app pass should leave behind:

- reusable primitives rather than page-only markup
- clear variant and size APIs
- accessible labels, focus states, and keyboard support
- consistent icon policy
- covered loading/empty/error/success states
- responsive layouts without clipped text
- verification through lint/typecheck/build and browser inspection when feasible
