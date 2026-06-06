#!/usr/bin/env python3
"""Scan a frontend project for design-engineering signals."""

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any

EXCLUDE_DIRS = {
    ".git",
    ".next",
    ".nuxt",
    ".output",
    ".svelte-kit",
    "build",
    "coverage",
    "dist",
    "node_modules",
    "out",
    "target",
}

UI_EXTENSIONS = {
    ".astro",
    ".css",
    ".html",
    ".js",
    ".jsx",
    ".mdx",
    ".scss",
    ".svelte",
    ".ts",
    ".tsx",
    ".vue",
}

STACK_DEPS = {
    "next": "Next.js",
    "vite": "Vite",
    "react": "React",
    "tailwindcss": "Tailwind CSS",
    "@tailwindcss/postcss": "Tailwind CSS v4",
    "fumadocs-ui": "Fumadocs",
    "@farming-labs/docs": "Docs runtime",
    "@farming-labs/theme": "Theme package",
    "@radix-ui/react-dialog": "Radix UI",
    "@radix-ui/react-popover": "Radix UI",
    "class-variance-authority": "CVA",
    "lucide-react": "lucide-react",
    "@iconify/react": "Iconify",
    "@iconify-icon/react": "Iconify",
    "iconify-icon": "Iconify",
    "cmdk": "cmdk",
    "sonner": "sonner",
    "framer-motion": "Framer Motion",
    "motion": "Motion",
    "gsap": "GSAP",
    "three": "Three.js",
    "@react-three/fiber": "React Three Fiber",
    "recharts": "Recharts",
    "@xyflow/react": "XYFlow",
}

SIGNAL_PATTERNS = {
    "className": re.compile(r"className="),
    "tailwind_classes": re.compile(r"\b(?:flex|grid|relative|absolute|border|bg-|text-|px-|py-|gap-|rounded|shadow|transition|animate)-?"),
    "keyframes": re.compile(r"@keyframes\b"),
    "transitions": re.compile(r"\btransition(?:-|:|\b)|duration-\d+|ease-"),
    "animations": re.compile(r"\banimate-|animation:|motion\.|framer-motion|gsap|useFrame|Canvas\b"),
    "reduced_motion": re.compile(r"prefers-reduced-motion|motion-reduce"),
    "view_transitions": re.compile(r"view-transition|::view-transition"),
    "icons": re.compile(r"lucide-react|@iconify|iconify-icon|simple-icons|<svg\b|Icon[A-Z]"),
    "loaders": re.compile(r"loading|spinner|skeleton|pending|progress|animate-spin", re.IGNORECASE),
    "states": re.compile(r"empty|error|success|disabled|selected|active|hover:|focus-visible|aria-", re.IGNORECASE),
    "risk_orbs": re.compile(r"\borb\b|\bblob\b|bokeh|blur-\[|blur-3xl|radial-gradient|conic-gradient", re.IGNORECASE),
    "cards": re.compile(r"\bcard\b|Card\b|rounded-|shadow-|border\b"),
}

INTERACTION_PATTERNS = {
    "navigation_shell": re.compile(r"\b(nav|sidebar|layout|breadcrumb|tabs|route|Link|NavLink)\b", re.IGNORECASE),
    "command_search": re.compile(r"\b(cmdk|command palette|CommandPalette|search|combobox)\b", re.IGNORECASE),
    "copy_affordance": re.compile(r"\b(clipboard|copy|copied|CopyIcon|Copy[A-Z])\b", re.IGNORECASE),
    "forms_filters": re.compile(r"\b(form|input|select|checkbox|radio|switch|filter|date range|DatePicker|Calendar)\b", re.IGNORECASE),
    "tables_lists": re.compile(r"\b(table|thead|tbody|tr|row|pagination|list|virtual)\b", re.IGNORECASE),
    "dialogs_popovers": re.compile(r"\b(dialog|modal|popover|drawer|sheet|tooltip|dropdown|toast|sonner)\b", re.IGNORECASE),
    "charts_data": re.compile(r"\b(recharts|chart|axis|tooltip|legend|bar|line|area|pie|map)\b", re.IGNORECASE),
    "live_status": re.compile(r"\b(status|watch|refresh|sync|stale|connected|reconnect|heartbeat|live)\b", re.IGNORECASE),
    "empty_error_success": re.compile(r"\b(empty|error|failed|denied|unauthorized|success|saved|retry)\b", re.IGNORECASE),
    "keyboard_access": re.compile(r"\b(keydown|shortcut|aria-|role=|tabIndex|focus-visible|Escape|Enter)\b", re.IGNORECASE),
}

HEX_RE = re.compile(r"#[0-9a-fA-F]{3,8}\b")
RADIUS_RE = re.compile(r"\brounded(?:-(?:none|sm|md|lg|xl|2xl|3xl|full|\[[^\]]+\]))?\b")


