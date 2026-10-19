# Global and its Core companion

Global has one composition mode, without Light/Medium/Heavy/Max profiles. Core is an optional
reviewed subset for focused observation. This worked example demonstrates the contracts with
**bounded CN/US/JP/HK/KR scope**, not a completed worldwide leadership screen.

The full pilot has sixteen companies and five market indices. Core keeps fifteen companies
and the same indices, prioritizing SK hynix as its direct memory representative while Samsung
remains additional depth in full. This small difference illustrates a review, not a target
full/Core ratio or a finding about investment returns.

| View | Report | Watchlist | Independent validation |
|---|---|---|---|
| Global | [Markdown](output/bundle/global-2026-10-18.en.md) / [HTML](output/bundle/global-2026-10-18.en.html) | [Sectioned](output/view/global-2026-10-18-by-observation.txt) / [Ticker-only](output/bundle/global-2026-10-18.txt) | [JSON](output/bundle/global-2026-10-18.validation.json) |
| Core companion | [Markdown](output/core-bundle/global-core-2026-10-18.en.md) / [HTML](output/core-bundle/global-core-2026-10-18.en.html) | [Sectioned](output/core-view/global-core-2026-10-18-by-observation.txt) / [Ticker-only](output/core-bundle/global-core-2026-10-18.txt) | [JSON](output/core-bundle/global-core-2026-10-18.validation.json) |

## Rebuild and validate

```bash
# Rebuild all native examples, then compose Global/Core from those qualified outputs.
python examples/build_examples.py

python scripts/universe.py validate-global \
  examples/global/output/bundle/global-2026-10-18.json \
  --contract examples/global/output/bundle/global-contract.json
python scripts/universe.py validate-global-core \
  examples/global/output/core-bundle/global-core-2026-10-18.json \
  --contract examples/global/output/core-bundle/global-core-contract.json
python scripts/universe.py validate-global-watchlist \
  examples/global/output/view/global-2026-10-18-by-observation.txt \
  --universe examples/global/output/bundle/global-2026-10-18.json \
  --contract examples/global/output/bundle/global-contract.json \
  --layout examples/global/output/view/layout.json
```

For a separate CLI rehearsal, use a new empty destination:

```bash
python examples/global/build_example.py --output temp/global-replay --with-core
```

`build_example.py` authors inputs and calls the maintained composition/layout engines; it never
writes final TXT. Output bundles retain exact source copies and can be moved independently.
The sectioned views place core/geographic indices first and industry-grouped companies last.
The pilot has no cross-asset instruments or admitted ETFs, so it creates no empty sections.

An optional `--fund-catalog PATH` adds a separately researched SOXX reference. It must pass every
[Global ETF gate](../../references/global.md); dated complete holdings, scale, costs, spreads and
histories are mandatory. Synthetic ETF tests are not market evidence. Production geography,
complementary-native overlap and thirty-family research follow the
[Global checklist](../../references/global-coverage.md).

Company facts and measurements retain native cutoffs; the three catalog index identities were
read on 2026-10-18. Offline replay refreshes no evidence and does not establish TradingView UI
import or feed permissions. Compact packages omit generated output: rebuild before opening links.
