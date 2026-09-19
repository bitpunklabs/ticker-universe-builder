---
name: ticker-universe-builder
description: Build a new or maintain an existing CN, US, or Crypto ticker universe at Light, Medium, or Heavy depth. Use when the user wants an auditable market universe or ticker pool, sector and theme coverage, leader and satellite selection, a universe review, or TradingView-importable watchlist files. Do not use for stock tips, portfolio construction, order instructions, or trade execution.
allowed-tools: Read, Write, Bash, WebSearch, WebFetch
---

# Ticker Universe Builder

Build one market at a time. Treat `cn`, `us`, and `crypto` as independent universes.

Read [examples/README.md](examples/README.md) first and open the example for the market you were
asked about. One worked snapshot answers more questions about the input format than the contract
does, and the shipped examples are known to build.

## Route the request

1. Read [references/methodology.md](references/methodology.md) and
   [references/tier-profiles.md](references/tier-profiles.md).
2. Read exactly one market overlay:
   - CN: [references/markets/cn.md](references/markets/cn.md)
   - US: [references/markets/us.md](references/markets/us.md)
   - Crypto: [references/markets/crypto.md](references/markets/crypto.md)
3. For an existing universe, also read [references/maintenance.md](references/maintenance.md).
4. Read [references/data-contracts.md](references/data-contracts.md) before writing any JSON.
5. Follow [references/source-policy.md](references/source-policy.md) for evidence and provider use.
6. Read [references/measurement.md](references/measurement.md) before filling in any metric.

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

1. Write `build-spec.json` from the user's request. Use the policy defaults unless the user asks
   for a target count inside the documented guidance range.
2. Start the taxonomy from the published one rather than inventing themes per run — two
   universes of one market built on ad-hoc taxonomies cannot be compared:

   ```bash
   python scripts/universe.py taxonomy --market us --profile light
   ```

   Edit it: add what the market has grown, drop what it has not. It is a starting point, not a
   schema.
3. Research the eligible universe against that taxonomy. Record facts in `snapshot.json`;
   never pass a claim to the scripts hidden inside prose.
4. Declare in `measurement` how each metric was produced. A window-dependent statistic —
   liquidity, `factor_r2`, `beta_strength`, `beta_stability` — must be computed, not estimated,
   and the builder refuses to accept it as judgement. If you have a table of daily bars, compute
   them instead of arguing with the gate:

   ```bash
   python scripts/universe.py measure --prices prices.csv --benchmark BINANCE:BTCUSDT.P \
     --source https://data.binance.vision/ --into snapshot.json --output snapshot.measured.json
   ```

   See [references/measurement.md](references/measurement.md). If you have no price table, the
   candidates that need those metrics do not belong in the universe yet.
5. Cite current sources for listing status, venue, liquidity and every non-obvious admission. If
   an essential fact cannot be verified, exclude the candidate or mark the snapshot incomplete.
6. Run:

   ```bash
   python scripts/universe.py build \
     --spec build-spec.json \
     --snapshot snapshot.json \
     --output output
   ```

7. The command prints the path of every artifact it wrote; they are named
   `{market}-{profile}-{as_of}`. Run `validate` on the `universe` path even though the builder
   validates before writing. Never present an output that fails.
8. Return the human-readable `.md` and the TradingView-importable `.txt`. The `.md` is written
   in the market's own language — Simplified Chinese for CN, English for US and Crypto — so
   write the snapshot's names, themes, reasons and methods in that language too. `--language`
   overrides it; nothing else about the build changes.

To change the depth of an existing universe, pass it as `--seed` instead of rebuilding. Widening
keeps every incumbent and fills the rest; narrowing reselects inside the incumbents against the
smaller target. A rebuild at the new depth churns a universe whose entire purpose is low turnover.

The model proposes taxonomy, roles and evidence. Python owns normalization, eligibility gates,
tier nesting, quotas, ordering, caps, hashing and rendering. Never hand-write the final txt.

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
a note for a later round is how a universe rots: use `ADD_THEME`, `REMOVE_THEME`, `MOVE` and
`REPLACE` in the same round, or record the candidate in `deferred` so the next round inherits it.

## Non-negotiable boundaries

- Never invent a ticker, venue, listing state, liquidity number, theme relationship or source.
- Never select a name solely because it is popular or recently rose.
- Preserve benchmarks and anchors before adding satellites.
- Heavy means broader independent observation, not relaxed quality or an arbitrary long tail.
- No return guarantees, allocations, order instructions or trade execution. This skill produces
  an observation instrument, not investment advice.
- Keep each TradingView file at or below 1,000 tokens including `###` section headers.
