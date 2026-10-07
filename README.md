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
operation against an exact version; and no universe is published unless the deterministic
validator passes. Small Max count-only shortfalls can be delivered with explicit partial status; larger gaps
keep diagnostics and a checkpoint so research can continue.

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

Name the market and the depth (`light` / `medium` / `heavy` / `max`). Skip the depth and it defaults to
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
| `crypto` | Crypto spot/perpetuals | BINANCE default; declare other verified venues | English |

Any other market builds by declaring the same handful of facts in the snapshot, evidence-gated,
hashed, and reported as **declared rather than reviewed** on every run.

CN, US and Crypto ship current [worked examples](examples/README.md), with a Crypto Heavy→Max
seed example. All new builds use a [coverage-first research plan](references/coverage-plan.md):
stable economic branches, a reviewed leader/necessary-peer roster, parent-sector ceilings,
instrument bindings and auditable Core migration. Archived replay requires an explicit policy
in `assets/legacy-policy.json`.

Light is leader-only. Medium covers most reviewed leaders. Heavy completes the necessary
backbone plus at most 20% satellites; Max expands that same qualified Heavy with at most
35% satellites overall, and must add at least 30% to Heavy's entity count entirely as qualified Beta.
Coverage Beta means supplementary business/token coverage, ranked by sourced market cap; price
beta, R² and stability are auxiliary measurements, not admission floors. Legacy high-beta replay
retains its statistical gates.
Entity budgets are ceilings; under-expansion retains a research checkpoint. A small count-only
gap may be delivered as explicit partial under the recovery contract, never complete. Unused
capacity above the minimum is allowed, and padding is never allowed.
Reference indices, rates and other gauges are exported separately from entity budgets in the same TXT.
Display theme weights and news heat do not allocate economic coverage.

## What you get

`build` and `maintain` write to the explicit `--output DIR`. The agent's default convention is
`ticker-universes/<market>/<profile>/<as_of>/` inside the user's project; the CLI does not choose
an implicit destination. Files use `{market}-{profile}-{as_of}` as their stem.

| File | Use |
|---|---|
| `.json` | Authoritative universe, coverage/admissions, dated facts, sources, rejections and hashes; keep for maintenance |
| `.validation.json` | Qualification, errors/warnings, counts and coverage/expansion checks |
| `.txt` | Grouped TradingView import, including references, at most 1,000 tokens |
| `.en.md` | Readable report |
| `.<market-language>.md` | Companion for non-English markets, e.g. `.zh-Hans.md` for CN |

**US/Crypto: four files; CN: five.** See the
[CN report](examples/cn-medium/output/cn-medium-2026-10-07.zh-Hans.md) and
[Crypto TXT](examples/crypto-medium/output/crypto-medium-2026-10-07.txt).

The CLI prints a JSON receipt with artifact paths and creates `DIR.run/` with saved inputs,
attempts and repair diagnostics. A resumed attempt uses a fresh destination; existing outputs
are never overwritten. Partial files include `-partial` in their names. The
[standard output contract](references/output-artifacts.md) documents paths, receipts, formats
and delivery statuses.

<!-- MEDIA PLACEHOLDER 2 of 2 — capture instructions: docs/media/README.md
![Importing a generated watchlist into TradingView](docs/media/watchlist-import.gif)
-->

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
| Economic plan, leader/peer roster, admissions, business evidence, sourced caps, proposed operations | Normalization, eligibility gates, window statistics, protected coverage, sector/satellite ceilings, apportionment, ordering, hashing, rendering |

The model never writes the final watchlist. Operations can be checked one at a time, rejected one
at a time and reversed; a finished list cannot.

## What it guarantees

- **Reproducible.** Policy hash, snapshot `as_of`, universe hash, and a machine-readable reason
  for every rejected candidate.
- **Measured, not asserted.** Window-dependent statistics — liquidity, `factor_r2`, beta strength
  and stability — must declare their method, window and source, and cannot be submitted as
  judgement. `measure` computes them from a price table so the rule has a way to be kept.
- **Coverage before depth.** The reviewed backbone is protected before optional Beta. Beta uses
  complementary business/token exposure and sourced market cap within Heavy's distribution.
  Supplied measurements retain their provenance; missing optional price statistics are not invented.
- **Low turnover.** Per-review-depth turnover budgets, flip-flop warnings, and a `deferred`
  queue the next round inherits.
- **Fail closed.** Incomplete facts, stale versions, missing evidence or a failed structural check
  block publication. Build attempts retain their inputs and repair diagnostics. Resume with
  `build --resume OUTPUT.run`. Coverage-first accepts unused capacity only after all quality
  gates pass; explicit small Max count-only shortfalls are `partial` (exit 3). See [recovery](references/recovery.md).

## The command surface

One entry point, ten subcommands, in the order a real session uses them.

| Command | What it is for |
|---|---|
| `taxonomy --market M [--profile P]` | Print the starter theme table to edit, or `--check` one before researching against it |
| `audit-core --watchlist W --universe U` | Preserve the Core and create exact-code research decisions |
| `import --watchlist W --market M` | Turn a TradingView export into a snapshot draft instead of retyping it |
| `fetch --market M --prices-until D --output O` | Optional public listings/history adapter; writes receipts and coverage, never membership |
| `measure --prices P --benchmark B` | Compute the window statistics the builder refuses to accept as judgement |
| `build --spec S --snapshot N` | Select, rank, apportion, validate and write the standard artifact bundle |
| `validate universe.json` | Re-run the structural verdict on any universe file |
| `maintain --universe U --changes C` | Apply a change set against an exact version, under the turnover budget |
| `diff before.json after.json` | Say what actually changed between two universes |
| `evaluate --universe U --prices P` | Measure a universe against the window it lived through — not a backtest |

## Repository layout

```text
SKILL.md              routing; the agent reads this first
AGENTS.md             repository-specific entry point and boundaries
references/           methodology, tiers, contracts, maintenance, sources, per-market overlays
scripts/universe.py   the only entry point
scripts/*_core.py     selection, measurement and evaluation; stdlib only
assets/               policy, theme tables (one shared equity base + per-market deltas), locales
examples/             CN/US/Crypto Medium and Crypto Heavy/Max, rebuilt from dated snapshots
tests/                pytest
```

`README.md` is for the human deciding whether to install this. `SKILL.md` is for the agent, and
`references/` is what the agent opens once it knows what it is doing.

## Known limits

Stated plainly, because a limit you cannot see is a defect:

- **Optional data adapters.** Public TradingView/Yahoo and Binance adapters write raw receipts.
  Endpoints can fail or change; incomplete requests are disclosed. Build and measure remain offline.
  See [provider scope](references/providers.md). A verified quote is not regulatory due diligence.
- **Leadership is researched judgement.** Validation checks sourced admissions and a declared
  roster; it does not independently certify business leadership or market-wide completeness.
  Optional legacy quality blends remain separately recorded; they do not rank coverage Beta.
- **Coverage constraints are declared policy.** Leader coverage, satellite ceilings, minimum
  expansion and sector budgets are transparent starting rules, not empirically optimal weights.
- **Worked examples are dated research subsets.** Their cutoffs, source scope and optional
  measurements remain visible; offline replay does not establish real-time data freshness or
  prove that the universe discovers every important move.

## Verifying

```bash
python -m pytest tests -q     # the suite, on a plain checkout
ruff check .                  # lint
python examples/build_examples.py && git diff --exit-code examples/
```

CI runs the suite on Python 3.10 through 3.13 with pytest; runtime scripts use only the standard
library. A second job drives the CLI: builds all current examples, including seeded Max, validates each,
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
