# Registry packages

## Distribution channels

- [ClawHub](https://clawhub.ai/bitpunklabs/skills/ticker-universe-builder): `0.9.1`, published
  under MIT-0. Registry verification returns `pass`; final ClawScan and VirusTotal verdicts are
  clean. SkillSpector warnings remain visible; final review identifies most as false positives
  and notes a Korean example content inconsistency. Audit approval does not certify research quality.
- [skills.sh](https://skills.sh/bitpunklabs/ticker-universe-builder/ticker-universe-builder):
  public GitHub distribution; project installs verified for Claude Code and Cursor. One skill
  needs no grouping manifest; the CLI writes the host directories and project lock file.
- [SkillsMP](https://skillsmp.com/creators/bitpunklabs/ticker-universe-builder/skill): already
  indexed, but its preview still shows `0.3.0`. Use the current GitHub source, not cached prose.
- Tencent SkillHub and OpenAI/Codex marketplace: deferred by the owner; no upload. Tencent
  materials are prepared; personal login and real-name verification are required to resume.

The smaller ClawHub bundle keeps all ten build specs, seven snapshots, references and runtime.
It excludes generated example outputs and compacts JSON whitespace; run
`python examples/build_examples.py` to recreate outputs. Original provenance file hashes refer
to upstream serialization; registry verification exposes actual uploaded file hashes.
GitHub retains the complete examples and MIT license. Initial full-bundle registration returned
server errors; the smaller bundle registered successfully. The server cause was not confirmed.

## Prepare packages

The repository stays a single skill. `plugin.json` is listing metadata; packaging copies the
same runtime, references and dated worked examples into a skills-only OpenAI plugin.
There is no MCP server, hosted service or runtime install step.

```bash
python scripts/package_release.py --output temp/release-packages \
  --developer-name "Your verified OpenAI developer name"
```

Use a new or empty output directory. The command writes an ordinary skill ZIP, an OpenAI
plugin ZIP and a receipt with source-file hashes, archive hashes and source commit/dirty state.
It copies only tracked skill resources; tests, caches, raw research, credentials and `.git`
are excluded. Inspect and test the extracted package before uploading. Without a verified
developer name, the OpenAI package is a preparation draft; it is not submission-ready.

For ClawHub, inspect a `clawhub skill publish --dry-run --json` before publishing. Its platform
license is MIT-0; confirm rights to distribute under that license before publishing. The
GitHub/OpenAI distribution remains MIT unless the owner changes it explicitly.

The OpenAI listing contains English and Simplified Chinese text, three starter prompts,
the directory icon and release notes. `countries: []` expresses the owner's choice of all
available countries. Keep the exact verified identity in the final manifest. Required platform
scans, identity verification and legal attestations remain dashboard steps.

This is skills-only: the current [OpenAI submission rules](https://developers.openai.com/plugins/deploy/submission)
do not require MCP cases, reviewer credentials, a demo video, or all four MCP policy URLs.
The animation planned for the README can be added in a later version.

Icon: `assets/icon.png`, generated with ImageGen; brief: a navy square with cyan watchlist rows
and a violet grouping spine, no text or market-return symbolism.
