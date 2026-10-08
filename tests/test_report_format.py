"""Readable reports must not lose the authoritative research/audit record."""

from copy import deepcopy

import pytest
from test_coverage_core import build, researched
from universe_core import UniverseError, _brief_reason, render_markdown


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
