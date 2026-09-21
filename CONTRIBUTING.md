# Contributing

## The rules that are not style

1. **Every change to deterministic logic ships with a test.** Selection, gating, ranking, apportionment,
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
than reviewed. **Registering** a market is five additions — a `MARKET_SPECS`
row, a breadth number, a starter taxonomy, an overlay and a seed table — plus locale keys if its
language is new. See
[`references/markets/adding-a-market.md`](references/markets/adding-a-market.md).

Do not ship an unexercised market overlay on speculation. The seed table is what exercises it,
which is why it is one of the five and not a follow-up: a test asserts that the set of examples
equals the set of registered markets, so a row added without one fails on the same commit.

## Cutting a release

The skill's version lives in `SKILL.md` frontmatter and is semver. Three places carry it and a
test pins two of them together; the third is the tag, which is why the order below matters.

```bash
# 1. bump SKILL.md  version: X.Y.Z
# 2. head the changelog  ## X.Y.Z — YYYY-MM-DD
python -m pytest tests -q          # VersionTests fails if 1 and 2 disagree
git commit -am "Release X.Y.Z" && git push
git tag vX.Y.Z && git push origin vX.Y.Z
clawhub skill publish . --version X.Y.Z --dry-run   # read it, then run it without --dry-run
```

### The listing text

GitHub's description and topics are set in the web UI and are therefore the one thing about a
release that no test can see. They are kept here so a change to them is reviewable:

**Description**

```text
An agent skill that builds and maintains auditable ticker universes for fourteen markets — every
member carrying a role, a reason and dated evidence — and renders them as TradingView watchlists.
An observation instrument, not investment advice.
```

**Topics**

```text
claude-skill  agent-skills  anthropic  openclaw  clawhub  skill  tradingview  watchlist
stock-market  equities  crypto  market-data  finance  python  zero-dependency
```

Nothing here claims a capability the skill refuses to have. `portfolio`, `trading-bot`,
`signals` and `stock-picker` are all topics this project would rank well under and all four
would be a lie, so they are not in the list and should not be added because traffic is slow.

What counts as which digit is decided by what a *caller* has to change, not by how much work it
was. A new market, a new locale, a new theme table: minor. A changed artifact shape, a removed
field, a renamed exclusion code, a policy default that moves an existing universe off its
target: major. A wrong symbol rule, a wrong theme table, a doc that describes a skill that no
longer exists: patch.

Regenerating the examples is not by itself a release. They move whenever selection, ordering,
rendering or hashing moves, and that change is already the thing being versioned.

## Adding a locale

`assets/locales/*.json` are flat key-value files and must stay key-for-key identical; a test
asserts it. Only the report chrome is translated — validation diagnostics stay English because
they name policy fields and code paths, and a translated field name cannot be grepped.

Translations are held to reading as native prose, not to being literally correct. A phrase that
a domain reader would never say is a defect even if every word maps.

## Licensing

This repository is MIT. Its OpenClaw registry listing is **MIT-0** — MIT without the attribution
requirement — because ClawHub has no licence field and distributes on those terms.

By contributing you agree your work may go out under both. That is not boilerplate: dual-stating
it only works while everyone who wrote a line agrees, and quietly relicensing someone else's
contribution later is the failure mode this paragraph exists to prevent.

## Style

- Line length 100, `ruff check .` clean, `select = ["E", "F", "I", "UP", "B"]`.
- Comments explain *why*, and only where the reason is not on the screen. The codebase has very
  few and they are all load-bearing; keep it that way.
- Commit messages say what changed about the design, not which files moved.
