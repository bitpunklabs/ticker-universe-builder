"""HTML is a complete, safe presentation, not a second selection pipeline."""

import copy
import json
import sys
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from build_run import run_build  # noqa: E402
from display_core import display_view  # noqa: E402
from report_html import render_html  # noqa: E402
from test_build_run import coverage_gap_args, resume, start  # noqa: E402
from universe_core import (  # noqa: E402
    apply_change_set,
    load_policy,
    read_json,
    report_languages,
    write_artifacts,
)


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.entries = []
        self.groups = []
        self.links = []
        self.downloads = []
        self.tags = []
        self.language = None
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        data = dict(attrs)
        self.tags.append(tag)
        if tag == "html":
            self.language = data["lang"]
        if "data-ticker" in data:
            self.entries.append((data["data-kind"], data["data-ticker"]))
        if "data-group" in data:
            self.groups.append(data["data-group"])
        if tag == "a":
            self.links.append(data["href"])
            if "download" in data:
                self.downloads.append(data["href"])


def example(name="us-medium"):
    folder = ROOT / "examples" / name / "output"
    universe = next(p for p in folder.glob("*.json") if ".validation." not in p.name)
    return read_json(universe), read_json(universe.with_suffix(".validation.json"))


@pytest.mark.parametrize("name", [
    "us-light", "us-medium", "us-heavy", "us-max", "cn-medium", "crypto-medium",
    "hk-medium", "jp-medium", "kr-medium", "uk-medium",
])
def test_every_language_contains_all_members_references_and_existing_groups(name):
    universe, report = example(name)
    _, grouped = display_view(universe)
    expected = Counter(("member", m["ticker"]) for m in universe["members"])
    expected.update(("reference", r["ticker"])
                    for r in universe["coverage_plan"]["references"])
    for language in report_languages(universe):
        source = render_html(universe, report, language)
        page = Page(source)
        assert page.language == language
        assert Counter(page.entries) == expected
        assert set(page.groups) == set(grouped)
        assert "<script" not in source
        assert "stylesheet" not in source  # All CSS is inline, no network dependency.
        assert all(not link.startswith(("https:", "http:")) for link in page.links)
        for link in page.links:
            assert (ROOT / "examples" / name / "output" / link).is_file()
        assert page.downloads == page.links
    if name == "us-medium":
        # Display groups merge underlying economic duties, matching the TXT/Markdown contract.
        assert len(grouped["10_A"]) == 9
        assert len(grouped["21_B"]) == 8


def test_authored_translations_brief_reasons_and_untrusted_text():
    universe, report = example("cn-medium")
    universe = copy.deepcopy(universe)
    member = universe["members"][0]
    member["name"] = '<script>alert("name")</script>'
    member["reason_summary"] = '主营 <img src=x onerror="alert(1)">。'
    member["reason"] = "LONG_PRIVATE_ADMISSION_REASON"
    universe["notes"].append('<script>alert("notes")</script>')
    universe["notes"].append("AMEX:BTG: no factor statistics, 0 sessions overlap a usable gauge")
    universe["report_translations"]["en"][member["reason_summary"]] = "Authored short reason."
    zh = render_html(universe, report, "zh-Hans")
    en = render_html(universe, report, "en")
    assert 'Authored short reason.' in en
    assert '主营 &lt;img' in zh
    assert 'LONG_PRIVATE_ADMISSION_REASON' not in zh
    assert "no factor statistics" not in zh
    assert "&lt;script&gt;" in zh
    assert "script" not in Page(zh).tags
    assert "img" not in Page(zh).tags


def test_max_marks_only_new_beta():
    universe, report = example("us-max")
    source = render_html(universe, report)
    assert source.count('class="added"') == 111
    assert "370 → 481" in source
    assert "+111 Beta (30.0%)" in source


def test_partial_and_maintenance_are_visible_and_link_to_correct_files(tmp_path):
    result, code = run_build(**coverage_gap_args(tmp_path))
    assert code == 3
    path = Path(result["artifacts"]["html_reports"]["en"])
    source = path.read_text()
    assert "-partial.en.html" in path.name
    assert 'class="verdict partial"' in source
    assert 'PARTIAL:' in source
    assert all("-partial." in link for link in Page(source).links)
    assert str(path) in result["artifact_sha256"]

    base, _ = example()
    changes = dict(schema_version=1, market="us", as_of=base["as_of"], complete=True,
                   base_version_hash=base["version_hash"],
                   base_content_hash=base["content_hash"], review_depth="routine",
                   sources=base["sources"], ops=[dict(op="NO_CHANGE", reason="Format review")])
    updated, report = apply_change_set(base, changes, load_policy())
    artifacts = write_artifacts(updated, report, tmp_path / "maintained")
    assert "This review" in artifacts["html_reports"]["en"].read_text()
    assert updated["members"] == base["members"]


@pytest.mark.parametrize("damage", ["missing", "changed"])
def test_html_is_checked_on_resume_and_repaired_into_a_new_directory(tmp_path, damage):
    result, code = run_build(**start(tmp_path))
    assert code == 0
    path = Path(result["artifacts"]["html_reports"]["en"])
    original = path.read_bytes()
    if damage == "missing":
        path.unlink()
    else:
        path.write_text("changed")
    blocked, code = resume(result)
    assert code == 2
    assert blocked["artifact_problems"] == [{"path": str(path), "reason": damage}]
    assert len(json.loads(Path(result["checkpoint"]).read_text())["attempts"]) == 1
    repaired, code = run_build(spec=None, snapshot=None, output=str(tmp_path / "revision"),
                               resume=str(Path(result["checkpoint"]).parent))
    assert code == 0
    assert Path(repaired["artifacts"]["html_reports"]["en"]).read_bytes() == original
