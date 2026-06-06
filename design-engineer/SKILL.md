---
name: design-engineer
description: "End-to-end frontend design engineering workflow for improving React, Next.js, Vite, docs sites, dashboards, component systems, product websites, and studio-style apps. Use when the user asks to make UI/UX/design/frontend/website/docs/app screens more polished, curated, premium, usable, production-grade, responsive, animated, or visually consistent; when editing TSX/JSX/CSS/Tailwind/Fumadocs/shadcn/Radix/lucide interfaces; when choosing design-engineering tools or inspiration resources; or when adding loaders, icons, empty/loading/error states, motion, interaction details, and visual QA."
---

# Design Engineer

## Overview

Use this skill to turn rough or merely functional frontend work into a carefully designed, shippable interface. Read the app first, preserve the stack's local conventions, then improve the actual product surface rather than adding generic decoration.

## Quick Start

1. Inspect the project before proposing visuals:

```bash
python /path/to/design-engineer/scripts/design_audit.py <app-or-package-path>
```

2. Read `references/design-language.md` when the target is a docs site, product landing page, component library, studio app, dashboard, or technical OSS website.
3. Read `references/implementation-patterns.md` when building a component library, adding reusable primitives, or mining existing source for package/component patterns.
4. Read `references/interaction-language.md` before changing navigation, command palettes, tables, forms, copy actions, loading/empty/error states, dialogs, charts, or mobile flows.
5. Read `references/design-tools.md` when choosing design-engineering tools, design-to-code workflows, source-of-truth strategy, asset sources, or inspiration libraries.
6. Read `references/motion-and-icons.md` before adding animation, transitions, loaders, status indicators, or iconography.
7. Implement the smallest complete design pass that improves the real workflow.
8. Run the app's typecheck/build/tests when available, then visually verify the edited screens in a browser across desktop and mobile.

## Workflow

### 1. Understand the Surface

- Identify whether the screen is a docs/product website, operational app, dashboard, editor, component library, auth surface, or interactive demo.
- Open the primary route/component and its local primitives before touching styles.
- Prefer existing libraries and patterns: local UI components, `cn` helpers, Tailwind tokens, shadcn/Radix primitives, lucide icons, docs/theme packages, motion libraries already installed, and existing data/loading flows.
- If the user names inspiration repos, URLs, screenshots, or files, inspect those sources directly. Do not rely on private/local exemplar paths unless the user provides them in the current task.

### 2. Set a Design Direction

- Choose a direction from the product's job, not from generic trends.
- For docs and OSS websites, favor strong first-viewport product signal, useful install/code affordances, crisp navigation, search, examples, and agent/AI-readable affordances when relevant.
- For studio/dashboard/productivity apps, favor density, scanability, stable controls, keyboard access, command palette/search, clear loading/empty/error states, and quiet hierarchy over marketing composition.
- Define the visual grammar in tokens: background, foreground, muted text, border, accent, radius, shadow, spacing, type scale, motion duration/easing.

### 3. Design the Whole State, Not Just the Happy Path

Cover expected states before calling the UI done:

- loading, skeleton, pending, and optimistic states
- empty states with useful next actions
- errors and denied/unauthorized states
- success/confirmation feedback
- hover, focus-visible, pressed, disabled, selected, active route, and drag/reorder states where applicable
- mobile navigation, long text, overflow, narrow cards, and touch targets

### 4. Apply Craft Rules

- Make the primary screen usable immediately; do not replace app work with a marketing landing page unless that is the requested artifact.
- Use real content, real product affordances, and real data shape from the app wherever possible.
- Keep layout stable with explicit dimensions, grid tracks, min/max constraints, aspect ratios, and overflow behavior.
- Use icons for recognizable tool actions. Prefer `lucide-react` when present; use local pixel/custom icons only when that visual language already exists.
- Use cards only for repeated items, widgets, modals, or genuinely framed tools. Avoid cards inside cards.
- Avoid decorative orbs, one-note gradients, bokeh backgrounds, and generic glass panels unless the codebase already uses them with restraint.
- Keep text inside containers across mobile and desktop; adjust layout before shrinking type too far.
- Respect `prefers-reduced-motion` and avoid animation that hides latency or blocks comprehension.

### 5. Verify Like a Designer-Engineer

Before finishing:

- Run formatter/linter/typecheck/build/test commands that are standard in the repo.
- Start the dev server for frontend apps when feasible and inspect the edited routes in a browser.
- Check desktop and mobile widths for overlaps, clipped text, unreadable contrast, broken scroll, blank canvases, console errors, and stalled loading states.
- For 3D/canvas-heavy work, verify the canvas is nonblank, framed, responsive, and interactive.
- Summarize changed files and the verification performed.

## Bundled Resources

- `scripts/design_audit.py`: quick project scan for stack, UI files, motion/icons, colors, radius, and visual-risk signals.
- `references/design-language.md`: portable technical-product design language for docs, OSS sites, dashboards, and studio apps.
- `references/implementation-patterns.md`: package and component implementation patterns for building polished apps and component libraries.
- `references/interaction-language.md`: interaction grammar for navigation, command, copy, forms, tables, charts, states, dialogs, and mobile.
- `references/design-tools.md`: tool directory and selection guide for design engineers.
- `references/motion-and-icons.md`: motion vocabulary, loader/icon choices, and animation implementation rules.

## Example Requests

- "Use `$design-engineer` to make this docs homepage feel curated and technically credible."
- "Polish this dashboard so it feels like a dense, production-grade studio app."
- "Improve the loading, empty, and error states for this table."
- "Add tasteful motion and status loaders without making the app noisy."
- "Make this OSS docs site responsive and visually consistent."
