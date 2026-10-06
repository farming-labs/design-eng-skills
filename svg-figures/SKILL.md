---
name: svg-figures
description: "Design and build animated SVG figures for product sites, docs, and blogs: isometric and hairline drawings, interactive illustrations that react to the pointer, labelled diagrams with wires, nav glyphs, and figures that play a story in step with the copy around them. Use when the user asks for SVG motion, illustrations, iso or isometric figures, hairline drawings, animated diagrams, hover illustrations, callouts or leader lines, glyph animations, or names an inspiration such as iso-figures, Hairline, Linear's illustrations, or an X post of an animated figure."
---

# SVG Figures

## Overview

Use this skill to draw figures that explain something and move with intent: a stopwatch that races frameworks, a build output that assembles plate by plate, a computer that types `farm dev`, a nav glyph that wakes on hover. The figures are plain SVG, a projection, and a handful of springs. No figure library, no canvas, no video.

The work is mostly restraint. Draw fewer lines, round every corner, give the one thing that matters the bright edge, and write the words beside the drawing on a wire, not over it.

## Quick Start

1. Read [Inspirations](references/inspirations.md) before choosing a direction. When the user links one, open it and study its states (rest, hover, mid-motion) before drawing anything.
2. Pick a grammar below. Do not mix them inside one page.
3. Read [Build and Verify](references/build-and-verify.md) before writing code: the projection, rounded solids, painter's order, springs, clocks, pointer mapping, callouts, and the screenshot harness.
4. Draw the rest pose first. It is what most people see, what reduced motion shows, and what server rendering emits.
5. Add motion that tells the figure's story, then the pointer, then the labels.
6. Verify frame by frame in a real browser before showing anyone.

## Pick a Grammar

**Iso faces.** Isometric objects with dark filled faces (top lightest, sides darker), thin strokes, real names printed small on the parts, a faint light behind the drawing, and a live readout under it. Best for scenes with many distinct objects: a desk computer, a street of services, a stack of panes. Reference: the farm.js `/agents` figures and iso-figures.

**Hairline.** Outlines only: one projection, one stroke weight, faces filled with the page background so solids hide what is behind them, a single dim crease inside each rounded solid, nothing glowing. Whatever matters right now gets the one bright edge. Best for small, quiet figures beside headline copy. Reference: Hairline (after Linear's homepage illustrations).

**Glyph.** Tiny line icons in a fixed viewBox (for example 32x24) with one accent stroke, each part tagged with a motion kind and delay, animated by CSS keyframes on hover or focus. Best for nav menus and lists. Reference: the assistant-ui nav glyphs.

## Rules That Make Them Feel Finished

- One projection and one stroke weight per figure, with `vector-effect: non-scaling-stroke`, round caps and joins.
- Round every corner. Solids are rounded rectangles and discs, not sharp boxes.
- Faces fill with the background colour. Occlusion comes from paint order, never from masks.
- One bright edge at a time. Everything else stays at hairline contrast. Highlights that glare get toned down (about 0.3 alpha on dark for lit parts, 0.9 only for the focus).
- No glow, bokeh, gradients, or squash-and-stretch wobble.
- Words go beside the drawing: a corner hint (what to do, uppercase mono) and a corner readout (what is happening, normal case, tabular numbers), plus labels wired to parts. Inside the drawing, print names only where they sit on the object itself.
- A figure that does not explain itself gets labels: a dot on the part, a wire with rounded elbows drawn out from it, then an end mark and the label. Draw the wire when the part does its thing and retract it at the reset.
- Every motion is a spring or a deliberate timeline. A hover that ends returns to a pose that was clearly drawn on purpose.
- Finish a motion before the next one starts. Never cut a connection or a sweep halfway because the loop moved on.
- Pointing slows or holds the figure and resumes from where it was. It never restarts or jumps.
- If the figure sits beside rotating copy, run it on that copy's clock so the two cannot drift.
- Show real data when the figure is about data: measured times on a dial, real file names on plates. Never invent numbers or claims.

## Workflow

### 1. Study the Reference

Open each inspiration the user names in a browser. Capture it at rest, mid-motion, and under the pointer, and write down its grammar: projection, stroke, fills, what moves, what lights up, where the words sit, how it resets. Take the grammar, not the subject. The subjects and motion should be your own unless the user asks for a recreation.

### 2. Decide What the Figure Says

Write one sentence: "the hand sweeps once while the title names a rival; each framework's mark rises at its measured time." If you cannot write it, the figure is decoration. Pick the subject that carries that sentence: a dial for time, a stack for layers, a belt for a pipeline, a desk for a dev loop.

### 3. Draw the Rest Pose

Lay out the world in units, choose a camera that fits the stage (a lower yaw makes long things run across a wide panel), and frame the viewBox tightly so the drawing fills the stage. Leave room in the viewBox for labels.

### 4. Add Motion, Pointer, Labels

Motion first (springs toward targets the clock sets), then the pointer (map to the drawing's units, keep hit areas fixed), then labels wired to parts. Keep the figure running only while it is on screen.

### 5. Verify

Seek the clock to fixed moments and screenshot a contact sheet; check hover, touch, reduced motion, phone width, console errors, and hydration. When refactoring a shared kit, prove other figures are pixel-identical before and after. Show the user screenshots before proposing a PR.

## Taste Notes From Past Rounds

These came from real review rounds. Treat them as defaults:

- Never restyle one figure differently from its siblings; one system per page.
- Never change motions the user has approved while fixing something else.
- Light behind a drawing stays faint and never over it.
- Hovered things hold their state while hovered ("swap and stay swapped"), and release resumes in place.
- Liked: anoma-style square panels, rounded-elbow connector wires with travelling pulses, numbered markers, typewriter captions, decode-style headings, figures that loop with the copy.
- Disliked: squash/stretch wobble, LED dot-matrix strips, races that look like every other animation on the site, unlabeled drawings that do not describe anything.

## Bundled Resources

- [references/inspirations.md](references/inspirations.md): every site and X post this skill was built from, with what each one contributes.
- [references/build-and-verify.md](references/build-and-verify.md): projection, shapes, painter's order, springs, clocks, pointer mapping, callouts, hydration safety, and the screenshot and recording harness.
