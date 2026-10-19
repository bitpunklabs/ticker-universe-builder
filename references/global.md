# Global composition

Use this mode for a researched Global selection across native-market universes and direct
index/ETF references. It is a separate composition, not a fifteenth market or another depth.
Read [data contracts](data-contracts.md), [source policy](source-policy.md) and the closest
[worked input](../examples/global/README.md). [Implementation design](../docs/design/0.10.0-global.md).
For the smaller reviewed companion, use [Global Core](global-core.md); it preserves the parent
market/theme map and adds complete member reviews, with optional explicit full-only operating depth.

## Research before composition

For a new scope, work through the [geography and thirty-family checklist](global-coverage.md).
Resolve exclusions explicitly before freezing the contract; it is not an automatic roster.

Define geographic gauges and economic child duties independently. Keep country, listing venue,
quote currency and operating exposure separate. Ordinary Global scope favors differentiated
indices, credible baskets and exceptional businesses, without national stock quotas or a
universal issuer-capitalization gate. A planning count is not a minimum to fill.

When native watchlists already exist, explicitly choose standalone or complementary Global scope.
For a complement, compare both exact codes and evidenced issuer aliases: changing an ADR to a
home listing does not remove company overlap. Preserve major CN/US index anchors and intentional
world franchises, while prioritizing incremental international businesses and credible baskets.
An ETF's listing venue is not its holdings geography. Record any retired/reassigned child duties
in a scope-review ledger before selecting a new parent; preserve every original source-theme
disposition. Detailed native duties can remain native responsibilities without being claimed as
Global coverage. Core normally preserves every parent duty; an explicitly requested focused
review can assign permitted operating depth to full only under the separate Core contract.

Concentrated businesses often warrant leaders first; dispersed industries may warrant a basket
and essential differentiated leaders. A fund name is not holdings evidence. Preserve financial,
industrial, consumer, healthcare and resource coverage alongside technology. A useful map includes
major Americas, Europe, Asia-Pacific and selected Middle East/Africa markets, but actual scope
must state what was researched and what was deferred. "Alpha" is not a return guarantee.

Create a frozen `global_coverage_contract` before selection. Do not shrink it to fit the roster.
Default to one primary instrument per economic issuer. Research ADR/share-class/home identities
and legal identifiers; keep unselected alternate lines in `identities`. V1 publishes one line
per issuer, with no A/H duplicate exemption. Ownership links are not legal-issuer identity.
Companies and protocols must come from qualified native universes; do not relabel them as refs.

## Commands

```bash
python scripts/universe.py compose-global --spec global-spec.json \
  --contract approved-coverage.json --output NEW_EMPTY_DIR
python scripts/universe.py validate-global NEW_EMPTY_DIR/global-2026-10-18.json \
  --contract approved-coverage.json
python scripts/universe.py check-watchlist NEW_EMPTY_DIR/global-2026-10-18.txt --ticker-only
python scripts/universe.py check-watchlist NEW_EMPTY_DIR/global-2026-10-18-by-theme.txt
```

Keep the independently reviewed contract as the expected input to validation. Hashes provide
integrity relative to that contract, not signatures or independent proof that an author selected
the right scope. Retain exact sources beside the delivered composition. Moving the entire bundle
is supported; editing a source or a TXT is detected by independent validation.

## Coverage contract

The object has `schema_version: 1`, `kind: "global_coverage_contract"`, a nonempty `scope`,
`scope_level: "global" | "pilot" | "synthetic"`, and these arrays:

| Field | Contract |
|---|---|
| `markets`, `themes` | `{id, name, purpose}`. IDs match `[A-Z0-9][A-Z0-9_]{0,39}`; names are safe ASCII headings. Every group has a duty. Global/context can be one market group alongside native countries. |
| `duties` | `{id, dimension, group, purpose, allowed_kinds, minimum, leader_minimum?}`. Dimension is market/theme. Minimum is positive; leader minimum defaults to zero. Market duties admit index/ETF gauges with market/style identity, not an operating company or sector-only fund. |
| `source_themes` | Every `SOURCE_ID:THEME_CODE` from every source universe taxonomy exactly once: `{id, disposition, themes, reason}`. `mapped` has nonempty Global theme IDs and selected source rows; `out_of_scope` has an empty array and no selected rows. Every selected row's source theme maps to its chosen Global theme. Catalogs have no native taxonomy. |

Optional `required_tickers` and `excluded_tickers` contain exact unique full codes. Use these
for the user's choices such as DIA/SOXX and bond-fund exclusions; do not hard-code one person's
choices into all markets. Optional `allow_peers: true` permits necessary researched peers;
they still do not count as leaders. No satellite can enter Global through this mode.

