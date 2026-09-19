# Ticker Universe Builder

An agent skill that builds and maintains **auditable ticker universes** for CN, US and Crypto
markets, and renders them as TradingView-importable watchlists.

A ticker universe is an observation instrument, not a recommendation list. This skill exists to
gate it: every member arrives with a role, a reason and dated evidence; every change is an
operation against an exact version; and nothing is written unless the deterministic validator
passes.

## Install

Copy this directory into your agent's skills folder. It needs Python 3.10+ and **no dependencies** —
the standard library only.

```bash
python scripts/universe.py taxonomy --market M [--profile P]
python scripts/universe.py import   --watchlist W --market M --output snapshot.draft.json
python scripts/universe.py measure  --prices P --benchmark B --source URL --output M [--into S]
python scripts/universe.py build    --spec S --snapshot N --output DIR [--seed universe.json]
python scripts/universe.py maintain --universe U --changes C --output DIR
python scripts/universe.py validate universe.json
python -m pytest tests -q
```

## How the work is divided

The model researches. Python decides.

| The model supplies | Python owns |
|---|---|
| Themes, roles, evidence, judgement, proposed operations | Normalization, eligibility gates, window statistics, rule scores, tier nesting, quotas, ordering, caps, hashing, rendering |

The model never writes the final watchlist. A hand-written membership list cannot be reviewed:
twenty silently dropped names, a reordered section and a mistyped venue all look identical to a
correct file. Operations can be checked one at a time, rejected one at a time and reversed.

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

## Layout

```text
SKILL.md              routing; read first
references/           methodology, tiers, contracts, maintenance, sources, per-market overlays
scripts/universe.py   the only entry point
                      (taxonomy | import | measure | build | maintain | diff | evaluate | validate)
scripts/measure_core.py   window statistics from a local price table, stdlib only
scripts/evaluate_core.py  post-hoc measurement of a universe against its window, stdlib only
scripts/universe_core.py  every mutation and output invariant
assets/               default policy (counts, quotas, turnover budgets, freshness), starter taxonomies, locales
examples/             one Light universe per market, generated from seeds and rebuilt by the test suite
tests/                pytest
```

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

## Not investment advice

This skill produces an observation universe. It does not provide recommendations, allocations,
return expectations, order instructions or trade execution, and nothing it emits should be treated
as a solicitation to buy or sell anything.

## License

MIT. See [LICENSE](LICENSE).
