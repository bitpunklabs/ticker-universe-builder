"""Readable reports must not lose the authoritative research/audit record."""

import re
from copy import deepcopy
from pathlib import Path

import pytest
from test_coverage_core import build, researched
from universe_core import UniverseError, _brief_reason, render_markdown, render_txt


def test_brief_report_keeps_full_reason_evidence_and_diagnostics_in_json():
    data = researched()
    original = data['candidates'][0]
    original['reason'] = ('Observe differentiated banking services. '
                          + 'Detailed audit evidence. ' * 20)
    original['reason_summary'] = 'Observe deposit funding and differentiated lending services.'
    diagnostic = 'NYSE:CORE0: no factor statistics, 0 sessions overlap a usable gauge'
    data['notes'] = [diagnostic, 'Venue identity needs a disclosed namespace limitation.']
    universe, report = build(data)
    report['warnings'].append('Material limitation: reference source requires review.')
    before = deepcopy(universe)
    text = render_markdown(universe, report)
    row = next(line for line in text.splitlines() if line.startswith('| NYSE:CORE0 |'))
    assert original['reason_summary'] in row
    assert 'Detailed audit evidence' not in row and 'https://' not in row
    assert row.count('|') == 5
    assert diagnostic not in text and diagnostic in universe['notes']
    assert 'Venue identity needs a disclosed namespace limitation.' in text
    assert 'Material limitation: reference source requires review.' in text
    assert universe == before
    member = next(c for c in universe['members'] if c['ticker'] == original['ticker'])
    assert member['reason'] == original['reason'].strip()
    assert member['evidence'] == original['evidence']
    assert '.validation.json)' in text and '.json)' in text


@pytest.mark.parametrize('summary', ['', 'x' * 161, 'two\nlines', 123])
def test_summary_contract_rejects_bad_values(summary):
    data = researched()
    data['candidates'][0]['reason_summary'] = summary
    with pytest.raises(UniverseError, match='reason_summary'):
        build(data)


def test_older_reasons_have_a_bounded_readable_excerpt_without_mutation():
    member = dict(reason='Observe 3.5 GHz radio equipment. Detailed audit facts follow.')
    assert _brief_reason(member) == 'Observe 3.5 GHz radio equipment.'
    assert 'Detailed audit facts follow' in member['reason']
    chinese = dict(reason='观察信贷与存款。完整审查保留在记录中。')
    assert _brief_reason(chinese) == '观察信贷与存款。'
    assert _brief_reason(dict(reason_summary='Funding | lending')) == 'Funding \\| lending'
    assert len(_brief_reason(dict(reason='long ' * 100))) <= 160


def test_authored_translations_only_change_requested_report_not_research_or_selection():
    data = researched()
    member = data['candidates'][0]
    member['name'] = '测试银行'
    member['reason_summary'] = '存款与信贷。'
    data['taxonomy'][0]['purpose'] = '存款与信贷需求。'
    original, original_report = build(data)
    data['report_translations'] = {'en': {
        '测试银行': 'Test Bank', '存款与信贷。': 'Deposits | lending.',
        data['taxonomy'][0]['purpose']: 'Banking demand and earnings drivers.',
    }}
    universe, report = build(data)
    before = deepcopy(universe)
    english = render_markdown(universe, report, 'en')
    chinese = render_markdown(universe, report, 'zh-Hans')
    row = next(line for line in english.splitlines() if line.startswith('| NYSE:CORE0 |'))
    assert 'Test Bank' in row and 'Deposits \\| lending.' in row
    assert '测试银行' in chinese and '存款与信贷。' in chinese
    assert 'Banking demand and earnings drivers.' in english
    assert universe == before
    assert universe['members'] == original['members']
    assert universe['version_hash'] == original['version_hash']
    assert universe['content_hash'] != original['content_hash']
    assert render_txt(universe) == render_txt(original)
    assert original_report['qualified'] and report['qualified']


@pytest.mark.parametrize('translations', [[], {'xx': {}}, {'en': []},
                                         {'en': {'x': ''}}, {'en': {'x': 42}}])
def test_translation_contract_rejects_malformed_maps(translations):
    data = researched()
    data['report_translations'] = translations
    with pytest.raises(UniverseError, match='report_translations'):
        build(data)


def test_cn_example_english_content_and_direct_chinese_member_briefs():
    folder = Path(__file__).resolve().parents[1] / 'examples/cn-medium/output'
    english = (folder / 'cn-medium-2026-10-08.en.md').read_text(encoding='utf-8')
    chinese = (folder / 'cn-medium-2026-10-08.zh-Hans.md').read_text(encoding='utf-8')
    assert not re.search(r'[\u3400-\u9fff]', english)
    rows = [line for line in chinese.splitlines() if re.match(r'\| (?:SSE|SZSE):', line)]
    assert len(rows) == 302
    assert all('| 观察' not in row for row in rows)
    assert '航空产品。' in next(row for row in rows if 'SSE:600760' in row)
    assert 'Aviation products.' in english


def test_all_worked_english_reports_have_authored_english_content():
    root = Path(__file__).resolve().parents[1] / 'examples'
    reports = sorted(root.glob('*/output/*.en.md'))
    assert len(reports) == 10
    for path in reports:
        text = path.read_text(encoding='utf-8')
        assert not re.search(r'[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af]', text), path
        assert 'no factor statistics' not in text, path
