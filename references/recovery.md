# Continue an interrupted or underfilled build

`build` keeps an append-only attempt history in `OUTPUT.run/run.json` by default. Use
`--run-dir PATH` to choose another checkpoint directory. Each attempt archives the exact spec,
snapshot, resolved policy and seed, their combined SHA-256, diagnostics and artifact paths.
The run index is updated atomically. Use a single writer per checkpoint.

| Exit | Status | Meaning |
|---|---|---|
| 0 | `complete` | All quality gates passed, including Extreme +35%–40%; unused capacity above the minimum is allowed (legacy replay: count filled) |
| 2 | `needs_research` | Input, coverage, seed or output error prevented publication |
| 3 | `partial` | Legacy replay only: valid subset below the requested size |

For coverage-first, resolve necessary representatives and Core decisions before optional depth.
A below-band Extreme is `needs_research`, never complete or silently replaced by Heavy. Read
the error's selected/required/missing counts and `diagnostics.expansion`: its proposed-candidate
count is only a bench capacity bound, before sector, satellite, evidence and export checks.
Widen research for the missing Beta, remeasure and resume. Never loosen quality just to add
codes. Outside this Extreme growth requirement, the following target-fill diagnostics apply
to legacy replay only.
Read the diagnostic for every intermediate tier, not just the first missing theme. Capacity
counts are upper bounds, not promises: duplicate assets, mandatory members and token limits can
still constrain selection. A 1,000-token ceiling is a real boundary; never hide a target reduction.

The agent owns the research loop; the Python selector is deliberately offline:

1. For transient provider failure, repeat `fetch` in the same data directory. Its same-day,
   exact-request cache retains successful responses; transient HTTP/network errors already have
   three request attempts. Inspect exclusions separately from transport failures.
2. For missing economic branches/representatives, repair that research or verify another source.
   Unused capacity above Extreme's growth minimum does not require expansion. In legacy replay, missing themes/counts
   may instead require a broader verified bench.
   Repair missing listing/provenance facts, and rerun `measure` on the changed data. Preserve
   verified candidates and disclose scope exclusions. Do not reinterpret a missing quote as a
   delisting, or invent a theme, metric or classification just to fill a slot.
3. Continue with the command printed in `resume_command`, for example:

   ```bash
   python scripts/universe.py build --resume output.run --snapshot snapshot.repaired.json
   ```

   Paths omitted on resume retain their original values. Changing the file at the saved path is
   also supported. Unchanged inputs return the last outcome without spending another attempt;
   a run interrupted while `running` may retry those inputs. Completed earlier outputs are kept.
   Later artifacts go in `RUN_DIR/attempt-NNN/artifacts`, unless `--output` names a new empty path.
4. Normally try up to three distinct repair rounds. Record what changed and why in the snapshot
   notes. Do not run three identical failing commands. A research bench smaller than the target is not a source capacity ceiling. Check fetched but
   unmapped candidates and alternative verified sources first. When Heavy and Extreme contain
   identical members, disclose zero expansion and continue classification research; regenerating
   identical snapshots is not a repair round. A proven source capacity ceiling, an
   unavailable required input or the user's budget can end the loop sooner. Return a valid
   partial subset only with its actual count, requested count, missing work and checkpoint.

Resuming does not guarantee more eligible assets exist. Do not call a partial Extreme complete,
silently substitute Heavy, or broaden the user's market/venue scope without disclosing it.
This workflow adds local receipts, not an agent runtime or automatic network research in `build`.

Syntax errors or unreadable initial input files must be fixed before the first build attempt can
be archived. Existing output directories are never overwritten. A continuation requiring a new
output path may pass `--output` explicitly.
