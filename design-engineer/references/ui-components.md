# UI Components

Use this reference when the local UI kit lacks a component, the user requests library recommendations, or a design pass needs a concrete implementation reference. Start with the relevant category or recipe; there is no need to load every linked site.

## Discovery And Selection

The sources in the first six categories below were found in [Designeer's component directory](https://www.designeer.xyz/components) and checked against their own sites on 2026-10-04. The final category adds complementary sources. This is a selected working set, not a mirror of the directory. The usage advice and recipes are this skill's guidance.

1. Inspect local components, package versions, theme tokens, and any registry configuration such as `components.json`.
2. Decide whether the gap is behavior (an accessible primitive), composition (a widget or page block), or visual treatment (motion or effects).
3. Open the relevant source's component docs and example. Check its current API, dependencies, source availability, and license for the specific item; a library may mix open components with paid blocks.
4. Choose the smallest addition that fits the app. Keep one foundation for overlapping controls; a visual refresh alone does not justify migrating the component system.

Treat directory blurbs and gallery previews as discovery aids. The original project docs and code determine compatibility. These links are research starting points, not installation instructions or guarantees of accessibility.

## Component Sources

### Foundations And Form Controls

| Source | Components to inspect | Use when / integration detail |
| --- | --- | --- |
| [shadcn/ui](https://ui.shadcn.com/docs/components) | Field, Combobox, Command, Sidebar, Data Table, Calendar, Empty | Extend an app that already owns shadcn components. Inspect its configured primitive and local wrappers; examples from a different preset may use different composition APIs. |
| [Base UI](https://base-ui.com/react/overview/quick-start) | Autocomplete, Combobox, Number Field, Field, Dialog, Menu | Build custom visuals on unstyled React controls. Read composition and portal setup before styling; preserve the provided interaction behavior. |
| [Radix Primitives](https://www.radix-ui.com/primitives/docs/overview/introduction) | Dialog, Dropdown Menu, Popover, Tabs, Tooltip, Slider | Extend an existing Radix system. Keep its focus management, portal behavior, and composition contract when adding wrappers or animation. |
| [coss ui](https://coss.com/ui) | Command, Number Field, OTP Field, Input Group, Drawer, Empty | Look for styled Base UI compositions. Adapt its theme and wrapper APIs instead of treating it as a drop-in replacement for Radix components. |

### Data And Product Workflows

| Source | Components to inspect | Use when / integration detail |
| --- | --- | --- |
| [Kibo UI](https://www.kibo-ui.com/) | Dropzone, Editor, Tree, Kanban, Gantt, Color Picker, Code Block | Fill gaps beyond basic shadcn controls. Inspect each component's dependencies; a board, editor, or timeline still needs the app's data and persistence behavior. |
| [Tremor](https://www.tremor.so/) | Charts, metric displays, tables, dashboard blocks | Build analytical screens. Choose the current copy-and-paste component or an existing package API deliberately; do not mix installation models. |

### Motion And Feedback

| Source | Components to inspect | Use when / integration detail |
| --- | --- | --- |
| [Motion Primitives](https://motion-primitives.com/docs) | Transition Panel, Animated Background, Text Effect, Morphing Dialog | Study continuity between states and small animated compositions. Keep the app's established semantics and provide reduced-motion behavior. |
| [Animate UI](https://animate-ui.com/docs/components) | Accordion, Dialog, Tabs, Code Tabs, Notification List | Add motion to familiar controls. Select the documented Radix, Base UI, or Headless UI variant that matches the project. |
| [SmoothUI](https://smoothui.dev/) | Dynamic Island, AI Prompt Input, Infinite Slider | Explore expressive status, input, and presentation components. Inspect the chosen component's runtime dependencies and tune movement to interaction frequency. |
| [NumberFlow](https://number-flow.barvian.me/) | Animated numeric values and grouped number transitions | Animate meaningful metric changes. Check locale and formatting limitations; use a static formatted number where unsupported and retain the motion preference setting. |

Use [Motion And Icons](motion-and-icons.md) for timing, interruption, touch behavior, and reduced-motion decisions. A component demo's default animation is a starting point.

### Expressive Components And Product Demos

| Source | Components to inspect | Use when / integration detail |
| --- | --- | --- |
| [Magic UI](https://magicui.design/docs/components) | Terminal, Code Comparison, Animated Beam, Marquee, Bento Grid | Explain a developer product or integration flow. Tie animated connections to real relationships and keep important text readable without animation. |
| [Aceternity UI](https://ui.aceternity.com/components) | Timeline, Compare, Expandable Card, File Upload, Resizable Navbar | Explore narrative sections and richer interactions. Verify keyboard and touch paths for the selected example and remove decoration that competes with the task. |
| [React Bits](https://reactbits.dev/) | Text animations, interactive components, animated backgrounds | Find effects for a deliberate creative direction. Choose a variant matching the project's language and styling, inspect rendering cost, and preserve a static fallback. |

### Page Sections And Layouts

| Source | Components to inspect | Use when / integration detail |
| --- | --- | --- |
| [Tailark](https://tailark.com/) | Heroes, feature sections, complete marketing page compositions | Establish a coherent product page. Prefer sections sharing a visual system; rewrite content and use the app's typography and spacing. |
| [Shadcnblocks](https://www.shadcnblocks.com/) | Application shells, dashboards, data tables, pricing, product lists | Start from a larger composition. Check access terms and the selected primitive variant before bringing in source. |
| [HyperUI](https://www.hyperui.dev/) | Tailwind application, marketing, and ecommerce patterns | Use markup and layout examples without adopting another React component system. Supply the actual behavior for interactive patterns. |
| [21st.dev](https://21st.dev/) | Community navigation, buttons, cards, heroes, chat examples | Compare visual directions or discover a missing pattern. Inspect the individual author's source and terms; entries do not share one implementation contract. |

### Chat Interfaces

| Source | Components to inspect | Use when / integration detail |
| --- | --- | --- |
| [Prompt Kit](https://www.prompt-kit.com/docs) | Chat Container, Message, Prompt Input, File Upload, Source, Scroll Button | Compose a chat surface around an existing backend. Connect components to real streaming, attachment, cancellation, and error states. |

### Complementary Sources Beyond The Directory Selection

| Source | Components to inspect | Use when / integration detail |
| --- | --- | --- |
| [React Aria](https://react-aria.adobe.com/) | ComboBox, DatePicker, Table, Tree, drag-and-drop collections | Complex keyboard, internationalization, and collection behavior shape the task. Style its components to match the product instead of rebuilding those behaviors. |
| [Mantine](https://mantine.dev/) | Combobox, dates, forms, Dropzone, notifications, Stepper | The project already uses Mantine or needs a broad styled React kit. Account for its provider, styles, and theming before adopting individual components. |
| [AI Elements](https://elements.ai-sdk.dev/) | Conversation, Message, Prompt Input, Sources, Tool, Confirmation | A chat or agent app needs UI aligned with the AI SDK. Verify component and SDK versions and map actual tool/message states to the display. |

## Recipes By Product Need

These recipes describe what to adapt and what makes it complete. Reuse local primitives for the same anatomy where they exist; a linked example does not require adding its library.

### Searchable Selection And Filters

Start with the [shadcn component index](https://ui.shadcn.com/docs/components), Base UI Combobox, or React Aria ComboBox. Separate typed query from selected value. Cover no matches, asynchronous loading, failed search, clear selection, disabled options, and long labels. For multi-select, keep removable selections visible and provide a clear-all action when useful.

### File Uploads

Inspect [Kibo Dropzone](https://www.kibo-ui.com/components/dropzone). Compose a labeled picker, drop target, file list, per-file progress, retry, cancel, and remove actions. Dragging needs a click/keyboard alternative. Show accepted types and size limits, report rejection beside the file, and distinguish selection from a completed server upload.

### Date Ranges And Scheduling

Use a local calendar/date picker, React Aria dates, or Mantine dates. Define whether the value is a calendar date or a timestamp before wiring it to the backend. Include selected-range text, relevant presets, unavailable dates, clear/reset, and narrow-screen behavior. Preserve locale and timezone meaning in serialization.

### Navigation And App Shells

Inspect shadcn Sidebar or a Shadcnblocks application shell. Compose workspace selection, primary navigation, secondary actions, search, and account controls according to the product. Keep the active route visible when collapsed, preserve navigation on mobile, and give icon-only controls accessible names.

### Tables And Bulk Actions

Start with the app's existing table or shadcn Data Table. Keep sorting, filtering, pagination, and selection consistent with the data source. Clarify whether selection means visible rows or all matching records. Provide a bulk-action toolbar, partial-failure feedback, stable row IDs, and recovery when a refresh removes a selected record.

For a concrete composition example, see the [Sales CRM reference](design-craft.md#sales-crm-reference): grouped navigation, a compact filter bar, stage chips, owner avatars, and inline probability/activity visuals. Its inspection notes distinguish visible design from behavior that still needs verification.

### Trees And Hierarchical Browsers

Inspect [Kibo Tree](https://www.kibo-ui.com/components/tree) or React Aria Tree. Distinguish expansion, selection, and opening an item. Preserve expanded paths across data refreshes, handle unloaded children, and keep row actions separately reachable. Use a tested tree primitive when tree keyboard behavior is required; ordinary nested navigation may only need disclosure buttons and links.

### Kanban And Timelines

Inspect [Kibo Kanban](https://www.kibo-ui.com/components/kanban) or [Gantt](https://www.kibo-ui.com/components/gantt). Define stable item IDs, order, allowed destinations, and persistence before animating movement. Provide a menu or keyboard alternative to dragging, display empty columns, and restore or reconcile state after a failed update. A Gantt also needs a readable timescale and a compact fallback on narrow screens.

### Charts And Live Metrics

Inspect [Tremor charts](https://www.tremor.so/charts), the local chart wrapper, and NumberFlow only if transitions improve comprehension. Define units, aggregation, timeframe, and missing-value behavior. Preserve zero as data, distinguish stale data from loading, and include a textual summary or table for values that cannot be accessed through chart interaction.

### Activity And Notification Panels

Combine local list rows, avatars, status badges, and timestamps; Animate UI's Notification List can inform transitions. Include unread/read state, grouping when useful, links to the affected objects, and empty/error states. Insert new events without pulling the user away from older content they are reading.

### Onboarding And Multi-Step Forms

Use local form controls or Mantine Stepper with the existing form layer. Keep entered data when moving between steps, validate the current step, and show progress using real completion state. Allow review before submission and make resume/retry behavior explicit where the workflow supports it. A visual stepper does not own validation or saving.

### Inspectors And Detail Overlays

Start with the local Dialog/Sheet or coss Drawer. Preserve the selected item's identity when a list updates behind the panel. Choose modal focus behavior deliberately, restore focus on close, and make long content scroll within a usable narrow-screen layout. A morphing transition must not remove the overlay's semantics.

### Changing Panels And Numeric Feedback

Inspect [Motion Primitives Transition Panel](https://motion-primitives.com/docs/transition-panel) and NumberFlow. Keep tab semantics separate from the animated content container. Handle rapid selection changes without stale panels or delayed input, reserve space where useful, and show final values immediately when reduced motion is requested.

### Code And Technical Product Previews

Inspect Kibo Code Block or Magic UI Terminal/Code Comparison. Keep code selectable, provide copy feedback and horizontal overflow, and label illustrative output so it cannot be confused with live execution. Use a static preview when animation would delay reading an install command or result.

### Marketing Sections And Comparisons

Start with Tailark, HyperUI, or Shadcnblocks for the section's structure. Use Aceternity Compare when a before/after view explains the product. Align sections to shared gutters, type, and spacing; replace demo claims, logos, prices, and imagery with appropriate content. Interactive comparisons need a labeled keyboard control and a useful touch layout.

### Chat And Agent Workspaces

Inspect [Prompt Kit Prompt Input](https://www.prompt-kit.com/docs/prompt-input) or AI Elements. Compose history, input, attachments, message actions, sources, and tool status according to the backend contract. Cover streaming, stop, retry, failed attachments, and long code blocks. Preserve the user's scroll position; offer jump-to-latest when they have scrolled away. Show actual reported status rather than fabricated progress.

## Adapting A Component Into The App

- Keep a short note in the implementation summary or existing attribution file identifying the source component and meaningful changes. Preserve any license notices required by copied code.
- Read the current install instructions; do not invent registry namespaces or import paths. Review generated files and dependencies, especially attempts to replace existing primitives or global CSS.
- Map colors, typography, spacing, radii, shadows, and icon sizes onto local tokens. Remove example branding, demo data, and unnecessary wrapper layers.
- Match React/framework and styling versions, primitive composition, ref handling, controlled state, and server/client boundaries. Read browser APIs on the client and avoid generating unstable markup during hydration.
- Wire real data, persistence, and failure recovery. A polished demo does not supply the product's backend behavior.
- Verify keyboard and pointer operation, focus return, touch layouts, long content, applicable loading/empty/error states, and reduced motion. For animated or canvas effects, inspect rendering cost and offscreen behavior.
- Use the app's normal typecheck/build checks and visually inspect the affected flow. Test behavior added by the adaptation, especially saving, selection, uploads, and drag alternatives.
