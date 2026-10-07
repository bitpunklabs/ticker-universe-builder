---
name: ticker-universe-builder
description: Build and maintain auditable, evidence-gated ticker universes for fourteen markets at four depths, exported as TradingView watchlists. Not stock tips.
allowed-tools: Read, Write, Bash, WebSearch, WebFetch
metadata:
  version: 0.7.0
  homepage: https://github.com/bitpunklabs/ticker-universe-builder
  openclaw:
    emoji: "📋"
    homepage: https://github.com/bitpunklabs/ticker-universe-builder
---

# Ticker Universe Builder

Build one market at a time. Every market is an independent universe; there is no cross-market
merge and a name listed in two markets is two members.

Registered markets, each with reviewed rules, its own theme table and a report in its own
language: `us`, `cn` (zh-Hans), `jp` (ja), `in`, `hk` (zh-Hant), `kr` (ko), `uk`, `tw` (zh-Hant),
`de` (de), `fr` (fr), `ca`, `au`, `br` (pt-BR), `crypto`. Anything else builds too — see step 6.

Read [examples/README.md](examples/README.md) first and open the example for the market you were
asked about — Medium examples ship for us, jp, cn, kr, hk, uk and crypto. For another
market, open the closest example and its own market overlay. The committed 0.4 snapshots are historical contract/regression examples, not current role or
classification policy; replay only with `examples/legacy-policy.json`; use the current starter and methodology for new research.
A worked snapshot answers more questions about
the input format than the contract does, and the shipped examples are known to build.
Read the example README, build spec and report summary first. Inspect relevant candidate rows
programmatically; do not load an entire multi-megabyte research snapshot into model context.

## Route the request

1. Read [references/methodology.md](references/methodology.md) and
   [references/tier-profiles.md](references/tier-profiles.md), then
   [references/coverage-plan.md](references/coverage-plan.md).
2. Read the market overlay at `references/markets/<market>.md` — exactly one. For an equity
   market read [references/markets/equity-common.md](references/markets/equity-common.md) first:
   the universe boundary, the fund-versus-basket redundancy test, the cash-management exclusion
   and the rule about regressing against the theme rather than the index are shared by all of
   them, and the per-market file covers only what is true there and nowhere else. `crypto` has
   no shared part; read [references/markets/crypto.md](references/markets/crypto.md) alone.
3. For an existing universe, also read [references/maintenance.md](references/maintenance.md).
4. Read [references/data-contracts.md](references/data-contracts.md) before writing any JSON.
5. Follow [references/source-policy.md](references/source-policy.md) for evidence and provider use.
6. Read [references/measurement.md](references/measurement.md) before filling in any metric.
7. To check a universe after the fact, read [references/evaluation.md](references/evaluation.md).

If the market or the depth is missing, ask only for the missing choice. Default the depth to
`medium` when the user asks for a generally useful universe without naming one.

## Start from a watchlist the user already has

If the user brings an existing TradingView export, do not retype it:

```bash
python scripts/universe.py import --watchlist theirs.txt --market us \
  --output snapshot.draft.json
```

The draft carries their tickers and their sections as a starting taxonomy, and nothing else — a
txt file does not say what is still listed, what anything is for, or how liquid it is. Every
candidate comes back ineligible and `complete` is false, so the draft cannot build until the
research below has been done against it. Tickers that do not belong to the named market are
reported rather than dropped.

## Build a new universe

1. Write `build-spec.json` from the user's request. Use the reviewed plan budgets unless the user asks
   for a smaller ceiling. Write `coverage_plan` first: stable economic sectors/branches, reviewed leader
   roster, necessary peers, scope, four entity ceilings and reference instruments. Counts are
   ceilings, never a reason to pad. When migrating a Core, run `audit-core` and resolve every
   original code before publishing Heavy; a retained code is not automatically a leader.
