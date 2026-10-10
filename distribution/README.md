# Distribution

| Channel | Recorded status |
|---|---|
| [GitHub Releases](https://github.com/bitpunklabs/ticker-universe-builder/releases/latest) | Compact installable Skill ZIP, checksums and automatic full source archives; MIT |
| [ClawHub](https://clawhub.ai/bitpunklabs/skills/ticker-universe-builder) | 0.9.1 published under MIT-0; verification pass, ClawScan/VirusTotal clean; SkillSpector warnings remain, including a Korean example inconsistency |
| [skills.sh](https://skills.sh/bitpunklabs/ticker-universe-builder/ticker-universe-builder) | GitHub-backed installation; Claude Code/Cursor installs verified |
| [SkillsMP](https://skillsmp.com/creators/bitpunklabs/ticker-universe-builder/skill) | Indexed; recorded preview was 0.3.0, so prefer current source |
| Tencent / OpenAI marketplace | Deferred by owner; no upload |

Scan approval does not certify research quality. Tencent requires personal login/real-name
verification; OpenAI publication requires verified developer identity and platform review.

## Package and release

```bash
python scripts/package_release.py --compact --output temp/release-packages
```

Use a new/empty directory. Compact ZIP preserves runtime/rules and all ten specs/seven snapshots
byte-for-byte, excluding reports/screenshots; README files explain offline rebuilding.
Publish ZIP + SHA256SUMS. The local receipt records commit/dirty state and copied/rewritten hashes.
Test extracted CLI and examples before uploading. ClawHub's smaller bundle also omits outputs,
but compacts JSON whitespace; provenance hashes refer to upstream serialization.

Align SKILL metadata.version, plugin.json and CHANGELOG. Commit, pass remote CI, tag `vX.Y.Z`,
then publish; tags remain immutable. Use draft/prerelease for unfinished checks.
Before ClawHub publication inspect `clawhub skill publish --dry-run --json` and confirm license rights.

Optional full skill + skills-only OpenAI draft:

```bash
python scripts/package_release.py --output temp/plugin-packages \
  --developer-name "Your verified OpenAI developer name"
```

Without verified identity it is not submission-ready. Listing countries `[]` means all available
regions; platform scans/attestations remain dashboard steps. No MCP server or hosted runtime.
Icon: assets/icon.png, generated with ImageGen.
