#!/usr/bin/env python3
"""Validate repository-wide Markdown links and ratchet Markdown formatting."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKIP_DIRS = {".git", ".venv", "venv", "node_modules"}
FENCE_RE = re.compile(r"^\s*(`{3,}|~{3,})")
INLINE_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)\n]+)\)")
REFERENCE_LINK_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)")
MATH_TOKEN_RE = re.compile(r"\\\[|\\\]|\\\(|\\\)")
LATEX_HINT_RE = re.compile(
    r"\\(?:boxed|text|rightarrow|longrightarrow|Longrightarrow|not\\?Rightarrow|"
    r"mathcal|mathrm|Delta|Sigma|Pi|Gamma|Lambda|left|right|begin|end)"
)


def markdown_files() -> list[Path]:
    return sorted(
        path
        for path in ROOT.rglob("*.md")
        if not any(part in SKIP_DIRS for part in path.relative_to(ROOT).parts)
    )


def visible_lines(text: str) -> list[tuple[int, str]]:
    """Return non-code-fence lines while preserving source line numbers."""
    output: list[tuple[int, str]] = []
    fence: str | None = None
    for number, line in enumerate(text.splitlines(), start=1):
        match = FENCE_RE.match(line)
        if match:
            marker = match.group(1)[0]
            if fence is None:
                fence = marker
            elif marker == fence:
                fence = None
            continue
        if fence is None:
            output.append((number, line))
    return output


def normalize_target(raw: str) -> str:
    raw = raw.strip()
    if raw.startswith("<") and ">" in raw:
        return raw[1 : raw.index(">")].strip()
    return raw.split(maxsplit=1)[0].strip("\"'")


def validate_link(source: Path, line: int, raw_target: str, errors: list[str]) -> None:
    target = normalize_target(raw_target)
    if not target or target.startswith("#"):
        return

    parsed = urlsplit(target)
    if parsed.scheme or parsed.netloc or target.startswith(("mailto:", "tel:")):
        return

    path_text = unquote(parsed.path)
    if not path_text or path_text.startswith("/"):
        return

    candidate = (source.parent / path_text).resolve()
    try:
        candidate.relative_to(ROOT.resolve())
    except ValueError:
        errors.append(f"{source.relative_to(ROOT)}:{line}: link escapes repository: {target}")
        return

    if candidate.is_dir():
        candidate = candidate / "README.md"

    if not candidate.exists():
        errors.append(
            f"{source.relative_to(ROOT)}:{line}: missing local link target: {target}"
        )


def validate_links(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    for line_number, line in visible_lines(text):
        for match in INLINE_LINK_RE.finditer(line):
            validate_link(path, line_number, match.group(1), errors)
        reference = REFERENCE_LINK_RE.match(line)
        if reference:
            validate_link(path, line_number, reference.group(1), errors)
    return errors


def validate_formatting(path: Path) -> list[str]:
    errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(ROOT)

    if text and not text.endswith("\n"):
        errors.append(f"{rel}: file must end with a newline")

    fence: str | None = None
    display_open = False
    inline_open = False
    visible = visible_lines(text)

    for line_number, line in visible:
        stripped = line.strip()

        if stripped in {"[", "]"}:
            nearby = "\n".join(
                candidate
                for number, candidate in visible
                if abs(number - line_number) <= 3
            )
            if LATEX_HINT_RE.search(nearby):
                errors.append(
                    f"{rel}:{line_number}: literal bracket appears to be a malformed math delimiter"
                )

        for token in MATH_TOKEN_RE.findall(line):
            if token == r"\[":
                if display_open:
                    errors.append(f"{rel}:{line_number}: nested display-math opener")
                display_open = True
            elif token == r"\]":
                if not display_open:
                    errors.append(f"{rel}:{line_number}: display-math closer without opener")
                display_open = False
            elif token == r"\(":
                if inline_open:
                    errors.append(f"{rel}:{line_number}: nested inline-math opener")
                inline_open = True
            elif token == r"\)":
                if not inline_open:
                    errors.append(f"{rel}:{line_number}: inline-math closer without opener")
                inline_open = False

        if display_open and re.fullmatch(r"\s*={3,}\s*", line):
            errors.append(
                f"{rel}:{line_number}: equals-sign rule inside display math; use an equation operator"
            )

    for line in text.splitlines():
        match = FENCE_RE.match(line)
        if not match:
            continue
        marker = match.group(1)[0]
        if fence is None:
            fence = marker
        elif marker == fence:
            fence = None

    if fence is not None:
        errors.append(f"{rel}: unclosed fenced code block")
    if display_open:
        errors.append(f"{rel}: unclosed display-math block")
    if inline_open:
        errors.append(f"{rel}: unclosed inline-math block")

    return errors


def format_paths(args: argparse.Namespace, all_files: list[Path]) -> list[Path]:
    if args.all_formatting:
        return all_files
    if args.format_paths_file is None:
        return all_files

    selected: list[Path] = []
    for raw in args.format_paths_file.read_text(encoding="utf-8").splitlines():
        raw = raw.strip()
        if not raw or not raw.endswith(".md"):
            continue
        candidate = (ROOT / raw).resolve()
        try:
            candidate.relative_to(ROOT.resolve())
        except ValueError:
            raise ValueError(f"format path escapes repository: {raw}") from None
        if candidate.exists():
            selected.append(candidate)
    return sorted(set(selected))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--format-paths-file",
        type=Path,
        help="newline-delimited repository paths whose formatting must be validated",
    )
    parser.add_argument(
        "--all-formatting",
        action="store_true",
        help="validate formatting for every Markdown file, including historical debt",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    files = markdown_files()
    selected = format_paths(args, files)

    errors: list[str] = []
    for path in files:
        errors.extend(validate_links(path))
    for path in selected:
        errors.extend(validate_formatting(path))

    if errors:
        print("Markdown validation failed:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        return 1

    print(
        f"Validated local links in {len(files)} Markdown files "
        f"and formatting in {len(selected)} Markdown files."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
