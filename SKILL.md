---
name: ticker-universe-builder
description: Build and maintain auditable, evidence-gated ticker universes for fourteen markets at four depths, exported as TradingView watchlists. Not stock tips.
allowed-tools: Read, Write, Bash, WebSearch, WebFetch
metadata:
  version: 0.9.2
  homepage: https://github.com/bitpunklabs/ticker-universe-builder
  openclaw:
    emoji: "📋"
    homepage: https://github.com/bitpunklabs/ticker-universe-builder
---

# Ticker Universe Builder

Research one market at a time. The agent supplies sourced facts and judgements;
Python validates, selects, hashes and renders. Run commands from the skill root.

## Route the request

Start with the closest [worked input](examples/README.md). Read specs/report summaries first;
inspect relevant snapshot rows programmatically. Compact ZIPs omit reports: recreate them with
`python examples/build_examples.py` if needed.

| Task | Read |
|---|---|
| New build | [Methodology](references/methodology.md), [depths](references/tier-profiles.md), [coverage plan](references/coverage-plan.md) |
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

## Boundaries

- Never invent tickers, venues, listing states, metrics, theme relationships or sources.
- Never hand-write final watchlists or bypass validation.
- Protect leaders, necessary peers and direct reference duties before optional Beta; no padding,
  role promotion to fill seats, tactical fallback or permanent heat-based themes.
- Light/Medium are leader-only; Heavy permits at most 20% satellites, Max at most 35% overall.
- No return guarantees, allocations, order instructions or trade execution.
- Archived replay requires `assets/legacy-policy.json` explicitly and does not certify current coverage.
