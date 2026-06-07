# Interaction Language

Use this reference before changing how a UI behaves. The goal is to make every interaction legible, responsive, accessible, and visually consistent with the product surface.

## Interaction Principles

- Make the next action obvious from the current state.
- Confirm user intent only when the action is destructive, costly, or hard to undo.
- Prefer inline feedback over distant status messages.
- Keep controls stable while content loads; do not move the target under the pointer.
- Use the same visual treatment for the same interaction across the app.
- Every interactive element needs hover, focus-visible, active/pressed, disabled, and loading behavior when applicable.
- Keyboard flows should match pointer flows: tab order, shortcuts, escape/close, enter/submit, arrow navigation for menus/lists.
- High-frequency interactions should feel immediate. Command palettes, keyboard shortcuts, row actions, toolbar buttons, and repeated dashboard controls should avoid decorative entrance/exit motion.
- Add motion only when it clarifies state, confirms feedback, explains spatial movement, or prevents a jarring change.

## Navigation

Use navigation to communicate location and scope:

- Active route: visible text contrast plus structural marker, not color alone.
- Sidebar: stable width, scrollable content, persistent primary sections, compact labels, clear nested state.
- Top bar: search/command entry, status, user/theme controls, primary route context.
- Mobile: use a drawer/sheet or compact nav that preserves search and primary actions. Avoid hiding critical actions behind unrelated menus.
- Docs navigation: make current page, section nesting, search, page actions, next/previous links, and feedback controls easy to scan.

## Command And Search

Command palettes and search should feel fast and useful:

- Trigger with visible button and keyboard shortcut when the app supports shortcuts.
- Keyboard-triggered command palettes should open instantly or nearly instantly; repeated expert actions should not wait for flourish.
- Include recent, suggested, and route/action results when useful.
- Keep input focused on open; close on escape; preserve scroll/focus behavior on close.
- Show empty, loading, and no-results states.
- Highlight matched text without harming readability.
- For docs, search results need title, section, snippet, and path.
- For apps, command results can include route, entity, action, and status.

## Copy And Install Affordances

Copy interactions are core for technical products:

- Put copy buttons next to commands, IDs, API keys, snippets, and URLs.
- Show copied confirmation for 1-2 seconds.
- Keep the code text selectable and horizontally scrollable if needed.
- Use monospace, stable height, and a clear boundary around command modules.
- Preserve the original value; do not replace it with the confirmation text if that causes layout shift.

## Forms And Filters

Forms should reduce uncertainty:

- Label every input; placeholders are not labels.
- Group related controls and separate optional/advanced sections.
- Validate near the field and summarize only when the form is complex.
- Show pending state on submit and prevent duplicate submission.
- Keep filter controls compact and reversible; include clear/reset when multiple filters can stack.
- Date controls need readable selected range, quick presets, custom range, and empty state.

## Tables And Lists

Tables should make data scannable:

- Use stable columns, sticky headers when tables scroll, and predictable row height.
- Include search, filters, sort, pagination or infinite loading, and row-level actions when the data set needs them.
- Use status badges with text, not color alone.
- IDs should be copyable and truncated with a full-value affordance.
- Empty rows should say what the user can do next.
- Loading rows should preserve table structure.
- Row hover should clarify clickability; selection should be unmistakable.

## Cards, Widgets, And Dashboards

Widgets should carry one job each:

- Metric widgets: label, value, trend, timeframe, and loading/error fallback.
- Chart widgets: axis/legend clarity, tooltip, empty state, and filter period.
- Activity widgets: timestamp, actor, action, target, status.
- Draggable/resizable widgets: visible handle, hover affordance, drop target, keyboard-safe fallback when possible.
- Avoid nesting cards. Use separators, headers, or section bands instead.

## Charts And Data Visuals

Charts are interaction surfaces, not decoration:

- Explain units, timeframe, and data source when not obvious.
- Tooltips should include series label, value, date/time, and useful metadata.
- Use restrained fills and muted gridlines; avoid rainbow palettes unless categories require it.
- Show loading, no-data, and error states inside the chart frame.
- Let users change timeframe where the chart implies time.

## Loading, Empty, Error, And Success

State language:

- Loading: preserve layout, show what is loading, and avoid blocking unrelated controls.
- Empty: name the missing object and offer the next useful action.
- Error: state what failed, why if known, and provide retry or recovery.
- Success: confirm the completed action near where it happened.
- Unauthorized/denied: explain access limits and show the safest next path.
- Sync/watch/live states: show connection, refreshing, stale, up-to-date, error, and reconnecting states.

## Dialogs, Popovers, Drawers, And Toasts

- Dialogs: use for focused tasks or confirmations. Trap focus, restore focus on close, close on escape unless unsafe.
- Popovers: use for lightweight choices, date pickers, quick filters, and inline details.
- Drawers: use for side workflows, details, or inspector panels that need more space.
- Toasts: use for brief nonblocking feedback; never rely on toast alone for critical errors.
- Destructive actions: use explicit labels, clear consequences, and confirmation when irreversible.

## Theme, Density, And Responsiveness

- Theme toggle should preserve context and avoid flashing.
- Dark/light modes need separate contrast checks, not just inverted colors.
- Dense UIs need smaller type and spacing, but still require touch-safe controls on mobile.
- Mobile layouts should reflow, not merely shrink. Watch for clipped labels, horizontal overflow, and buried primary actions.
- Use responsive constraints for boards, grids, toolbars, icon buttons, counters, and tiles.

## Acceptance Checklist

An interaction pass is complete when:

- the primary action is visible
- keyboard and pointer paths work
- loading/empty/error/success states are covered
- focus-visible is clear
- destructive actions are protected
- controls do not jump during state changes
- mobile flows retain the same essential capabilities
- browser verification confirms no overlap, clipping, or console errors