2. Start the taxonomy from the published one rather than inventing themes per run — two
   universes of one market built on ad-hoc taxonomies cannot be compared:

   ```bash
   python scripts/universe.py taxonomy --market us --profile light
   ```

   Edit display themes for readability. Their number and `weight` do not determine economic
   budgets in 0.6. Set stable parent-sector caps/weights in `coverage_plan` before looking at
   optional candidates. Merge sparse themes with economically adjacent themes through
   `coverage_plan.display_groups`; preserve underlying duties. Light/Medium may use broader
   groups; Heavy/Max share the same map. Max follows Heavy group entity proportions, with
   only integer rounding surplus, and stops at the minimum qualified expansion.
   Carry forward the user's existing economic-driver map when available, but recheck ambiguous
   assignments against current business disclosures. Preserve the method, not inherited mistakes.
   Separate the primary observation purpose from secondary businesses; fibre/cable is not an
   optical module, EDA is not generic enterprise software, and oilfield service is not shipbuilding.
   Apply the same legacy
   principles to every market: primary business, earnings/value capture, persistent catalyst,
   then supply-chain position. Provider sectors and product tags discover candidates; they do
   not replace that map. Declare each theme's `purpose` and `representative_roles` (contracts).
   Preserve market/sector gauges separately from companies. Do not generate weights from how
   many names the provider happened to return.
3. Check the table before researching a single candidate. This is the step that is cheapest to
   redo now and most expensive to redo later:

   ```bash
   python scripts/universe.py taxonomy --check taxonomy.json --market cn --profile light
   ```

   This is a legacy display-table diagnostic, not economic feasibility certification. The
   formal build checks economic branches, necessary representatives, sector caps and export limits.
4. Optionally fetch a dated research bench with `fetch` before researching admissions:

   ```bash
   python scripts/universe.py fetch --market cn --prices-until 2026-09-28 --limit 1250 --output temp/cn
   ```

   See [references/providers.md](references/providers.md). Fetch is optional and never chooses
   membership. Inspect the manifest, rejected histories and raw receipts; provider classification
   is a starting point, not issuer due diligence. Research the eligible universe against the taxonomy. Record facts in `snapshot.json`;
   never pass a claim to the scripts hidden inside prose. Research structural representatives
   before extensions. Add sourced `admission` records (leader/peer/satellite), not just roles:
   size/turnover leadership alone does not establish business leadership,
   and low R² alone does not establish useful independent information. Use candidate `reason`
   and evidence to explain the observed variable; several complementary leaders may share a
   theme. Unmapped candidates stay deferred, never in a permanent OTHERS or provider-industry
   catch-all. Do not promote a candidate's role merely to satisfy a coverage constraint.
5. Declare in `measurement` how each metric was produced. A window-dependent statistic —
   liquidity, `factor_r2`, `beta_strength`, `beta_stability` — must be computed, not estimated,
   and the builder refuses to accept it as judgement. If you have a table of daily bars, compute
   them instead of arguing with the gate:

   ```bash
   python scripts/universe.py measure --prices prices.csv --benchmark BINANCE:BTCUSDT.P \
     --source https://data.binance.vision/ --into snapshot.json --output snapshot.measured.json
   ```

   See [references/measurement.md](references/measurement.md). If you have no price table, the
   candidates that need those metrics do not belong in the universe yet.
