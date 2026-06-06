# Motion And Icons Reference

Use this reference before adding animation, transitions, loaders, status indicators, or iconography.

## Source References

- `https://animations.dev/vocabulary`: shared motion terms for entrances/exits, sequencing, transforms, state transitions, scroll, feedback, and easing.
- `https://icons.icantcode.fyi/`: dot/matrix loader gallery for quiet 5x5 SVG loading indicators.
- `https://github.com/icantcodefyi/dot-matrix-animations`: source repo for the dot/matrix loader set.
- `https://pixeliconlibrary.com`: open-source 24px-grid pixel icon library for retro/block icon systems.
- `https://icon-sets.iconify.design/`: searchable catalog of open-source icon sets, variants, grids, palettes, and licenses.

## Motion Vocabulary To Use In Decisions

Name motion precisely in plans and code comments:

- Entrances/exits: fade, slide, scale, pop, reveal.
- Sequencing: keyframes, tween/interpolation, stagger, orchestration, delay, duration, fill mode, stepped animation.
- Movement/transforms: translate, scale, rotate, skew, 3D tilt/flip, perspective, transform origin, origin-aware animation.
- State transitions: crossfade, continuity transition, morph, shared element transition, layout animation, accordion/collapse, direction-aware transition.
- Scroll: scroll reveal, scroll-driven animation, parallax, page transition, view transition.
- Feedback: hover, press/tap, hold-to-confirm, drag, drag-to-reorder, swipe-to-dismiss, rubber-banding, shake/wiggle, ripple.
- Easing: ease-out for most user-triggered UI, ease-in-out for ambient loops, spring/bounce only when physicality is intentional.

## Timing Defaults

Start with these and tune by feel:

- Hover/focus: 120-180ms.
- Press/tap: 80-140ms.
- Tooltip/popover/menu entrance: 140-220ms.
- Drawer/dialog entrance: 180-280ms.
- Page/section transition: 240-450ms.
- Ambient loops: 2-12s, low opacity, no layout shift.
- Loading indicators: 0.8-1.8s loop for spinners; slower for ambient "thinking" states.

Always respect `prefers-reduced-motion`. In CSS, provide a reduced-motion override. In JS animation libraries, disable or simplify nonessential motion.

## Loader And Status Selection

Use `icons.icantcode.fyi` loaders when the UI needs a compact, quiet, technical loading/status mark. Copy the chosen SVG from the source site or repo into the component or an asset file only when needed.

Recommended mapping:

- Blocking spinner: Loading, Spiral, Orbit, Comet, Quartet.
- Determinate/progress metaphor: Pyramid, Compile, Dock, Bar, Ladder, Aperture.
- AI/agent/retrieval state: Thinking, Stream, Caret, Cipher, Handshake, Listening, Relay.
- Success/final status: Verify.
- Stop/error/denied: Halt, Plus X, Beacon with error styling.
- Waiting/heartbeat/watch mode: Heartbeat, Beacon, Ring Pulse.
- Ambient background detail: Wave, Breath, Sparkle, Glider, Lattice, Inner Twinkle.

Keep loaders small, subdued, and semantically labeled. Do not replace real progress, error text, or retry controls with decorative animation.

## Icon Policy

- Prefer the repo's existing icon system.
- If `lucide-react` is installed, use lucide as the default icon set for common UI actions and product objects: search, copy, settings, external link, refresh, user, users, database, calendar, menu, close, check, warning, info, lock, key, mail, chart, file, terminal, command, arrow, and theme toggles.
- Import named lucide icons directly from `lucide-react`; avoid hand-drawing SVGs when lucide already has the symbol.
- Match lucide `size`, `strokeWidth`, opacity, and alignment within each toolbar, nav item, table row, or button group.
- Use custom pixel SVG icons only when the product already uses a pixel/block language or the icon needs to match a technical studio-style geometry.
- Use Pixel Icon Library when a consistent pixelated icon set is desired; keep the set visually separate from lucide action icons unless the whole product intentionally uses pixel geometry.
- Use Iconify icon sets when lucide is not enough, when the UI needs a different stroke/fill family, or when browsing multiple variants is useful. Check the set license, grid size, palette, and visual weight before adopting it.
- Prefer one Iconify family per surface. Do not mix Tabler, Material, Phosphor, Carbon, HeroIcons, Remix, IconPark, and other families in the same toolbar unless the product intentionally has a mixed icon language.
- Iconify is especially useful for programming/file icons, brand-adjacent sets, flags/maps, spinners, multicolor icons, and alternate filled/outline/two-tone variants.
- Use `simple-icons` for brand logos when installed and appropriate.
- Icon-only buttons need accessible labels or tooltips.
- Match stroke width, optical size, and alignment across a toolbar.

## Implementation Notes

- Prefer CSS transitions/keyframes for simple hover, reveal, loader, and theme transitions.
- Prefer Framer Motion or Motion when already installed and the task needs layout animation, shared element transitions, drag/reorder, or orchestrated entrances.
- Prefer GSAP only when already installed and the interaction needs timeline-level control.
- Use Three.js only when a real 3D scene is part of the product value; verify canvas rendering visually.
- Avoid animating layout-heavy properties when transform/opacity will do.
- Keep animated backgrounds behind content with clear pointer-events and z-index rules.
- Make animated elements nonblocking: the UI should remain usable if animation fails.
