# Registry packages

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
