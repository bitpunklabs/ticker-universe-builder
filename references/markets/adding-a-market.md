# Adding a market

Existing market rules live in `MARKET_SPECS` in `scripts/universe_core.py`.
Use a sourced `market_spec` for an unregistered market; register frequently used markets so
venue/identity rules no longer depend on per-run research. Registered rules reject overrides.

| Route | Rule source | Delivered claim |
|---|---|---|
| Declared | Snapshot market_spec with strong evidence | `Market rules: declared`; no starter taxonomy |
| Registered | Reviewed registry row, taxonomy and overlay | Repository-reviewed rules |

Both use the same coverage, admission, measurement, identity and maintenance contracts.
Declared markets require explicit legacy breadth/guidance compatibility, but current budgets
always come from coverage_plan. [Declaration shape](../data-contracts.md#market_spec).

## Register a market

1. Add `MarketSpec`: code/label, venues, symbol_pattern/hint, venue_in_asset_id, asset_id_strip,
   factor_r2_required, language and optional quality_flags. Test real listings; numeric/alphanumeric
   symbols such as Germany's 4GLD and Brazil's B3SA3 exposed earlier regex errors.
2. Research a coverage plan: branches, leaders/necessary peers, four entity ceilings, sector
   caps/weights, references and scope. Do not size it with legacy breadth multipliers.
3. Add `assets/taxonomy/<code>.json`. Equity starters extend `_equity.json` with drop/add/groups/
   level/weight changes; starter levels/weights do not allocate current seats. Check all four
   profiles without errors/warnings. Required duties need real representatives, not invented sectors.
4. Add `references/markets/<code>.md` for identity, local economic duties, adverse flags and sources.
   Link [shared equity rules](equity-common.md); do not repeat them.
5. Test a researched dated snapshot, actual measurements, build/validate and language outputs.
   Publishing a new example is a separate scope choice; use [worked inputs](../../examples/README.md).

CI checks every registry/taxonomy/locale and rebuilds the shipped examples. Real listing and
business tests matter: old starters promised managed-care/tech duties where no suitable listed
representatives existed. Fix the map instead of padding candidates.

## Quality flags

Use local codes only for a discrete published status whose distinction affects research and
is specific to that regime. Shared statuses belong in QUALITY_FLAG_CODES. Local codes need
translations in both English and the market locale, cannot collide across markets and retain
the same rule-score cost as universal flags. Declared markets can add at most six local codes.

## Report language

Registered locales: en, zh-Hans, zh-Hant, ja, ko, de, fr, pt-BR. Add missing languages with the
same keys as en.json. English is always generated; `--language` changes only the companion.
Locales translate fixed vocabulary; authored `report_translations` supplies human content.
Codes remain visible, and validation diagnostics remain English. Unknown declared flags print
bare codes with warnings.

Localization tests cover key/vocabulary completeness, CJK punctuation, distinct labels and
zh-Hans/zh-Hant conversion parity (regional exceptions are explicit). Use consistent depth
terms and distinguish membership turnover from trading turnover. Inspect actual rendered
reports; English headings with untranslated research do not make an English report.

## Scope decisions

There is no combined `eu` registry row: separate identity rules/report languages apply to Germany
and France. Switzerland/Saudi Arabia/Singapore remain declared routes until reviewed resources
are added. Crypto accepts Binance/OKX, while its bundled fetch adapter covers Binance only.
Research jurisdiction boundaries that venue prefixes cannot express, such as Paris within EURONEXT.
