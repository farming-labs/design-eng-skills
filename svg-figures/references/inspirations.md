# Inspirations

Every source below was shared while building the farm.js and assistant-ui figures, launch video, and blog figures. Open the source itself before borrowing from it; this file records what each one is good for, not a copy of it. Take the grammar, not the subject, unless the user asks for a recreation.

## Isometric and Hairline Figures

| Source | What it is | What to take |
| --- | --- | --- |
| [iso-figures.vercel.app](https://iso-figures.vercel.app) | ISO FIGURES by April Zhu ([april-zhu.com](https://april-zhu.com)), crediting [@wheresryan22](https://x.com/wheresryan22) and [@0xbigturk](https://x.com/0xbigturk). Ten interactive isometric objects: desk computer, drum machine, typewriter, server rack, system stack, kitchen timer, cassette deck, desk lamp, logic board, vending machine. | Objects you can operate (type on the computer, play the pads, insert cartridges). Each figure has a "Fig N" label, its name, a corner hint ("TYPE ON IT · CLICK IT TO SWITCH") and a live readout ("on · 0 chars"). The system stack wires labelled cartridges into layers; the logic board runs a signal along traces. One accent colour. |
| [lucasmarkes.com/lab/hairline](https://www.lucasmarkes.com/lab/hairline) | "Hairline" by Lucas Marques: six figures drawn after Linear's homepage hover illustrations (Riffle, Terrain, Exploded, Phosphor, Slow, Turntable). Shared as `hairlines.lucasmarkes.com`, which returns 404; the page lives on his lab. | The hairline grammar: one projection, one stroke weight, rounded solids with a single dim crease inside a brighter outline, no words inside the figure. Springs instead of timed eases, fixed hit bands so a lifting part cannot drop the hover, one shared frame loop that stops when everything settles, slowing time instead of pausing it, a camera that springs back to the angle it was drawn for. |
| [linear.app](https://linear.app) | The homepage row of small isometric drawings that move when pointed at. | The original of the hairline grammar: nothing filled or glowing, a plate lifts, an edge turns bright, and the drawing returns to a deliberate pose. |
| [x.com/benchodev/status/2106728542214263055](https://x.com/benchodev/status/2106728542214263055) | Bencho sharing "isometric wireframes" by @wheresryan22, found on [bencho.dev](https://bencho.dev). | The isometric wireframe look the farm.js `/agents` figures started from: thin strokes on dark faces, objects that carry their names, scenes that play on their own. |
| [x.com/wheresryan22/status/2106476722463900105](https://x.com/wheresryan22/status/2106476722463900105) | @wheresryan22 generating an isometric SVG with an `/isometric-objects` skill: an old all-in-one computer like the first Apple PC, a logo on the screen, and a keyboard with a cable. | The prompt shape for object figures, and the farm.js `/agents` "farm dev" computer: keys pressing as the command types, a pulse running down the keyboard cable, the screen booting to the logo. |
| [codedvisuals.com/visuals/automations/workflow-builder](https://codedvisuals.com/visuals/automations/workflow-builder) | Coded Visuals' animated workflow-builder visual. | Node-and-wire illustrations for agent and automation pages, kept in the page's own design system. |

## Motion, Video, and Editorial Effects

| Source | What it is | What to take |
| --- | --- | --- |
| [anoma.ly/notes/opencode-reloaded](https://anoma.ly/notes/opencode-reloaded/) | Anomaly's "opencode reloaded" note. | Square animated panels inside a long-form post, headings that decode through look-alike glyphs, video moments placed between sections. Used for the farm.js 0.1.0 blog figures. |
| [x.com/sxmawl/status/2104996131419856928](https://x.com/sxmawl/status/2104996131419856928) | Saksham's launch video for Cardboard, a video editor. | Launch-video pacing and product-UI motion. One of the two references for the farm.js 0.1.0 launch video. |
| [x.com/nizzyabi/status/2104587269621612997](https://x.com/nizzyabi/status/2104587269621612997) | Nizzy's launch video for Keiki for agencies. | Product launch storytelling with real UI. The second reference for the farm.js 0.1.0 launch video. |
| [x.com/evilrabbit_/status/2105062376575992090](https://x.com/evilrabbit_/status/2105062376575992090) | Evil Rabbit announcing Vercel's Creative Studio. | Creative direction for brand films; the reference for an assistant-ui video and for the farm.js launch video's restraint. |
| [21st.dev/community/ascii](https://21st.dev/community/ascii) | Community ASCII art components. | ASCII textures and lattices, used for the launch video and the `/agents` hero lattice. Keep them at low opacity behind content. |

## Components and Loaders

| Source | What it is | What to take |
| --- | --- | --- |
| [designeer.xyz](https://www.designeer.xyz/) | A directory of UI libraries, registries, blocks, and motion components. | Component and motion sources to adapt into the local design system. The `design-engineer` skill's UI component guide covers it in depth. |
| [loading.dev](http://loading.dev/) | Loading and progress animation patterns. | Loaders and pending states that match a figure's line language. |

## Exemplars Built From These

Read these before building something similar; they are the working versions of the rules in this skill.

- farm.js `/agents` figures: [docs/src/components/agents/iso-figures.tsx](https://github.com/farming-labs/farm.js/blob/main/docs/src/components/agents/iso-figures.tsx), iso faces, a moving camera, per-layer callouts, keyboard and cable animation, hover that holds and resumes.
- farm.js landing hero drag and wire: [docs/src/components/home/selection-wire.tsx](https://github.com/farming-labs/farm.js/blob/main/docs/src/components/home/selection-wire.tsx), a selection box dragged over a word, then a rounded-elbow wire into the call to action.
- farm.js blog figures: [docs/src/components/blog](https://github.com/farming-labs/farm.js/tree/main/docs/src/components/blog), anoma-style panels with pulses on wires.
- assistant-ui nav glyphs: [apps/docs/components/shared/nav-glyph.tsx](https://github.com/assistant-ui/assistant-ui/blob/main/apps/docs/components/shared/nav-glyph.tsx), 21 thin-stroke glyphs with per-part motion kinds and a showcase that swaps windows and stays swapped while hovered.
- farm.js benchmark figures (on a branch, not on main yet), hairline and synced to each panel's rotating title: a stopwatch whose marks rise to their first-page times, a column race for build time, a server rack for production boot, and a balance for HTML size, all with wired labels (`docs/src/components/home/benchmark-figures.tsx`, shared kit in `docs/src/components/iso/scene.tsx`).
- farm.js routing card (same branch): a wire from the selected file in the app tree to a hairline browser that shows what the file becomes (`docs/src/components/home/route-explorer.tsx`).