def iter_files(root: Path, max_files: int) -> list[Path]:
    files: list[Path] = []
    for path in root.rglob("*"):
        if len(files) >= max_files:
            break
        if any(part in EXCLUDE_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix in UI_EXTENSIONS:
            files.append(path)
    return files


def read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")
    except OSError:
        return ""


def read_package(root: Path) -> tuple[dict[str, str], dict[str, str]]:
    package_path = root / "package.json"
    if not package_path.exists():
        return {}, {}

    try:
        data = json.loads(package_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError):
        return {}, {}

    deps = data.get("dependencies") or {}
    dev_deps = data.get("devDependencies") or {}
    scripts = data.get("scripts") or {}
    return {**deps, **dev_deps}, scripts


def score_file(text: str) -> int:
    score = 0
    for pattern in SIGNAL_PATTERNS.values():
        score += len(pattern.findall(text))
    return score


def analyze(root: Path, max_files: int) -> dict[str, Any]:
    root = root.resolve()
    deps, scripts = read_package(root)
    files = iter_files(root, max_files)

    signal_counts = Counter()
    interaction_counts = Counter()
    colors = Counter()
    radii = Counter()
    top_files: list[tuple[int, Path]] = []
    risk_files: set[str] = set()
    motion_files: set[str] = set()
    icon_files: set[str] = set()

    for file_path in files:
        text = read_text(file_path)
        if not text:
            continue

        for name, pattern in SIGNAL_PATTERNS.items():
            matches = pattern.findall(text)
            signal_counts[name] += len(matches)

        for name, pattern in INTERACTION_PATTERNS.items():
            matches = pattern.findall(text)
            interaction_counts[name] += len(matches)

        colors.update(HEX_RE.findall(text))
        radii.update(RADIUS_RE.findall(text))

        score = score_file(text)
        if score:
            top_files.append((score, file_path))
        if SIGNAL_PATTERNS["risk_orbs"].search(text):
            risk_files.add(str(file_path.relative_to(root)))
        if SIGNAL_PATTERNS["animations"].search(text) or SIGNAL_PATTERNS["keyframes"].search(text):
            motion_files.add(str(file_path.relative_to(root)))
        if SIGNAL_PATTERNS["icons"].search(text):
            icon_files.add(str(file_path.relative_to(root)))

    detected_stack = sorted({label for dep, label in STACK_DEPS.items() if dep in deps})
    top_files.sort(reverse=True, key=lambda item: item[0])

    return {
        "root": str(root),
        "files_scanned": len(files),
        "detected_stack": detected_stack,
        "scripts": {key: scripts[key] for key in sorted(scripts) if key in {"dev", "build", "test", "lint", "typecheck", "check"}},
        "signals": dict(signal_counts.most_common()),
        "interactions": dict(interaction_counts.most_common()),
        "colors": colors.most_common(12),
        "radii": radii.most_common(12),
        "top_ui_files": [
            {"score": score, "path": str(path.relative_to(root))}
            for score, path in top_files[:12]
        ],
        "motion_files": sorted(motion_files)[:12],
        "icon_files": sorted(icon_files)[:12],
        "visual_risk_files": sorted(risk_files)[:12],
    }


def print_report(report: dict[str, Any]) -> None:
    print(f"Design audit: {report['root']}")
    print(f"Files scanned: {report['files_scanned']}")

    stack = ", ".join(report["detected_stack"]) or "No known frontend stack detected from package.json"
    print(f"Stack: {stack}")

    if report["scripts"]:
        print("\nUseful scripts:")
        for name, command in report["scripts"].items():
            print(f"  {name}: {command}")

    print("\nSignals:")
    for name, count in report["signals"].items():
        print(f"  {name}: {count}")

    if report["interactions"]:
        print("\nInteraction surfaces:")
        for name, count in report["interactions"].items():
            print(f"  {name}: {count}")

    if report["radii"]:
        print("\nRadius usage:")
        for value, count in report["radii"]:
            print(f"  {value}: {count}")

    if report["colors"]:
        print("\nCommon raw colors:")
        for value, count in report["colors"]:
            print(f"  {value}: {count}")

    if report["top_ui_files"]:
        print("\nStart by reading:")
        for item in report["top_ui_files"][:8]:
            print(f"  {item['path']} (score {item['score']})")

    if report["motion_files"]:
        print("\nMotion-heavy files:")
        for path in report["motion_files"][:6]:
            print(f"  {path}")

    if report["icon_files"]:
        print("\nIcon-heavy files:")
        for path in report["icon_files"][:6]:
            print(f"  {path}")

    if report["visual_risk_files"]:
        print("\nCheck these for noisy gradients/orbs/blurs before adding more:")
        for path in report["visual_risk_files"][:6]:
            print(f"  {path}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Scan a frontend project for UI design signals.")
    parser.add_argument("path", nargs="?", default=".", help="Project/app/package directory to scan.")
    parser.add_argument("--max-files", type=int, default=2500, help="Maximum UI files to scan.")
    parser.add_argument("--json", action="store_true", help="Print JSON instead of a text report.")
    args = parser.parse_args()

    root = Path(args.path)
    report = analyze(root, args.max_files)

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print_report(report)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
