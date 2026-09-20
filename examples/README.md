# Examples

Fourteen Light universes, one per registered market. Each builds and validates as shipped, and
the test suite rebuilds every one — a rotted example fails CI rather than a user's first attempt.

```bash
python scripts/universe.py build \
  --spec examples/crypto-light/build-spec.json \
  --snapshot examples/crypto-light/snapshot.json \
  --output /tmp/crypto-light
```

It writes `crypto-light-2026-09-17.{json,md,txt,validation.json}` and prints all four paths.

| Example | Members | Themes | Report | Shows |
|---|---:|---:|---|---|
| `crypto-light/` | 40 | 15 | English | Spot/perpetual merging via `asset_id`, the BTC/ETH/SOL factor measurement, a delisted pair and a stablecoin pair kept in the audit, and a `changes.json` that retires one satellite and adds one at 5% turnover |
| `us-light/` | 80 | 30 | English | The shared equity table unchanged — the thirty Level-1 themes here are `_equity.json` itself. Two recent listings as the tactical budget; a second share class and a sector ETF in the audit |
| `cn-light/` | 80 | 32 | 简体中文 | Venue-bearing identity (`SSE:` / `SZSE:`), semiconductors at 3.5 against property developers at 0.4, the cash-management exclusion every liquidity ranking otherwise puts first |
| `jp-light/` | 65 | 34 | 日本語 | The trading houses as their own group, semicap outweighing semiconductors, and an alphanumeric TSE code (`285A`) that a letters-only rule would have rejected |
| `hk-light/` | 55 | 32 | 繁體中文 | Bare numeric codes (`HKEX:5`, `HKEX:700`), the China platforms, the Macau gaming theme and a property complex the shared base has no room for |
| `in-light/` | 60 | 28 | English | IT services at 3.0 carrying the table, NBFCs as their own group, and symbols with `&` and `-` in them (`M&M`, `BAJAJ-AUTO`) |
| `kr-light/` | 55 | 35 | 한국어 | Semiconductors at the 4.0 ceiling, the battery chain, shipbuilding and K-pop as themes, and a preferred line audited as `duplicate_asset` |
| `tw-light/` | 50 | 27 | 繁體中文 | Two venues (`TWSE` / `TPEX`), hardware at 3.0 and IC design at 2.0 — the densest single-sector table shipped |
| `uk-light/` | 50 | 27 | English | Symbols ending in a dot (`BP.`, `SN.`, `AV.`), the investment trusts as a group, and an accumulating share class audited against the one already held |
| `de-light/` | 45 | 25 | Deutsch | A Xetra code opening with a digit (`4GLD`), autos at 3.0, and a table with no energy group at all |
| `fr-light/` | 45 | 28 | Français | Luxury at the 4.0 ceiling, and the `EURONEXT` venue caveat the overlay states outright |
| `ca-light/` | 45 | 25 | English | Unit and class tickers (`BIP.UN`, `TECK.B`), banks at 3.5, mining at 3.0, and a manager audited against its own parent |
| `au-light/` | 40 | 24 | English | Mining at 4.0 taking about a sixth of the universe — the weight doing visible work |
| `br-light/` | 35 | 23 | Português | Share-class digits (`PETR3` against `PETR4`), agribusiness as its own group, and managed care at Light, which no other table has |

## Every one of them is full size

Each example is exactly its market's Light target — which comes from that market's `breadth`
factor, not from a number in the generator — inside the guidance band, buckets on quota, and
**zero warnings**. No `allow_outside_guidance` anywhere, because an example that needs an escape
hatch teaches that the hatch is normal.

The honesty constraint behind the seeds has not moved: every ticker in `seeds/*.tsv` is written
from knowledge rather than read off an exchange listing. That is why a seed holds sixty to a
hundred and twenty names rather than a thousand, and why the seeds are a per-market table someone
can read in one screen and argue with.

Building them changed the code twice, which is the argument for having them. The `de` symbol rule
demanded a leading letter until `4GLD` failed it; the `br` rule demanded four letters until
`B3SA3` did. Both are real listings, both were rejected by a rule that looked right on paper, and
neither would have been caught by another English-language example.

They also changed nine of the theme tables. A theme with nothing listed in it is worse than no
theme — the breadth floor spends a slot on it regardless — so managed care leaves Light in Japan,
Korea, Hong Kong and the UK, where health cover is single-payer or national; energy and payments
leave the German table entirely; and managed care comes *up* to Light in Brazil, where private
health is listed and large. Each of those is recorded in the market's taxonomy note and overlay.

Medium and Heavy examples still do not ship. Growing a seed to 240 names is a TSV edit against a
real listing file, not a code change.

## Read one without running it

Each folder carries the report the build produces:

| File | What it is |
|---|---|
| `universe.md` | The built universe — roles, metric provenance, rejection counts, every member with its reason and evidence |
| `watchlist.txt` | The TradingView import file, sectioned by theme. This is the artifact that leaves the repository, so it is committed and diffable rather than only produced |
| `crypto-light/maintenance.md` | The same report after `changes.json` is applied, including the `## This review` block with turnover, additions and removals |

Both are generated, not written. Committing them means a change in selection shows up as a
reviewable diff instead of as a silently different result the next time someone runs a build.

Eight of the fourteen reports are not in English, because the report follows the market rather
than the tool. Their seeds are written the same way — `贵州茅台`, `トヨタ自動車`, `삼성전자`,
local `l1_name`, local `measurement.method` — since the renderer translates the chrome and leaves
the content exactly as the snapshot wrote it. A test asserts that each example's heading is the
one its market's lexicon produces. See
[markets/adding-a-market.md](../references/markets/adding-a-market.md) for the classification.

## They are generated from seeds

`seeds/{market}.tsv` holds the part that is real and hand-maintained — ticker, name, theme, role —
and `build_examples.py` expands it into `snapshot.json`, `build-spec.json` and the reports:

```bash
python examples/build_examples.py
```

The test suite regenerates and compares every generated file, so editing one directly fails CI.
Add a ticker to the TSV instead. Themes must come from the market's resolved taxonomy, which is
also asserted, so the examples and the starter tables cannot drift apart — and a market added to
the registry without an example fails a test on the same commit.

## The numbers are illustrative

The tickers, venues and taxonomies are real. Every metric is **derived by the generator** and was
not computed from market data; the evidence URLs point at the right kind of source rather than at
a page proving the specific number. Never copy these values into a real universe — run
[the measurement command](../references/measurement.md) instead.

## Try making one fail

The fastest way to understand the contract is to break it. Each of these stops the build with a
named error:

- Delete a `measurement` entry that a candidate uses.
- Change `factor_r2` to `{"basis": "judged"}`.
- Change `quality` to `{"basis": "judged", "method": "..."}` while candidates still carry facts.
- Add an `adverse_flags` entry that is not in the closed vocabulary.
- Drop `tier` from an evidence item.
- Write an `exclusion_reasons` entry that does not start with a known code.
- Set `complete` to `false`.
- Edit a member in a built universe file, then run `validate` — the hash will not match.
