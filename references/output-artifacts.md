# Standard output and delivery

Pass `--output DIR` explicitly; the CLI has no default. If unspecified by the user, the agent
uses an absolute `ticker-universes/<market>/<profile>/<as_of>/` in the user's project, outside
installed skills. Revisions require a new empty directory; existing artifacts are not overwritten.

## Artifact bundle

Stem: `{market}-{profile}-{as_of}`, with Light/Medium/Heavy/Max profile names lowercase.

| File | Content |
|---|---|
| `{stem}.json` | Authoritative members, admissions, plan, references, evidence, measurements, rejections, limits, hashes and history; Max embeds Heavy |
| `{stem}.validation.json` | `passed`, `qualified`, errors, warnings, counts and coverage/expansion checks |
| `{stem}.txt` | TradingView venue-prefixed codes and `###` groups; entities, references and headers together use at most 1,000 tokens |
| `{stem}.en.md` / `{stem}.<market-language>.md` | Readable structure, short member reasons, material limits and Max additions |
| `{stem}.en.html` / `{stem}.<market-language>.html` | Complete offline dark report with members, references, warnings, folded research notes and relative artifact links |

English is always generated; `--language` changes only the companion. US/Crypto normally have
five files, CN seven. Headings use locales; human text uses authored `report_translations`.
The CLI does not translate research. HTML uses two independent CSS columns on desktop, one on
mobile, without model calls or external assets; read down the left column, then the right.

`reason_summary` supplies one short business reason; older inputs use a first-sentence excerpt
capped at 160 characters. Full reasons, admissions, sources, market-cap evidence and per-ticker
measurement diagnostics stay in JSON. Material warnings and partial status stay visible.
Maintenance uses the same bundle with operations/turnover/deferred decisions in its history/report.
Specs, snapshots, raw receipts and price CSVs are research inputs, not extra final watchlists.

Deliver links to HTML, Markdown, TXT, universe JSON and validation. State entity/reference counts
separately, effective source cutoffs and status. Filename date does not mean every fact was refreshed.
Read language-keyed paths from `artifacts.reports` and `artifacts.html_reports`.
Keep the bundle together; open HTML locally, since GitHub displays its source.

## Receipt and checkpoint

Stdout JSON includes status, filled/unused capacity, artifact paths, warnings, checkpoint and
continuation. It is not an additional bundle file unless the caller saves it.

```text
DIR.run/
  run.json
  attempt-001/{inputs.json,result.json}
  attempt-002/{inputs.json,result.json,artifacts/}
```

`--run-dir` changes the checkpoint location. Archived inputs contain spec/snapshot/policy/seed/
language; results retain receipts and diagnostics. Attempts are preserved. Use returned paths
rather than assuming resumed artifacts live in the initial output directory.

```bash
python scripts/universe.py build --resume DIR.run --snapshot repaired.json
```

Do not move rendered directories: checkpoints refer to them. Deliver copies or links.
`artifact_sha256` maps actual paths to hashes; same-input resume checks them. Missing/changed
artifacts yield `needs_research` without another attempt. Restore originals or regenerate with
`--output NEW_EMPTY_DIR`; this repairs delivery, not research.

## Delivery status

| Status | Exit | Meaning |
|---|---:|---|
| `complete` | 0 | Every gate passed; unused ceiling capacity allowed |
| `partial` | 3 | Explicit Max growth-only gap within 5% of required entities; positive Beta growth, all other checks passed; `passed: true`, `qualified: false` |
| `needs_research` | 2 | No new qualified bundle; retain diagnostics and continuation |

Partial stems end `-partial` before language/extension. Disclose actual growth, required count,
gap and continuation. Legacy under-target partials do not certify current economic coverage.
See [recovery](recovery.md) for the repair loop and [data contracts](data-contracts.md) for validation.
