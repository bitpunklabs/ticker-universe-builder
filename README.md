# Ticker Universe Builder

An agent skill that builds and maintains **auditable ticker universes** for CN, US and Crypto
markets, and renders them as TradingView-importable watchlists.

[![ci](https://github.com/bitpunklabs/ticker-universe-builder/actions/workflows/ci.yml/badge.svg)](https://github.com/bitpunklabs/ticker-universe-builder/actions/workflows/ci.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)
[![dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen.svg)](pyproject.toml)

<!-- MEDIA PLACEHOLDER 1 of 2 — drop docs/media/demo.gif in place, then delete these two
     comment lines so the image below renders. Recording instructions: docs/media/README.md
![The skill building a Light crypto universe, end to end](docs/media/demo.gif)
-->

A ticker universe is an observation instrument, not a recommendation list. This skill exists to
gate it: every member arrives with a role, a reason and dated evidence; every change is an
operation against an exact version; and nothing is written unless the deterministic validator
passes.

## Contents

- [The problem this solves](#the-problem-this-solves)
- [Say this](#say-this)
- [Install](#install)
- [What you get](#what-you-get)
- [Use it when](#use-it-when)
- [How the work is divided](#how-the-work-is-divided)
- [What it guarantees](#what-it-guarantees)
- [The command surface](#the-command-surface)
- [Repository layout](#repository-layout)
- [Known limits](#known-limits)
- [Verifying](#verifying)
- [Contributing](#contributing)
- [Not investment advice](#not-investment-advice)

## The problem this solves

Ask any capable model for "a list of the 80 most interesting US tickers" and it will produce one
immediately. It will also be unreviewable. Twenty silently dropped names, a reordered section, a
mistyped venue and a company that delisted last quarter all look identical to a correct file, and
the next run — same prompt, same model — produces a different list with no way to say what
changed or why.

The failure is not that the model is bad at picking tickers. It is that a hand-written membership
list carries no structure to check: no record of which theme each name is there to observe, no
distinction between a benchmark and a satellite, no statement of what was rejected, and no version
to diff against. Research is exactly what a model is good at. Bookkeeping that has to be identical
twice is exactly what it is not.

So this skill splits the job. The model researches and proposes; Python normalizes, gates, ranks,
caps, hashes and writes. The output is a universe you can hand to someone else, argue with one row
at a time, and rebuild byte-for-byte a month later.

## Say this

The skill routes on intent. Literal prompts that trigger it:

- *"Build me a Light crypto ticker universe for observation, using Binance perpetuals."*
- *"Build a Medium US universe with sector breadth and ETF benchmarks, as of today."*
- *"Here's my TradingView watchlist export — turn it into a proper universe snapshot."*
- *"Review my CN universe (universe.json attached) and propose changes under 10% turnover."*
- *"Widen my Light crypto universe to Medium without churning the incumbents."*
- *"Evaluate the universe I built in July against the last 60 days of prices."*
- *"Diff these two universe.json files and tell me what actually changed."*

Name the market (`cn` / `us` / `crypto`) and the depth (`light` / `medium` / `heavy`). If you
skip the depth it defaults to Medium; if you skip the market you will be asked for it and nothing
else.

Prompts it will decline: stock tips, position sizing, allocations, entries and exits, "what should
I buy". See [Not investment advice](#not-investment-advice).

## Install

No dependencies. Python 3.10+ and the standard library.

**Claude Code — all projects**

```bash
git clone https://github.com/bitpunklabs/ticker-universe-builder.git \
  ~/.claude/skills/ticker-universe-builder
```

**Claude Code — one project**

```bash
git clone https://github.com/bitpunklabs/ticker-universe-builder.git \
  .claude/skills/ticker-universe-builder
```

Start a new session and ask for a universe; the skill loads itself from its `description`.

**claude.ai**

Zip the repository directory and upload it under **Settings → Capabilities → Skills**. The zip
must contain `SKILL.md` at its top level.

**Claude Agent SDK / API**

Mount the directory into the agent's skills path, or upload it as a container file and point the
skills setting at it. `SKILL.md` is the entry point; nothing else needs registering.

**Other agents**

[`AGENTS.md`](AGENTS.md) routes any agent that reads it, and
[`agents/openai.yaml`](agents/openai.yaml) carries the display metadata. The scripts are plain
Python with no host-specific assumptions — an agent that can run `python scripts/universe.py`
can use this skill.

## What you get

Four artifacts per build, all named `{market}-{profile}-{as_of}`.

A **`.md` report** you can read — written in the market's own language, Simplified Chinese for CN
([see the shipped example](examples/cn-light/universe.md)):

```markdown
# CRYPTO Ticker Universe

- Profile: Light
- Facts as of: 2026-09-17
- Version: `c8a5de84748b`
- Tickers: 40
- Themes: 15
- Theme cap: 4
- TradingView tokens: 55 / 1000
- Rejected or unselected candidates: 17
- Validation: PASS

## Members

| Theme | Ticker | Name | Role | Reason | Evidence |
|---|---|---|---|---|---|
| 00_A CORE_ASSETS | BINANCE:BTCUSDT.P | Bitcoin Perpetual | BENCHMARK | … | https://api.binance.com/… |
| 10_A L1_MAJORS   | BINANCE:ADAUSDT.P | Cardano          | THEME_LEADER | … | https://api.binance.com/… |
```

A **`.txt` watchlist** TradingView imports directly, sectioned by theme and capped at 1,000 tokens:

```text
###00_A_CORE_ASSETS,BINANCE:ETHUSDT.P,BINANCE:BTCUSDT.P,BINANCE:SOLUSDT.P,###10_A_L1_MAJORS,BINANCE:ADAUSDT.P,…
```

<!-- MEDIA PLACEHOLDER 2 of 2 — drop docs/media/watchlist-in-tradingview.png in place, then
     delete these two comment lines. Capture instructions: docs/media/README.md
![The generated watchlist after import into TradingView](docs/media/watchlist-in-tradingview.png)
-->

A **`.json` universe** — the version of record, carrying every member, every rejected candidate
with its exclusion code, the policy hash and the content hash. This is the file you keep and the
file you pass back in to maintain.

A **`.validation.json`** — the structural verdict. If it fails, the other three were never
written.

Three complete worked examples ship in [`examples/`](examples/README.md), one per market, rebuilt
by the test suite on every commit.

## Use it when

| Use it for | Do not use it for |
|---|---|
| An auditable observation universe or ticker pool | Stock tips or "what should I buy" |
| Sector and theme coverage at a chosen depth | Portfolio construction or position sizing |
| Leader, satellite and benchmark selection | Return expectations or backtests |
| A periodic universe review at bounded turnover | Entry and exit signals |
| A TradingView-importable watchlist | Order instructions or trade execution |
| Comparing two universes, or two people's versions of one | Anything requiring live market data — it has no network layer |

## How the work is divided

The model researches. Python decides.

| The model supplies | Python owns |
|---|---|
| Themes, roles, evidence, judgement, proposed operations | Normalization, eligibility gates, window statistics, rule scores, tier nesting, quotas, ordering, caps, hashing, rendering |

The model never writes the final watchlist. Operations can be checked one at a time, rejected one
at a time and reversed; a finished list cannot.

## What it guarantees

- **Reproducible.** Policy hash, snapshot `as_of`, universe hash and a machine-readable reason for
  every rejected candidate.
- **Measured, not asserted.** Window-dependent statistics (liquidity, `factor_r2`, beta strength
  and stability) must declare their method, window and source. They cannot be submitted as
  judgement — and `measure` computes them from a price table so the rule has a way to be kept.
- **Judgement, bounded.** `quality` is half rule and half model opinion wherever checkable facts
  exist — listing age, size percentile, a closed list of adverse flags — and the two halves stay
  separately recorded.
- **Low turnover.** Per-depth turnover budgets, hysteresis, flip-flop warnings and a `deferred`
  queue that the next round inherits.
- **Fail closed.** Incomplete facts, stale versions, missing evidence or a failed structural check
  produce nothing at all.

## The command surface

One entry point, eight subcommands, in the order a real session uses them.

| Command | What it is for |
|---|---|
| `taxonomy --market M [--profile P]` | Print the starter theme table to edit, or `--check` one before researching against it |
| `import --watchlist W --market M` | Turn a TradingView export into a snapshot draft instead of retyping it |
| `measure --prices P --benchmark B` | Compute the window statistics the builder refuses to accept as judgement |
| `build --spec S --snapshot N` | Select, rank, cap, validate and write the four artifacts |
| `validate universe.json` | Re-run the structural verdict on any universe file |
| `maintain --universe U --changes C` | Apply a change set against an exact version, under the turnover budget |
| `diff before.json after.json` | Say what actually changed between two universes |
| `evaluate --universe U --prices P` | Measure a universe against the window it lived through — not a backtest |

```bash
python scripts/universe.py build \
  --spec examples/crypto-light/build-spec.json \
  --snapshot examples/crypto-light/snapshot.json \
  --output output
```

## Repository layout

```text
SKILL.md              routing; the agent reads this first
AGENTS.md             the same routing for agents that are not Claude
references/           methodology, tiers, contracts, maintenance, sources, per-market overlays
scripts/universe.py   the only entry point
                      (taxonomy | import | measure | build | maintain | diff | evaluate | validate)
scripts/measure_core.py   window statistics from a local price table, stdlib only
scripts/evaluate_core.py  post-hoc measurement of a universe against its window, stdlib only
scripts/universe_core.py  every mutation and output invariant
assets/               default policy (counts, quotas, turnover budgets, freshness), starter taxonomies, locales
examples/             one Light universe per market, generated from seeds and rebuilt by the test suite
tests/                pytest
docs/media/           README imagery and how to capture it
```

`README.md` is for the human deciding whether to install this. `SKILL.md` is for the agent, and
`references/` is what the agent opens once it knows what it is doing — do not read them to
evaluate the skill, and do not duplicate them here.

## Known limits

Stated plainly, because a limit you cannot see is a defect:

- **No network layer.** The snapshot is the boundary. Whatever fetches the facts, this skill only
  accepts the documented contract. `measure` closes the gap between that rule and a usable
  workflow — it turns a local price table into conforming declarations — but it does not fetch,
  and supplying the table is still the caller's job.
- **Half of `quality` is still judgement**, by design — durability is not a statistic. The rule
  half covers listing age, size percentile and adverse flags, and the two halves are recorded
  separately so nobody has to guess which is which.
- **The constants are still guesses, but they are now checkable.** `evaluate` measures a
  universe against the window it lived through — survival, coverage of the largest moves, the
  cost of each exclusion code, per-theme volatility, per-metric rank correlation, declared
  independence against realised. Nothing in this repository has yet been recalibrated from it:
  one window is one draw, and the numbers in `assets/default-policy.json` are the same judged
  ones they always were.
- **The composite score is an ordinal tie-break**, deliberately. Role order carries the structural
  judgement; the weighted metric score only breaks ties inside a bucket, and nothing downstream
  should read it as a rating.
- **Only Light examples ship.** All three are full size — exactly their market's Light target,
  inside guidance, on quota, zero warnings — but Medium and Heavy have none, because every ticker
  in `examples/seeds/*.tsv` is written from knowledge rather than read off an exchange listing and
  the honest limit of that is about a hundred names. Extending them is a TSV edit, not a code
  change.
- **Every metric value in the examples is illustrative.** The tickers, venues and themes are real;
  the liquidity, beta and factor numbers are shaped to exercise the selection logic, not measured
  off a tape. No example asserts a regulatory status about a real issuer, and none should.
- **Three markets ship reviewed rules** (`cn`, `us`, `crypto`), in one `MARKET_SPECS` table
  rather than in scattered branches. Any other market builds by declaring the same handful of
  facts in the snapshot, under the same evidence gate as everything else — recorded, hashed, and
  reported as declared rather than reviewed on every run. A fourth *registered* market is still a
  code change, and no unexercised market overlay is shipped on speculation. See
  [references/markets/adding-a-market.md](references/markets/adding-a-market.md).
- **Three locales ship** (`en`, `zh-Hans`, `zh-Hant`), and the report is written in the market's
  own language by default. Only the chrome is translated; validation diagnostics stay English
  because they name policy fields and code paths. The language of every above-scale market is
  already decided in the same document, so implementing one does not reopen the question.

## Verifying

```bash
python -m pytest tests -q     # the suite, on a plain checkout
ruff check .                  # lint
python examples/build_examples.py && git diff --exit-code examples/   # the examples still match their seeds
```

CI runs the suite on Python 3.10 through 3.13 and **installs nothing beforehand** — if the
zero-dependency claim ever stops being true, the job fails rather than the claim quietly rotting.
A second job drives the CLI the way a user does: it builds all three markets, validates each
output, re-imports a generated watchlist, checks every starter theme table, applies the example
change set, diffs the result and runs `evaluate` against a synthetic window.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: every change to deterministic logic ships with a
test, contracts in `references/` are agreed before implementation, and the validator is never
weakened to make an output pass.

## Not investment advice

This skill produces an observation universe. It does not provide recommendations, allocations,
return expectations, order instructions or trade execution, and nothing it emits should be treated
as a solicitation to buy or sell anything.

## License

MIT. See [LICENSE](LICENSE).