6. Supply a dated active `listing` check, admission `reason`, strong evidence and per-ticker
   `measurement_record`. Cite current sources for listing status, venue, liquidity and every non-obvious admission. If
   an essential fact cannot be verified, exclude the candidate or mark the snapshot incomplete.
   For a market outside the fourteen, also research its rules and declare them in the snapshot's
   `market_spec` — venues, symbol shape, identity rule and one `breadth` factor sizing the tiers,
   with tier 1 or tier 2 evidence. Everything else about the build is unchanged. See
   [references/data-contracts.md](references/data-contracts.md#market_spec); do not guess a venue
   code or a symbol format, and say in your answer that the rules were declared, not reviewed.
7. Run:

   ```bash
   python scripts/universe.py build \
     --spec build-spec.json \
     --snapshot snapshot.json \
     --output output
   ```

8. A blocked or underfilled build starts a repair loop, not an immediate final error. Read
   [references/recovery.md](references/recovery.md): preserve the checkpoint, research the
   diagnostics, remeasure and resume. Normally allow up to three materially different repair
   rounds within the user's scope. Stop sooner when the accessible source universe is exhausted
   or a required external input is unavailable; explain that boundary and retain a continuation.
   A small mapped snapshot does not prove source exhaustion. Repair necessary coverage before
   researching optional depth. Max must add at least 40% of Heavy's entity count, entirely as
   qualified Beta. Below that minimum is `needs_research`, even when the backbone passes. Widen
   the researched bench and resume; never publish a shorter Max as complete. Unspent
   capacity above the minimum is allowed. Reference instruments do not count toward growth.
   Never weaken gates or hide the difference between a ceiling and actual membership.
9. The command prints the path of every artifact it wrote; they are named
   `{market}-{profile}-{as_of}`. Run `validate` on the `universe` path even though the builder
   validates before writing. Never present an output that fails. Review the content too: each
   economic duty still has a qualified representative, gauges remain observable, and role
   shortages are understood. A filled count with poor duty coverage is not a completed research
   result. Core supply far below its policy target calls for role/business research, not padding.
10. Return the human-readable `.md` reports and the TradingView-importable `.txt`. There are two
   reports wherever the market does not already read in English — `{stem}.ja.md` and
   `{stem}.en.md` for `jp`, and likewise Korean for `kr`, Traditional Chinese for `hk` and `tw`,
   Portuguese for `br` — because a universe is read both by the people who trade that market and
   by someone allocating across several. Write the snapshot's names, themes, reasons and methods
   in the market's language; only the report's chrome is translated, so the English report
   carries those fields exactly as the snapshot wrote them. `--language` names the companion
   report, not the only one: English is always written. Nothing else about the build changes.

If you have a price table covering the window after a universe was built, run
`evaluate --universe U --prices P` before proposing the next set of changes. It reports whether
the instrument saw the largest moves, which exclusion code cost the most, and which metric
ordered anything — see [references/evaluation.md](references/evaluation.md). It is not a
backtest and never reports what the universe "returned".

To compare two universes — two sessions, two months, two people — run
`diff before.json after.json`. It leads with `market_spec`, because for a declared market two
sessions that researched the venue list differently did not build two versions of one universe.

Use `--seed heavy.json` for Max. It must be a qualified Heavy from the same plan and
source date; only sourced, measured satellites may be added. For a narrower depth, rebuild from
the same reviewed roster. Plan for at least `ceil(0.40 * H)` new entities, where `H`
is the actual Heavy entity count. Check sector, satellite and export capacity before research;
the new growth minimum does not waive those gates. Update Heavy first when facts or necessary representatives change.

The model researches core business leadership and quality, economic branches and information gain.
For Beta, verify broad business/token identity, complementarity to named core members and sourced
market cap; do not spend time on detailed profitability or tokenomics analysis. Eligible Beta
are ranked by equity market cap (stocks) or circulating USD market cap (Crypto) within the
planned distribution. All measured/liquidity/listing gates remain.
Python owns evidence contracts, protected coverage, sector/satellite ceilings, identity, hashing
and rendering. Never hand-write the final txt. See the [0.7 design](docs/design/0.7.0-heavy-shaped-max.md).

## Maintain an existing universe

1. Load `universe.json`, not just the txt. The JSON carries the version and the audit history.
2. Refresh liveness, venue, liquidity, theme leadership, factor redundancy and event evidence as
   the market overlay specifies.
3. Produce a small `changes.json` against the exact `base_version_hash`. Prefer `NO_CHANGE` when
   fresh evidence does not justify churn.
4. Run:

   ```bash
   python scripts/universe.py maintain \
     --universe universe.json \
     --changes changes.json \
     --output output
   ```

5. A hard finding means no new universe. Repair the proposal; never bypass the validator. Report
   warnings, additions, removals, turnover and deferred candidates in the Markdown result.

A verdict must come with an operation. Judging a theme obsolete or missing and writing it down as
a note for a later round is how a universe rots: use `ADD_THEME`, `UPDATE_THEME`, `REMOVE_THEME`, `REFRESH`, `MOVE` and
`REPLACE` in the same round, or record the candidate in `deferred` so the next round inherits it.

## Non-negotiable boundaries

- Never invent a ticker, venue, listing state, liquidity number, theme relationship or source.
- Never select a name solely because it is popular or recently rose.
- Preserve benchmarks and anchors before adding satellites.
- Light is leader-only; Medium covers most reviewed leaders; Heavy completes the necessary
  leader/peer skeleton plus at most 20% satellites; Max adds at least 40% to qualified Heavy,
  entirely as Beta, with at most 35% satellites overall. The latter is a quality ceiling,
  distinct from the required expansion minimum.
- Every optional satellite must explain its incremental value relative to named core members.
  No BREADTH_PROXY/tactical fallback, no padding to satisfy growth, no hot-theme budget inflation.
- Preserve direct reference instruments and explicitly explain substitutions; references do not
  consume leader seats. A passed contract does not independently establish leadership truth.
- No return guarantees, allocations, order instructions or trade execution. This skill produces
  an observation instrument, not investment advice.
- Keep each TradingView file at or below 1,000 tokens including `###` section headers.