`etf_rules` may tighten the default floors below: `min_aum_usd`, `min_turnover_usd`,
`max_spread_pct`, `max_fee_pct: {broad, country, theme}`. It cannot silently relax them.

## Global spec and identities

`schema_version: 1`, `kind: "global_spec"`, ISO `as_of` not in the future, plus:

| Field | Contract |
|---|---|
| `sources` | `{id, kind, file, sha256}`; kind universe/catalog. Lowercase safe IDs; paths relative to spec or absolute; full SHA-256 of actual file bytes. Every source is dated within 30 days. Universe sources must independently qualify under current policy, using coverage-first selection. |
| `identities` | `{ticker, entity_id, name, economic_market, coverage_type, legal_ids, evidence}`. One row per exact ticker. Stable uppercase entity/legal IDs; evidenced identity, not ticker-derived aliases. Coverage type entity/market/style/theme/macro. Distinct selected tickers cannot share economic identity or a legal identifier. |
| `selections` | `{ticker, source, market, theme, duties, reason, evidence}`. Source must contain the exact ticker. Market equals the identity's economic market; claims must match known duties, group and instrument kind. |
| `coexistence_reviews` | Optional `{pair: [ticker_a, ticker_b], reason, evidence}` for two flagged selected ETFs with distinct duties. Identical benchmark wrappers are rejected even with a review. Unused reviews also fail. |

Source candidate admissions/listings/measurements remain authoritative. Global additionally checks
selected listing and measurement cutoffs within 30 days of composition; this is a staleness gate,
not certification of the latest completed session. Refresh under each native overlay when current
research is requested. Preserve actual cutoffs in the report. Identity/selection evidence requires
T1/T2 support within 180 days. Research assertions are not proven semantically by Python.

## Reference catalog

An object with `schema_version: 1`, `kind: "global_reference_catalog"`, `as_of`, `references`.
Each row is `{ticker, name, kind, observes, evidence, verified_ticker, verified_as_of, fund?}`.
The confirmed ticker must match, the name must match its identity, and matching dated strong
symbol evidence must be within 30 days. Kind uses the existing reference vocabulary, except
protocol spot must remain an entity. Direct indices need no fabricated volume.

ETF rows from either catalogs or native universes require the `fund` object below. Existing
`fund_review` prose or an old scan field does not satisfy this newer Global contract.

## ETF evidence and measurements

Ordinary V1 ETF support is **unlevered equity baskets**. Bond, leveraged/inverse, option-income,
cash-management and physical-commodity ETP structures are not accepted through this equity-fund
gate. Commodity prices/FX/yields/futures can remain separately verified direct references.

`fund` fields:

- `ticker` matching the row; `category: broad|country|theme`; actual `benchmark_id` and
  `exposure_group`; `structure: "unlevered_equity"`; ISO `inception` at least 365 days old.
- `assets_usd`, `gross_fee_pct`, `spread_pct`: each `{value, as_of, source}`, with a matching
  dated T1/T2 evidence item. Assets/spread at most 30 days old; fees at most 180 days old.
  Amounts/percentages must be finite numbers; booleans and missing values fail.
- Net assets at least USD 1 billion. Gross fee at most 0.25% broad / 0.65% country / 0.75%
  theme. Median relative spread at most 0.15%. Percent units are 0.15, not 0.0015.
- `holdings_as_of`, `holdings_source`, `holdings: [{entity_id, weight}]`: full issuer-normalized
  equity holdings with unique IDs and fractional weights totaling 0.98–1.02; normalize before
  overlap. Matching dated evidence and holdings within 30 days are required. A top-ten sample
  is not full holdings. Weights describe the fund, not a proposed user allocation.
- `activity: {source, as_of, currency: "USD", method, data_sha256, observations}`.
  Exactly 30 ordered, unique completed-session `{date, notional_usd}` rows; their last date
  equals activity `as_of`, no future observations, span at most 90 days and final date at most
  14 days old. Supply matching dated evidence. Mean notional must be at least USD 10 million.
  `data_sha256` is full SHA-256 over canonical JSON of the observations: UTF-8, sorted keys,
  compact separators, no NaN. See `global_core.digest`.
- Supported activity methods: `source_reported_notional`, `close_times_shares_proxy`,
  `local_notional_converted_to_usd`. Research must verify share units, FX convention and
  completed-session calendars; code checks recorded dates, not the exchange's live calendar.

