# Continue an interrupted or underfilled build

`build` stores append-only attempts in `OUTPUT.run/run.json`; `--run-dir` overrides the location.
Each archives effective spec/snapshot/policy/seed, combined SHA-256, dates, diagnostics and paths.
The index updates atomically; use one writer per checkpoint. Unreadable initial inputs must be
fixed before an attempt can be archived. Existing output directories are never overwritten.

| Exit | Status | Meaning |
|---|---|---|
| 0 | `complete` | Every quality/growth gate passed; unused capacity allowed |
| 2 | `needs_research` | Input, coverage, seed or delivery error blocks publication |
| 3 | `partial` | Valid bounded Max growth shortfall, or legacy under-size replay |

## Max shortfall handler

`shortfall_action` defaults to `auto`; CLI `--shortfall-action` overrides and persists on resume.

- `auto` / `deliver`: emit partial only if minimum growth is the sole failure, some Beta was
  added, the gap is at most 5% of required total entities and all other gates pass. Preserve
  original group ceilings/vacancies. Heavy 457 requires 595; 580 is a 15/595=2.52% gap.
  Output has exit 3, `qualified: false`, actual/required/growth/gap, `-partial` filenames and continuation.
- `retry`: require full growth. Larger gaps or invalid facts always yield `needs_research`, exit 2.
  Diagnose supply, group distribution and caps; research affected groups or another verified source.

`diagnostics.expansion` shows capacity before remaining constraints; `diagnostics.recovery`
identifies deficient groups and strategies. Counts are upper bounds: duplicates, protected core
and export limits can still constrain output. Beta's optional price factors are not admission
floors; listing, identity, measured liquidity, sourced cap and complementarity remain mandatory.
Legacy high-beta gates are unchanged. Only legacy replay has general target-fill diagnostics.

## Agent repair loop

1. Inspect every failed depth. Resolve necessary representatives/Core decisions before extensions.
   For transient acquisition failures, rerun `fetch` in the same directory; exact same-day cache
   retains successes and requests already allow three attempts. Separate scope exclusions from failures.
2. Preserve verified candidates; repair listing, business, gauges, mappings or sources and remeasure
   affected data. Do not infer delisting from one failed quote. An undersized mapped bench does not
   establish exhaustion: inspect fetched/unmapped candidates and alternative verified sources.
   No expansion is needed beyond Max's qualified minimum.
3. Use the returned continuation, for example:

   ```bash
   python scripts/universe.py build --resume output.run --snapshot snapshot.repaired.json
   ```

   Omitted paths retain saved values; editing a saved file is supported. Unchanged inputs return
   the last outcome without another attempt; interrupted `running` attempts may retry.
   Later artifacts use `RUN_DIR/attempt-NNN/artifacts` unless a new empty `--output` is supplied.
   Missing/changed saved artifacts require restoration or a new output path. [Delivery rules](output-artifacts.md).
4. Normally allow three materially different repair rounds, recording changes in snapshot notes.
   Stop for demonstrated source exhaustion, unavailable required input or user budget.
   Identical Heavy/Max is zero expansion, not a successful repair. Explain the remaining work and checkpoint.

Python does not research online or relax gates. Justified policy changes require uniform
remeasurement, not cherry-picking. Never call partial complete, silently replace Max with Heavy,
or broaden venue/market scope without disclosure. [Exact partial contract](data-contracts.md#max-shortfall-delivery-071).
