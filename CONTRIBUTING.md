# Contributing

## The rules that are not style

1. **Every change to deterministic logic ships with a test.** Selection, gating, ranking, caps,
   hashing, rendering, validation — if the behaviour can differ between two runs, a test pins
   which one is correct. `tests/test_universe_core.py` is the home for almost all of it.
2. **The contract changes before the code does.** The shapes in `references/data-contracts.md`
   are agreed first, then implemented. A field that exists in the parser and not in the contract
   is a bug in both.
3. **The validator is never weakened to make an output pass.** If a real universe fails, either
   the universe is wrong or the rule is wrong — say which, in the commit message.
4. **No dependencies.** Standard library only, and CI proves it by installing nothing before
   running the suite. A change that needs a package needs a conversation first.
5. **No trade execution, ever**, and no feature that turns an observation universe into a
   recommendation: no rank, no grade, no score presented as a rating, no allocation.

## Before you commit

```bash
python -m pytest tests -q
ruff check .
python examples/build_examples.py && git diff --exit-code examples/
```

The third one matters more than it looks. The examples are generated from
`examples/seeds/*.tsv`, and any change to selection, ordering, rendering or hashing rewrites
them. A diff there is not noise — it is the change you just made, shown as its effect on a real
universe. Read it before committing it, and commit it in the same commit as the code.

If the hash changed, `examples/crypto-light/changes.json` carries a `base_version_hash` that has
to move with it.

## Adding a market

Two paths, and the cheap one is usually right. A market can be **declared** in the snapshot's
`market_spec` — venues, symbol shape, identity rule, size guidance — with no code change at all;
it builds under the same evidence gate as everything else and is reported as declared rather
than reviewed. **Registering** a market puts it in `MARKET_SPECS` with reviewed rules and is a
code change plus a test plus a starter taxonomy plus locale keys. See
[`references/markets/adding-a-market.md`](references/markets/adding-a-market.md).

Do not ship an unexercised market overlay on speculation.

## Adding a locale

`assets/locales/*.json` are flat key-value files and must stay key-for-key identical; a test
asserts it. Only the report chrome is translated — validation diagnostics stay English because
they name policy fields and code paths, and a translated field name cannot be grepped.

Translations are held to reading as native prose, not to being literally correct. A phrase that
a domain reader would never say is a defect even if every word maps.

## Style

- Line length 100, `ruff check .` clean, `select = ["E", "F", "I", "UP", "B"]`.
- Comments explain *why*, and only where the reason is not on the screen. The codebase has very
  few and they are all load-bearing; keep it that way.
- Commit messages say what changed about the design, not which files moved.