Recompute fund-pair overlap as `sum(min(weight_a, weight_b))`. Holdings dates must be within
seven days; the actual gap is disclosed. Same exposure group or at least 80% overlap blocks
publication pending a valid coexistence review with distinct observation duties. A common
benchmark always requires choosing one wrapper. No invented return/alpha or automatic
leader-versus-fund superiority follows from this calculation.

## Artifacts and TradingView format

`global-DATE.json` is authoritative. The portable bundle also contains the pinned
`global-contract.json`, exact `source-ID.json` copies, validation JSON, English Markdown/HTML,
and three equivalent watchlists:

- `global-DATE.txt`: ticker-only companion for tooling and aggregates.
- `global-DATE-by-theme.txt`: safe `###` thematic headings.
- `global-DATE-by-market.txt`: safe `###` economic-market headings.

For a maintained human watchlist, default to publishing the generated by-theme bytes as
`global.txt` (and the equivalent Core view as `global-core.txt`), unless the user requests a
different format. Pin the selected view's path, format and hash in the current registry.
The CLI bundle's unsuffixed file stays ticker-only for backward compatibility; it need not be
the user's primary published file. Never hand-add headings or strip sections after rendering.

All are UTF-8, comma-separated exchange-prefixed codes on one line, with an optional final LF,
no BOM, comments, prices, empty tokens, guessed venues or duplicate symbols. Grouped views
must retain exactly the main ticker set; each header counts toward the repository's 1,000-token
export contract. Do not silently truncate or split coverage. The legacy import parser still
accepts handwritten/newline inputs; the new export checker deliberately rejects lossy output.

### Presentation layout

When the user requests a different navigation order, author an export-only layout instead of
changing economic themes or recomposing membership. Suggested observation order, when requested:
major indices, geographic indices, broad/regional/country ETFs, thematic ETFs, Crypto, FX,
commodities, rates/volatility, then industry-grouped company leaders. Keep listing venue separate
from economic geography. A currency index belongs with FX gauges; a volatility index is not a
regional equity index. Label perpetuals, commodity quotations and yields accurately.

The layout is a JSON object with exactly these fields:

| Field | Contract |
|---|---|
| `schema_version`, `kind` | Integer `1`, `"global_watchlist_layout"`. |
| `universe_sha256` | SHA-256 of the exact qualified Global or Core JSON file bytes. |
| `sections` | Ordered nonempty array of `{id, name, tickers}`. IDs use the Global safe-ID grammar; generated `###ID_NAME` headers use the strict ASCII heading grammar. Tickers are ordered full codes. Every section is nonempty; every universe member occurs exactly once, with no additions. |

```bash
python scripts/universe.py export-global-watchlist --universe BUNDLE/global-DATE.json \
  --contract approved-coverage.json --layout layout.json --output NEW_EMPTY_VIEW_DIR
python scripts/universe.py validate-global-watchlist \
  NEW_EMPTY_VIEW_DIR/global-DATE-by-observation.txt --universe BUNDLE/global-DATE.json \
  --contract approved-coverage.json --layout NEW_EMPTY_VIEW_DIR/layout.json
```

For Core pass its JSON and the complete Core review as `--contract`. Derive a separate Core
layout from retained parent members, omitting empty sections and pinning the Core JSON hash.
The commands revalidate the complete source bundle, including the parent for Core. Export writes
`*-by-observation.txt`, exact `layout.json` and validation JSON to a new empty directory; it does
not copy or replace the source bundle. Keep that independently portable bundle and expected
contract available alongside the layout view. Validation compares exact regenerated TXT bytes,
including member order and headings, rather than trusting a stored success flag.

Register a custom view as `by_observation` with its source path/hash and layout path/hash. This
view changes navigation only: evidence dates, members and all economic coverage claims remain
unchanged. The original three bundle exports still independently validate byte-for-byte.

[TradingView's official import documentation](https://www.tradingview.com/support/solutions/43000487233-how-to-import-or-export-a-watchlist/)
confirms TXT, exchange prefixes and comma separation. `###` grouped TXT follows the existing
repository convention; a ticker-only companion remains available. Correct syntax and
recorded symbol verification do not prove UI import, feed permissions or account capacity.
Only claim those after an actual separate browser test.

Publication is atomic and requires a new empty output directory. Failed composition returns
exit 2 and no new import bundle. `validate-global` recomputes source validity, identities,
coverage, ETF checks, canonical content digest and exact TXT files; it does not trust stored
`passed` flags. `pilot` and `synthetic` scope warnings stay visible even when their bounded
contracts qualify. Never label those a completed worldwide research run.
