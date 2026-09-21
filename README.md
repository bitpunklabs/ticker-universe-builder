# Ticker Universe Builder

An agent skill that builds and maintains **auditable ticker universes** for fourteen markets, and
renders them as TradingView-importable watchlists.

[![ci](https://github.com/bitpunklabs/ticker-universe-builder/actions/workflows/ci.yml/badge.svg)](https://github.com/bitpunklabs/ticker-universe-builder/actions/workflows/ci.yml)
[![license: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](pyproject.toml)
[![dependencies: none](https://img.shields.io/badge/dependencies-none-brightgreen.svg)](pyproject.toml)

<!-- MEDIA PLACEHOLDER 1 of 2 — drop docs/media/demo.gif in place, then delete these two
     comment lines so the image below renders. Recording instructions: docs/media/README.md
![The skill building a Medium US universe in OpenClaw, end to end](docs/media/demo.gif)
-->

A ticker universe is an observation instrument, not a recommendation list. This skill exists to
gate it: every member arrives with a role, a reason and dated evidence; every change is an
operation against an exact version; and nothing is written unless the deterministic validator
passes.

## The problem this solves

Ask any capable model for "a list of the 80 most interesting US tickers" and it will produce one
immediately. It will also be unreviewable. Twenty silently dropped names, a reordered section, a
mistyped venue and a company that delisted last quarter all look identical to a correct file, and
the next run — same prompt, same model — produces a different list with no way to say what
changed or why.

The failure is not that the model is bad at picking tickers; research is exactly what it is good
at. It is that a hand-written membership list carries no structure to check: no record of which
theme each name is there to observe, no distinction between a benchmark and a satellite, no
statement of what was rejected, no version to diff against. So this skill splits the job. The
model researches and proposes; Python normalizes, gates, ranks, apportions, hashes and writes.

## Say this

- *"Build me a Light crypto ticker universe for observation, using Binance perpetuals."*
- *"Build a Medium Japan universe with sector breadth, as of today."*
- *"Here's my TradingView watchlist export — turn it into a proper universe snapshot."*
- *"Review my CN universe (universe.json attached) and propose changes under 10% turnover."*
- *"Widen my Light crypto universe to Medium without churning the incumbents."*
- *"Evaluate the universe I built in July against the last 60 days of prices."*

Name the market and the depth (`light` / `medium` / `heavy`). Skip the depth and it defaults to
Medium; skip the market and you will be asked for that and nothing else.

It declines stock tips, position sizing, allocations, entries and exits.

## Markets

Fourteen ship with reviewed rules — venue list, symbol shape, identity rule, adverse-flag
vocabulary, theme table and report language:

| Code | Market | Venues | Report in |
|---|---|---|---|
| `us` | United States | NASDAQ, NYSE, AMEX, ARCA … | English |
| `cn` | China A-shares | SSE, SZSE, BSE | Simplified Chinese |
| `jp` | Japan | TSE | Japanese |
| `in` | India | NSE, BSE | English |
| `hk` | Hong Kong | HKEX | Traditional Chinese |
| `kr` | Korea | KRX | Korean |
| `uk` | United Kingdom | LSE | English |
| `tw` | Taiwan | TWSE, TPEX | Traditional Chinese |
| `de` | Germany | XETR, FWB | German |
| `fr` | France | EURONEXT | French |
| `ca` | Canada | TSX, TSXV | English |
| `au` | Australia | ASX | English |
| `br` | Brazil | BMFBOVESPA | Portuguese |
| `crypto` | Crypto perpetuals | BINANCE | English |

Any other market builds by declaring the same handful of facts in the snapshot, evidence-gated,
hashed, and reported as **declared rather than reviewed** on every run.

Each ships a full-size Light example — [`examples/`](examples/) — in its own language. Tier sizes
follow the market: one `breadth` factor scales the 60 / 160 / 400 tier bases, so US Light is 80
members and Brazil Light is 35. Equity markets share one theme table and state only
their delta — what they do not list, what nobody else lists, and the **weights** that say what
that market is actually about. There is no per-theme cap; slots are apportioned to weight, so
semiconductors in China (3.5) take more of the universe than property developers (0.4). See
[references/tier-profiles.md](references/tier-profiles.md).

## What you get

Four artifacts per build, named `{market}-{profile}-{as_of}`.

A **`.md` report** in the market's own language ([CN example](examples/cn-light/universe.md)):

```markdown
# CRYPTO Ticker Universe

- Profile: Light
- Facts as of: 2026-09-17
- Tickers: 40
- Themes: 15
- Largest theme: 10_A · 4 · 10% · weighted share 5
- Validation: PASS

| Theme | Ticker | Name | Role | Reason | Evidence |
|---|---|---|---|---|---|
| 10_A L1_MAJORS | BINANCE:ADAUSDT.P | Cardano | THEME_LEADER | … | https://api.binance.com/… |
```

A **`.txt` watchlist** TradingView imports directly, sectioned by theme, capped at 1,000 tokens
([crypto example](examples/crypto-light/watchlist.txt)):

```text
###00_A_CORE_ASSETS,BINANCE:ETHUSDT.P,BINANCE:BTCUSDT.P,###10_A_L1_MAJORS,BINANCE:ADAUSDT.P,…
```

<!-- MEDIA PLACEHOLDER 2 of 2 — drop docs/media/watchlist-import.gif in place, then
     delete these two comment lines. Capture instructions: docs/media/README.md
![Importing a generated watchlist into TradingView](docs/media/watchlist-import.gif)
-->

A **`.json` universe** — the version of record, carrying every member, every rejected candidate
with its exclusion code, the policy hash and the content hash. This is the file you keep and pass
back in to maintain. And a **`.validation.json`** — the structural verdict. If it fails, the
other three were never written.

## Install

No dependencies. Python 3.10+ and the standard library.

Releases are semver-tagged; `--branch v0.1.0` pins one, and `main` is always the newest.

```bash
# Claude Code — all projects
git clone https://github.com/bitpunklabs/ticker-universe-builder.git \
  ~/.claude/skills/ticker-universe-builder

# Claude Code — one project
git clone https://github.com/bitpunklabs/ticker-universe-builder.git \
  .claude/skills/ticker-universe-builder
```

For **OpenClaw**, `clawhub install @bitpunklabs/ticker-universe-builder`, or clone into
`~/.openclaw/workspace/skills/`. For **claude.ai**, zip the repository and upload it under
Settings → Capabilities → Skills; the zip must carry `SKILL.md` at its top level. For the **Agent SDK or API**, mount the directory into
the agent's skills path. For **any other agent**, [`AGENTS.md`](AGENTS.md) is the routing and the
scripts are plain Python with no host-specific assumptions.

## How the work is divided

The model researches. Python decides.

| The model supplies | Python owns |
|---|---|
| Themes, weights, roles, evidence, judgement, proposed operations | Normalization, eligibility gates, window statistics, rule scores, tier nesting, quotas, apportionment, ordering, hashing, rendering |

The model never writes the final watchlist. Operations can be checked one at a time, rejected one
at a time and reversed; a finished list cannot.

## What it guarantees

- **Reproducible.** Policy hash, snapshot `as_of`, universe hash, and a machine-readable reason
  for every rejected candidate.
- **Measured, not asserted.** Window-dependent statistics — liquidity, `factor_r2`, beta strength
  and stability — must declare their method, window and source, and cannot be submitted as
  judgement. `measure` computes them from a price table so the rule has a way to be kept.
- **Judgement, bounded.** `quality` is half rule and half model opinion wherever checkable facts
  exist — listing age, size percentile, a closed list of adverse flags — and the halves stay
  separately recorded.
- **Low turnover.** Per-depth turnover budgets, hysteresis, flip-flop warnings, and a `deferred`
  queue the next round inherits.
- **Fail closed.** Incomplete facts, stale versions, missing evidence or a failed structural check
  produce nothing at all.

## The command surface

One entry point, eight subcommands, in the order a real session uses them.

| Command | What it is for |
|---|---|
| `taxonomy --market M [--profile P]` | Print the starter theme table to edit, or `--check` one before researching against it |
| `import --watchlist W --market M` | Turn a TradingView export into a snapshot draft instead of retyping it |
| `measure --prices P --benchmark B` | Compute the window statistics the builder refuses to accept as judgement |
| `build --spec S --snapshot N` | Select, rank, apportion, validate and write the four artifacts |
| `validate universe.json` | Re-run the structural verdict on any universe file |
| `maintain --universe U --changes C` | Apply a change set against an exact version, under the turnover budget |
| `diff before.json after.json` | Say what actually changed between two universes |
| `evaluate --universe U --prices P` | Measure a universe against the window it lived through — not a backtest |

## Repository layout

```text
SKILL.md              routing; the agent reads this first
AGENTS.md             the same routing for agents that are not Claude
references/           methodology, tiers, contracts, maintenance, sources, per-market overlays
scripts/universe.py   the only entry point
scripts/*_core.py     selection, measurement and evaluation; stdlib only
assets/               policy, theme tables (one shared equity base + per-market deltas), locales
examples/             one Light universe per market, generated from seeds and rebuilt by the tests
tests/                pytest
```

`README.md` is for the human deciding whether to install this. `SKILL.md` is for the agent, and
`references/` is what the agent opens once it knows what it is doing.

## Known limits

Stated plainly, because a limit you cannot see is a defect:

- **No network layer.** The snapshot is the boundary. `measure` turns a local price table into
  conforming declarations, but it does not fetch, and supplying the table is the caller's job.
- **Half of `quality` is still judgement**, by design — durability is not a statistic. The rule
  half covers listing age, size percentile and adverse flags, recorded separately.
- **The constants are still guesses, but they are now checkable.** `evaluate` measures a universe
  against the window it lived through. Nothing here has been recalibrated from it yet: one window
  is one draw, and the numbers in `assets/default-policy.json` — breadth factors included — are
  the same judged ones they always were.
- **Theme weights are judgement too, and they are the biggest lever in the system.** They decide
  how the universe is apportioned, and nothing measures them. The report prints where a universe
  concentrated and what the weights asked for, which makes a wrong weight visible, not impossible.
- **The composite score is an ordinal tie-break**, deliberately. Role order carries the structural
  judgement; nothing downstream should read the weighted score as a rating.
- **Only Light examples ship.** All fourteen markets have one, full size and warning-free, but
  Medium and Heavy have none: every ticker in `examples/seeds/*.tsv` is written from knowledge
  rather than read off an exchange listing, and the honest limit of that is sixty to a hundred
  and twenty names per market. Every metric value in the examples is illustrative; no example
  asserts a regulatory status about a real issuer.
- **`fr` cannot enforce its own boundary.** TradingView's `EURONEXT` venue code covers Paris,
  Amsterdam, Brussels and Lisbon alike, so the identity rule cannot tell them apart and the
  research has to. It is stated in the overlay rather than papered over.
- **Eight locales ship.** Only the chrome is translated; validation diagnostics stay English
  because they name policy fields and code paths. A market's adverse-flag vocabulary is
  translated in its own language and in English, and prints as a code elsewhere.

## Verifying

```bash
python -m pytest tests -q     # the suite, on a plain checkout
ruff check .                  # lint
python examples/build_examples.py && git diff --exit-code examples/
```

CI runs the suite on Python 3.10 through 3.13 and **installs nothing beforehand** — if the
zero-dependency claim stops being true, the job fails rather than the claim quietly rotting. A
second job drives the CLI the way a user does: builds all fourteen examples, validates each,
re-imports a generated watchlist, checks every registered market's starter table, applies the
example change set, diffs the result and runs `evaluate` against a synthetic window.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: every change to deterministic logic ships with a
test, contracts in `references/` are agreed before implementation, and the validator is never
weakened to make an output pass.

## Not investment advice

This skill produces an observation universe. It does not provide recommendations, allocations,
return expectations, order instructions or trade execution, and nothing it emits should be treated
as a solicitation to buy or sell anything.

## License

MIT — see [LICENSE](LICENSE).

Published to the OpenClaw registry under **MIT-0**, which is MIT without the attribution
requirement. ClawHub carries no licence field and distributes listings on those terms, so saying
so here is more honest than letting the two disagree quietly. Cloning from GitHub gets you MIT;
installing from ClawHub gets you MIT-0. Both are this repository, offered by its author under
both terms, and MIT-0 asks strictly less of you.
