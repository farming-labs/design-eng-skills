# Build and Verify

How the figures in this skill are built, and how to check them before anyone else sees them. Everything here is plain SVG, a little math, and React state; no figure library.

## Projection

Draw in world units and project through a camera: yaw turns the world about the vertical axis, pitch tilts it toward the viewer, then scale and shift place it in the viewBox.

```ts
type Camera = { yaw: number; pitch: number; scale: number; shift: [number, number] };
const UNIT = 30;

function lens({ yaw, pitch, scale, shift: [dx, dy] }: Camera) {
  const [cy, sy, cp, sp] = [Math.cos(yaw), Math.sin(yaw), Math.cos(pitch), Math.sin(pitch)].map(snap);
  const k = scale * UNIT;
  return {
    at: (x: number, y: number, z: number): [number, number] => [
      (x * cy - y * sy) * k + dx,
      ((x * sy + y * cy) * sp - z * cp) * k + dy,
    ],
    depth: (x: number, y: number) => x * sy + y * cy, // nearer the viewer is larger
    flat: [k, k * sp], // a ground circle's radii on screen
  };
}
```

- Yaw 45° and pitch asin(√(1/3)) is true isometric. Pitch 30° reads a little flatter, as in the hairline figures.
- A lower yaw (about 0.4 rad) runs long objects across a wide panel. Yaw 0 with a small pitch gives a face-on view for things that must read level, like a balance beam.
- A ground circle projects to an axis-aligned ellipse with radii `flat`, so discs and dials are an `<ellipse>` for the top and a path for the side band.

## Hydration Safety

Server and browser can disagree in the last bit of a sine, which flips a rounded coordinate and breaks hydration. Snap trigonometry to a fixed precision, print coordinates with a fixed number of decimals, and never print `-0`:

```ts
const snap = (v: number) => Math.round(v * 1e9) / 1e9;
const fixed = (v: number) => (Math.abs(v) < 0.005 ? 0 : v).toFixed(2);
```

Render a deterministic rest pose on the server and on the first client render. Start any motion from an effect after hydration.

## Shapes and Paint Order

- Rounded rectangles: build the outline from four quarter arcs (five steps each is enough), project the top at `z1`, and draw the side band as the near arc between the outline's leftmost and rightmost screen points, at `z1` and back down at `z0`.
- Faces fill with the background colour, so occlusion is just paint order: draw far things first (sort by `depth`), lower things before the things stacked on them.
- Stacked solids make their own creases: a column built from one block per second shows a hairline at every second without drawing any extra lines.
- Text on a surface: `matrix(a b c d x y)` from the projected x axis and the projected y axis (top) or the down axis (front). Fade top-printed text as the camera levels off.
- One stroke weight with `vector-effect: non-scaling-stroke`, so lines stay crisp at any size.

## Motion

Use springs for anything the pointer or the story moves. Cap the step so a background tab does not explode the simulation:

```ts
type Spring = { x: number; v: number };
function pull(s: Spring, to: number, dt: number, stiffness = 170, damping = 22) {
  s.v += (stiffness * (to - s.x) - damping * s.v) * dt;
  s.x += s.v * dt;
}
// dt = Math.min(1 / 30, (now - last) / 1000)
```

- Critical damping is `2 * sqrt(stiffness)`. Go slightly under it for a settle with life, and at or over it for smooth, calm motion (users asked for this on the benchmark figures).
- Springs only creep up on their target. Anything that waits for "done" (a label appearing, a wire counted as drawn) should trigger a little early, for example at 60 to 90 percent.
- Ease the clock that drives a sweep (`t * t * (3 - 2 * t)`) so it starts and stops softly.
- Run the frame loop only while the figure is on screen (an `IntersectionObserver` gates `requestAnimationFrame`) and stop it when everything has settled.
- Under `prefers-reduced-motion`, draw one still, finished pose and stop. Do not just slow things down.

## Running on Someone Else's Clock

When a figure sits beside copy that animates on its own (a rotating "9.21× faster than Nuxt." title), drive the figure from that animation's clock instead of a second timer:

```ts
const animation = titleItem.getAnimations()[0];
const { duration, delay } = animation.effect!.getTiming();
const into = (Number(animation.currentTime) - Number(delay)) % Number(duration);
```

The two can never drift, even after the figure was off screen, and pausing the CSS animation in a test pauses the figure too.

## Pointer

- Map client coordinates into the drawing with `svg.getScreenCTM().inverse()`.
- To find where on a plane the pointer is, invert the projection for that plane (ground or a known height).
- Pick by fixed hit bands (a part's rest position), not by the shape's current outline, so a part that lifts or grows cannot slide out from under the pointer and drop the hover.
- On touch, `pointerleave` fires as the finger lifts. Keep what was tapped instead of clearing it.
- Pointing holds or slows the figure and resumes from the same place when the pointer leaves.

## Labels and Wires

A callout has three parts: a dot on the part, a wire with rounded elbows, and an end mark with the label.

- Build the route in screen units: start at the part, turn once toward a label column outside the drawing, end at the label.
- Draw the wire progressively by tracing a fraction of the route's length, so it can draw in, retract, and follow a moving part.
- Fade the end mark and label in only once the wire has landed.
- Keep labels in columns on the sides of the drawing, sorted by height, with a minimum gap so they never overlap.
- For a wire between HTML and SVG (a list row to a drawing beside it), measure both ends with `getBoundingClientRect` in a layout effect, end the wire exactly on the target's edge, and re-measure on resize. Only set state when a measured value changes, or the measurement will loop renders.

## Corners and Readouts

Put a hint in one corner (what to do: "POINT AT THE DIAL", uppercase mono) and a readout in the other (what is happening: "t 1.24s", "Farm.js 253ms · Nuxt 2.33s", normal case, tabular numbers). Give the readout a fixed height so the page never jumps when its text changes length.

## Sharing a Kit Between Pages

Keep the primitives (camera, shapes, text, callouts, clock) in a module without a `"use client"` directive, imported by each page's figure module, so one page does not ship another page's figures. Scope the drawing styles to a class such as `.iso-scene` and keep the selectors' specificity unchanged when moving them, or older figures will change.

## Verify

1. **Freeze the clock.** Pause the driving CSS animation and seek `currentTime`, or tick a fake clock, then screenshot the same moments every time. Lay the shots out on a contact sheet: before start, mid-motion, finished, reset.
2. **Prove refactors are invisible.** Capture the other figures under `reducedMotion: "reduce"` before and after a shared change and compare bytes (`cmp`). Identical files, not "looks the same".
3. **Exercise the pointer.** Move a real mouse over each part and check the highlight and readout; check a touch tap keeps its selection.
4. **Check the edges.** Reduced motion, a phone width (no horizontal overflow), console errors, hydration warnings, and the figure pausing off screen.
5. **Record when motion is the point.** Drive the page with a deterministic clock and pipe frames into ffmpeg (two-pass x264) when a video has to stay under a size limit, rather than screen-recording in real time.
6. **Show it first.** Send screenshots (or a short recording) before proposing a PR; figure work is judged by eye.
