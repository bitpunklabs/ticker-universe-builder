---
name: ticker-universe-builder
description: Build evidence-gated native and Global/Core ticker universes, with audited coverage and validated TradingView TXT exports. Not stock tips.
allowed-tools: Read, Write, Bash, WebSearch, WebFetch
metadata:
  version: 0.12.1
  homepage: https://github.com/bitpunklabs/ticker-universe-builder
  openclaw:
    emoji: "📋"
    homepage: https://github.com/bitpunklabs/ticker-universe-builder
---

# Ticker Universe Builder

Research native markets individually; compose Global views from validated sources. The agent
supplies sourced facts and judgements; Python validates, selects, hashes and renders.
Run commands from the skill root.

## Route the request

Start with the closest [worked input](examples/README.md). Read specs/report summaries first;
inspect relevant snapshot rows programmatically. Compact ZIPs omit reports: recreate them with
`python examples/build_examples.py` if needed.

| Task | Read |
|---|---|
| New build | [Methodology](references/methodology.md), [depths](references/tier-profiles.md), [coverage plan](references/coverage-plan.md) |
| Global / Global Core | [Global research and export contract](references/global.md); [reviewed Core subset](references/global-core.md) |
| Market rules | `references/markets/<market>.md`; equities also read [shared rules](references/markets/equity-common.md) |
| Write input JSON | [Data contracts](references/data-contracts.md) |
| Research / acquire data | [Sources](references/source-policy.md); optional [fetch adapters](references/providers.md) |
| Supply metrics | [Measurement](references/measurement.md) |
| Blocked / partial build | [Recovery](references/recovery.md) |
| Deliver results | [Output contract](references/output-artifacts.md) |
| Review existing universe | [Maintenance](references/maintenance.md) |
| Compare / evaluate | [Evaluation](references/evaluation.md); `diff before.json after.json` |

