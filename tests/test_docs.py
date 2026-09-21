from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Everything a reader is pointed at. `temp/` is scratch and `.venv/` is not ours.
SKIPPED = {".git", ".venv", ".pytest_cache", ".ruff_cache", "temp", "__pycache__"}

LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
HEADING = re.compile(r"^#{1,6}\s+(.*?)\s*#*$", re.MULTILINE)
FENCE = re.compile(r"^```.*?^```", re.MULTILINE | re.DOTALL)
COMMENT = re.compile(r"<!--.*?-->", re.DOTALL)


def live_text(path: Path) -> str:
    """The prose a reader actually follows: no fenced samples, no commented-out slots."""
    return COMMENT.sub("", FENCE.sub("", path.read_text(encoding="utf-8")))


def markdown_files() -> list[Path]:
    found = []
    for path in sorted(ROOT.rglob("*.md")):
        if SKIPPED & set(path.relative_to(ROOT).parts):
            continue
        found.append(path)
    return found


def slug(heading: str) -> str:
    """GitHub's anchor rule, near enough for headings we write ourselves."""
    text = re.sub(r"[^\w\s-]", "", heading.lower())
    return re.sub(r"\s+", "-", text.strip())


class DocumentationLinkTests(unittest.TestCase):
    """A link that has rotted is a documentation bug that nothing else catches.

    The README, SKILL.md and AGENTS.md exist to route someone — a human or an agent — to a
    file. A rename that leaves the pointer behind turns the routing into a dead end, silently,
    and the only reader who finds out is the one who needed it.
    """

    def test_every_relative_link_resolves(self) -> None:
        for path in markdown_files():
            body = live_text(path)
            for target in LINK.findall(body):
                if target.startswith(("http://", "https://", "mailto:", "#")):
                    continue
                with self.subTest(file=str(path.relative_to(ROOT)), link=target):
                    resolved = (path.parent / target.split("#", 1)[0]).resolve()
                    self.assertTrue(resolved.exists(), f"{target} does not exist")

    def test_every_same_file_anchor_names_a_heading(self) -> None:
        for path in markdown_files():
            body = live_text(path)
            anchors = {slug(heading) for heading in HEADING.findall(body)}
            for target in LINK.findall(body):
                if not target.startswith("#"):
                    continue
                with self.subTest(file=str(path.relative_to(ROOT)), anchor=target):
                    self.assertIn(target[1:], anchors)


class ReadmeMediaTests(unittest.TestCase):
    """Two image slots, commented out until the files exist.

    A placeholder that renders as a broken image is worse than no image at all, so the tags live
    inside HTML comments and the capture instructions live beside the directory they write into.
    Either half going missing leaves someone holding an instruction for a slot that is not there,
    or a slot nobody knows how to fill.
    """

    def test_each_placeholder_has_capture_instructions(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        instructions = (ROOT / "docs" / "media" / "README.md").read_text(encoding="utf-8")
        slots = re.findall(r"docs/media/([\w.-]+\.(?:gif|png|jpg|svg))", readme)
        self.assertEqual(sorted(set(slots)), ["demo.gif", "watchlist-import.gif"])
        for slot in set(slots):
            with self.subTest(slot=slot):
                self.assertIn(slot, instructions)

    def test_a_missing_asset_is_commented_out_rather_than_broken(self) -> None:
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        commented = "".join(re.findall(r"<!--.*?-->", readme, re.DOTALL))
        for slot in re.findall(r"docs/media/([\w.-]+\.(?:gif|png|jpg|svg))", readme):
            if (ROOT / "docs" / "media" / slot).exists():
                continue
            with self.subTest(slot=slot):
                self.assertIn(f"]({Path('docs/media') / slot})", commented)


if __name__ == "__main__":
    unittest.main()
