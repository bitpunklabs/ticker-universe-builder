# AGENTS.md

Read [SKILL.md](SKILL.md) first. This repository contains one skill: **ticker-universe-builder**.

- Run `python scripts/universe.py <subcommand>` from the repository root. Python 3.10+, standard library only.
- Read [data contracts](references/data-contracts.md) before writing JSON and the closest
  [worked input](examples/README.md) before creating a snapshot.
- Tests: `python -m pytest tests -q`. Lint: `ruff check .`.
- Keep project documentation in English; generated market reports retain language companions.
  Refresh static screenshots separately with `examples/render_previews.cjs`.
- Never invent facts or sources, hand-write final watchlists, or weaken validation.
- No return guarantees, allocations, order instructions or trade execution.
