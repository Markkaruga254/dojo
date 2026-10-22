"""Check repository-relative Markdown links and heading anchors."""
from __future__ import annotations

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK_RE = re.compile(r"!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
REF_RE = re.compile(r"^\s*\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", re.MULTILINE)

def slug(text: str) -> str:
    tick = chr(96)
    text = re.sub(tick + r"([^" + tick + r"]*)" + tick, r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text).lower().strip()
    text = re.sub(r"[^\w\- ]", "", text)
    return re.sub(r"\s+", "-", text)

def files(root: Path) -> list[Path]:
    return sorted(p for p in root.rglob("*.md") if not any(x in {".git", ".venv", "node_modules"} for x in p.parts))

def anchors(path: Path) -> set[str]:
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return set()
    found = set(re.findall(r'\bid=["\']([^"\']+)["\']', text, re.IGNORECASE))
    counts: dict[str, int] = {}
    for heading in HEADING_RE.findall(text):
        base = slug(heading)
        count = counts.get(base, 0)
        counts[base] = count + 1
        found.add(base if count == 0 else f"{base}-{count}")
    return found

def check_links(root: Path) -> list[str]:
    root = root.resolve()
    errors: list[str] = []
    for source in files(root):
        try:
            text = source.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError) as exc:
            errors.append(f"{source.relative_to(root)}: cannot read Markdown ({exc})")
            continue
        links = [m.group(1) or m.group(2) for m in LINK_RE.finditer(text)] + REF_RE.findall(text)
        for raw in links:
            raw = raw.strip()
            if not raw:
                continue
            if raw.startswith("#"):
                target, fragment = source, unquote(raw[1:])
                if not fragment:
                    continue
            else:
                parsed = urlsplit(raw)
                if parsed.scheme or parsed.netloc:
                    continue
                target_text, fragment = unquote(parsed.path), unquote(parsed.fragment)
                target = (source.parent / target_text).resolve() if target_text else source
            try:
                target.relative_to(root)
            except ValueError:
                errors.append(f"{source.relative_to(root)}: link escapes repository: {raw}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(root)}: missing target: {raw}")
            elif fragment and target.is_file() and target.suffix.lower() in {".md", ".markdown"} and fragment not in anchors(target):
                errors.append(f"{source.relative_to(root)}: missing anchor: {raw}")
    return errors

def main() -> int:
    errors = check_links(ROOT)
    if errors:
        print(f"Markdown link check failed: {len(errors)} issue(s)")
        for error in errors:
            print(f"::error::{error}")
        return 1
    print(f"Markdown link check passed ({len(files(ROOT))} files scanned).")
    return 0

if __name__ == "__main__":
    sys.exit(main())
