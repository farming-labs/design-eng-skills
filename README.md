# Design Engineering Skills

[![skills.sh](https://skills.sh/b/farming-labs/design-eng-skills)](https://skills.sh/farming-labs/design-eng-skills)

Reusable design-engineering skills for Codex. The first skill helps design, build, and refine apps, websites, docs, dashboards, studio tools, component libraries, and design systems.

## Install

From the future GitHub repo:

```bash
npx skills add farming-labs/design-eng-skills --skill design-engineer
```

Install the SVG figures skill:

```bash
npx skills add farming-labs/design-eng-skills --skill svg-figures
```

Codex-targeted install:

```bash
npx skills add farming-labs/design-eng-skills --skill design-engineer --agent codex --yes
```

Full GitHub URL form:

```bash
npx skills add https://github.com/farming-labs/design-eng-skills --skill design-engineer
```

Or install directly in Codex with:

```text
$skill-installer install https://github.com/farming-labs/design-eng-skills/tree/main/design-engineer
```

For local testing:

```bash
mkdir -p ~/.codex/skills
cp -R design-engineer ~/.codex/skills/design-engineer
```

Restart Codex after installing so the skill is discovered.

## Skills

- `svg-figures`: Design and build animated SVG figures: isometric and hairline drawings, pointer-reactive illustrations, labelled diagrams with drawn wires, nav glyphs, and figures synced to the copy beside them. Includes every inspiration it was built from ([inspirations](svg-figures/references/inspirations.md)) and the build and verification patterns ([build and verify](svg-figures/references/build-and-verify.md)).
- `design-engineer`: Design and build polished frontend experiences for React, Next.js, Vite, docs sites, dashboards, studio apps, product websites, component libraries, and design systems. Covers visual language, primitive/component APIs, design-engineering tool selection, interactions, motion, icons, loading states, and browser-based visual QA.

The [UI component guide](design-engineer/references/ui-components.md) includes 21 curated sources from [Designeer](https://www.designeer.xyz/components) and complementary libraries, with guidance for choosing and adapting forms, navigation, uploads, tables, charts, boards, motion, marketing blocks, and chat components.

The [design craft reference](design-engineer/references/design-craft.md) adds Jakub Krehel's `better-ui`, Emil Kowalski's `emil-design-eng`, and the Sales CRM demo, with attributed polish guidance and practical patterns for dense business apps.