Registered markets: `us`, `cn`, `jp`, `in`, `hk`, `kr`, `uk`, `tw`, `de`, `fr`, `ca`, `au`, `br`,
`crypto`. Unregistered markets need a sourced [market_spec](references/data-contracts.md#market_spec).
Registered rules cannot be overridden. Ask for a missing market; default unspecified depth to Medium.

## Build

1. Declare `coverage_plan` before optional candidates: scope, sectors/caps, economic branches,
   reviewed leaders/necessary peers, four entity ceilings and separate references. When migrating
   a Core, run `audit-core` and resolve every original code before Heavy. Retention is not proof
   of leadership. Use the reviewed budgets unless the user requests a smaller ceiling.
2. Start from `taxonomy`, then check it. Map primary business/value capture and supply-chain
   position from sources, not provider tags. Merge sparse related display groups without changing
   economic duties. Heavy/Max share one group map; heading counts and news heat never create seats.
3. Research necessary representatives first. Record active listing, identity, strong evidence,
   admissions and per-ticker measurements in `snapshot.json`. Unknown essentials block admission;
   unmapped candidates remain deferred. Optional `fetch` collects a bench, not membership.
4. Compute window statistics with `measure`. Never estimate liquidity, R², beta or stability.
   Inspect raw receipts, symbol/volume units, cutoffs and missing data. Core requires business and
   quality research. Beta needs broad business/token identity, complementarity to named core
   members and sourced market cap; detailed profitability/tokenomics is optional. Rank Beta by
   cap within the planned distribution, never FDV. Supplied price factors need measured provenance;
   missing optional factors are disclosed rather than invented.
5. Build, then independently validate and review economic duties, assignments and limits:

   ```bash
   python scripts/universe.py build --spec build-spec.json --snapshot snapshot.json --output OUTPUT
   python scripts/universe.py validate OUTPUT/<market>-<profile>-<as_of>.json
   ```

6. On failure, read diagnostics, preserve the checkpoint, repair inputs and resume. Normally try
   up to three materially different research rounds. Stop for proven source exhaustion, unavailable
   required input or the user's budget; an undersized mapped bench alone is not exhaustion.
   Unchanged input does not consume another attempt. Never weaken a gate to finish.
7. Deliver returned HTML, Markdown, TXT, universe JSON and validation paths. Without a requested
   destination, pass an absolute `ticker-universes/<market>/<profile>/<as_of>/` inside the user's
   project. Use new empty revision directories; retain rendered paths and checkpoints.
   State entities separately from references, actual source cutoffs, warnings and delivery status.

Useful preflight commands:

```bash
python scripts/universe.py taxonomy --market us --profile light
python scripts/universe.py taxonomy --check taxonomy.json --market us --profile light
python scripts/universe.py import --watchlist core.txt --market us --output snapshot.draft.json
python scripts/universe.py audit-core --watchlist core.txt --universe old-heavy.json --output core-audit.json
```

Import saves transcription only: candidates remain ineligible and `complete: false` until researched.
Taxonomy checks display structure; build checks economic feasibility.

## Max and delivery

Use `--seed heavy.json`: qualified Heavy, same market, date and plan. Retain every member's facts
and binding; add at least `ceil(0.30 * H)` Beta entities following Heavy group proportions.
References do not count. Sector, satellite, entity and 1,000-token export ceilings still bind.
Repair Heavy first when core facts or duties change, then rebuild Max.

A growth-only gap within 5% of required entities may be explicit `partial` under the recovery
contract: positive Beta growth, every other check passed, original group quotas retained,
`qualified: false`, `-partial` filenames and a continuation. Larger gaps remain `needs_research`.
`--shortfall-action retry` requires full growth. Never present partial Max as complete or substitute Heavy.

English reports are always generated, plus the market-language companion. Supply authored
`report_translations.en` for names and other human content; the CLI does not translate research.
Use direct, one-sentence `reason_summary` (at most 160 characters, preferably 60 for Chinese),
without repetitive “Observe” prefixes. Full reasoning/evidence stay in JSON.

## Maintain

Load the authoritative universe JSON, refresh facts under the market overlay and submit
`changes.json` against its exact base version/content hashes:

```bash
python scripts/universe.py maintain --universe universe.json --changes changes.json --output OUTPUT
```

Apply justified operations now or record them in `deferred`. Prefer `NO_CHANGE` when evidence
shows no useful change. Failed validation publishes no new universe. Plan/reference/Core changes
require rebuilding Heavy and then Max. Use forward-window `evaluate` before proposing changes
when a wider price table is available; it measures observation coverage, not portfolio returns.

When full and Core converge, review primary anchors versus additional representatives before
adding names. Preserve original category headings; normally start Core with one primary leader,
adding genuine important complements rather than automatic second/third seats. Full-only status
does not demote a qualified leader to Beta or establish failed quality. Record omitted subfunctions
explicitly and preserve the complete migration audit. Compare company/entity counts separately
from the common index/reference base; no fixed Core/full ratio is a quality gate.

## Global compositions

For Global requests, read [Global](references/global.md) and its worked input. Freeze separate
geographic/theme duties before selection, preserve source-theme dispositions, and research
global issuer identities and ETF quality/overlap. Use exceptional leaders and credible baskets;
do not fill national quotas, infer ADR aliases or call a distinctive index proven alpha.

Declare whether Global stands alone or complements existing native lists. For a complement,
audit overlap by exact ticker and researched issuer identity; distinguish US listings from US
businesses and international ETF holdings. Prefer major indices, substantial qualified baskets
and exceptional world franchises. Keep intentional CN/US anchors, rather than copying every
native subindustry. Record revised scope and each retired duty before selection, preserving
the original taxonomy ledger; never conceal a gap by renaming an adjacent business.

Use `compose-global --spec S --contract C --output DIR`, then independently run
`validate-global DIR/global-DATE.json --contract C` against the original reviewed contract.
The portable bundle retains qualified source JSON and separately checked references. It generates
ticker-only, by-theme and by-market TXT views with identical membership. For a human watchlist,
publish the generated by-theme view as the main Global/Core TXT unless another view is requested;
for custom section ordering use the [reviewed presentation layout](references/global.md#presentation-layout)
and `export-global-watchlist`, then independently `validate-global-watchlist`. Keep geographic,
instrument and observation headings separate from economic coverage duties; assign every member
exactly once and bind the layout to the exact qualified JSON. Filter Core layouts to retained
members and omit empty sections. Never change taxonomy or membership just to rearrange a view.
Keep the ticker-only companion for tooling and ticker-only aggregates. Validate grouped files
with `check-watchlist FILE` and ticker-only files with `--ticker-only`. Do not infer format from
the destination basename. Failed gates publish no watchlist. Declare pilot/synthetic
scope, dated evidence and unverified TradingView UI import explicitly.

Global Core requires the [complete Core review](references/global-core.md), not a top-cap filter.
Review every parent ticker and theme; preserve every market/theme group and qualified ETF gate.
Default to all parent duties. When the user requests focused Core, use the complete optional
coverage-decision ledger to assign non-leader operating depth to full only; market, leader,
index and context duties and all retained minima stay binding. Never claim those omitted
functions as Core coverage. Prefer business relevance and genuine leadership before size/profit: an adjacent
advertising business cannot alone replace content/platform coverage. Concentrated franchises
favor leaders; dispersed functions favor credible baskets and essential distinct leaders.
Counts are guidance, not quotas. Review essential reference protection individually; do not freeze
every parent ETF when a retained index serves the same Core observation. Explain omissions with
surviving Core coverage and explicit full-only depth; verify holdings
when a basket is used to retain an omitted company's exposure.

Use `compose-global-core --parent G --parent-contract C --contract R --output DIR`, then
`validate-global-core DIR/global-core-DATE.json --contract R`. Core must be strictly smaller,
contain only unchanged parent members, and retain protected tickers. Its portable bundle pins
and revalidates the complete parent. Inherit evidence dates; refresh Global before refreshing
Core. Publish a maintained pair only after checking that Core references the currently selected
Global parent, each published format matches its exact generated view, and grouped sections
are nonempty with the same complete ticker set as the ticker-only companion.

## Boundaries

- Never invent tickers, venues, listing states, metrics, theme relationships or sources.
- Never hand-write final watchlists or bypass validation.
- Protect leaders, necessary peers and direct reference duties before optional Beta; no padding,
  role promotion to fill seats, tactical fallback or permanent heat-based themes.
- Light/Medium are leader-only; Heavy permits at most 20% satellites, Max at most 35% overall.
- No return guarantees, allocations, order instructions or trade execution.
- Archived replay requires `assets/legacy-policy.json` explicitly and does not certify current coverage.
