# Design Craft References

Read this when a task calls for component polish, interaction refinement, or a dense CRM/business-app design. Use the relevant source alongside the project's existing tokens and primitives. These are companion references; the skill remains usable without installing them.

## Upstream Skills

These companion skills were inspected on 2026-10-04; follow their current pages for updates. The notes below are a selective synthesis, not a bundled copy of either skill.

| Author and skill | Best use | Source |
| --- | --- | --- |
| Jakub Krehel — `better-ui` | Refining the visual details of an existing component | [skills.sh](https://www.skills.sh/jakubkrehel/skills/better-ui) · [reviewed SKILL.md](https://github.com/jakubkrehel/skills/blob/267330e1adfc66a718fb65fa6918c1f06d0a689e/skills/better-ui/SKILL.md) |
| Emil Kowalski — `emil-design-eng` | Deciding how interactions respond and whether motion helps | [skills.sh](https://www.skills.sh/emilkowalski/skills/emil-design-eng) · [reviewed SKILL.md](https://github.com/emilkowalski/skills/blob/e8a175de22ae1e49370fc144c1f3bb9aeedf988d/skills/emil-design-eng/SKILL.md) |

### Jakub Krehel: better-ui

Useful details to carry into a polish pass:

- Relate a rounded container's outer curve to its inset and inner curve. Inspect uneven-looking nested corners instead of assigning the same radius everywhere.
- Check perceived centering of asymmetric icons; mathematical centering can still look unbalanced beside a label.
- Keep dividers and selected-state borders that explain structure. Use layered shadows when the actual purpose is elevation.
- Keep icon weight consistent with neighboring text, and express state through the existing icon's styling where possible.
- Preserve visible confirmation after an animated state change ends. A successful action should remain understandable with motion disabled.

The upstream skill supplies exact values for some effects. Consult its recipe when deliberately using that effect; do not treat every control as a candidate for the same motion treatment.

### Emil Kowalski: emil-design-eng

Use interaction frequency and purpose to choose motion. Repeated operations should stay immediate; occasional transitions can explain a change in location or state. The general timing and origin rules already live in [Motion And Icons](motion-and-icons.md).

Two details worth applying during implementation:

- For a group of tooltips, use the primitive's delay/skip-delay support: a brief initial delay avoids accidental activation, while moving between nearby controls should not repeatedly impose that wait or entrance animation. Check focus-triggered behavior separately.
- Exercise transitions while they are already running: reopen a closing panel, dismiss an entering notification, or change tabs rapidly. The displayed state must follow the newest action without waiting for decorative movement to finish.

Review motion at normal speed for responsiveness and at reduced playback speed for defects. Respect the user's reduced-motion preference as a separate behavior, not merely a slower replay.

## Applying The References Together

Begin with the user's actual flow and the app's existing component. Identify a concrete defect, then use the relevant source to refine it. Choose one implementation for each interaction; do not combine overlapping animation recipes or install another motion library just to reproduce a demo.

For a CRM filter control, for example:

1. Keep the current field and selected value legible in the closed trigger.
2. Inspect alignment, corners, border purpose, and icon weight.
3. Keep opening, choosing, and clearing responsive; preserve menu keyboard behavior and focus return.
4. Verify long values, no results, rapid changes, and narrow layouts against the real data flow.

When reporting a polish pass, connect the observed issue to the change and its user impact. A compact before/after table is useful when comparing several fixes. State which interactions were actually verified.

## Sales CRM Reference

[Live Sales CRM](https://sales-crm-kargulstudio.vercel.app/) — inspected on 2026-10-04 in the desktop Companies view, including opening and dismissing the owner filter.

| Observed pattern | Why it is a useful reference |
| --- | --- |
| Navigation grouped into primary work, teams, reporting, and pipelines | Separates task destinations from saved scopes. |
| Compact toolbar with sort, owner, stage, and recent-activity controls | Keeps query context near the records. |
| Dense company rows with stage chips and named owner avatars | Combines account context with ownership. |
| Inline probability bars with percentages and small activity charts | Adds visual scanning cues beside numeric data. |
| Checkbox selection, row emphasis, and a bottom calculation strip | Gives a reference for selection and table summaries. |
| Dark neutral surfaces, thin separators, and a prominent creation action | Creates hierarchy within a data-heavy screen. |

This is a composition reference, not a component package. The inspection did not establish persistence, complete workflow behavior, mobile quality, or accessibility compliance. Navigation labels alone do not prove that those flows are implemented.

### Adaptation Recipe For A Business App

- Build from the local sidebar, tabs, menu, table, badge, avatar, and meter/chart primitives. Keep the reference's information relationships while using the product's own theme.
- Define what each control scopes and whether the table footer summarizes the current page, filtered records, or selected records. Keep query state and displayed totals consistent.
- Make stage-chip overflow inspectable, expose full truncated names, and preserve readable numbers. Small activity graphics need a textual explanation or accessible data when they carry meaning.
- Distinguish a probability meter from task progress. Give the metric a meaningful accessible name and preserve its numeric value.
- For narrow screens, prioritize columns and provide intentional table scrolling or a suitable record layout. Keep filters and row actions reachable; validate this in the target app.
- Use actual data or clearly identified demo content. Verify filters, sorting, selection, detail opening, and recovery states instead of assuming a visual match makes the flow complete.

For implementation sources, continue with [UI Components](ui-components.md). For behavior coverage, use [Interaction Language](interaction-language.md).
