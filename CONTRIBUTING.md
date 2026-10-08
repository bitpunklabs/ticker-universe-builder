# Contributing

Keep runtime code compatible with Python 3.10+ and the standard library. Tests use pytest;
ruff configuration lives in pyproject.toml.

- Update [data contracts](references/data-contracts.md) before changing input/output shapes.
- Test changed deterministic behavior. Never weaken validation to make a fixture pass.
- Keep selection offline; provider adapters supply facts, and agents research admissions.
- Preserve the observation-only scope: no trade execution, allocations or return promises.

## Checks

```bash
python -m pytest tests -q
ruff check .
python examples/build_examples.py
git diff -- examples/
```

Inspect and commit intended example changes with their inputs. After committing, regeneration
must leave examples unchanged. The generator updates Crypto's maintenance base hashes too.

For markets and locales, follow [adding a market](references/markets/adding-a-market.md).
A declared market needs researched rules; a registered market also needs an overlay, taxonomy
and reproducible coverage tests. Example coverage and registered-market coverage are distinct.

## Release

Keep `SKILL.md` metadata.version and the newest [CHANGELOG](CHANGELOG.md) heading aligned.
Use an unreleased heading until publication. Breaking contracts require migration notes;
provider/correctness fixes are patches. Versions before 1.0 may change contracts between minors.

1. Review the complete diff, run checks, inspect online recovery evidence and TradingView import.
2. Commit the reviewed tree. Verify remote CI before tagging the same commit `vX.Y.Z`.
3. Create GitHub release notes naming changes, compatibility and observed limits.
4. If publishing ClawHub, run its bundle dry-run first and inspect the complete artifact set.
   `.clawhubignore` restores committed examples excluded by `.gitignore`; raw research stays out.
   A dry-run is not a registry upload or authorization check.

README edits and unfinished checks must be reflected in draft/prerelease status. Do not use
`git commit -am` to sweep unrelated work into a release. Keep published tags immutable.

## Licensing and disclosure

The repository uses [MIT](LICENSE). Contributions may also be distributed under MIT-0 for
the existing registry distribution. Do not redistribute provider histories without source rights.
Report exploitable issues through [Security](SECURITY.md); use ordinary issues for correctness bugs.
