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
python scripts/universe.py build    --spec S --snapshot N --output DIR [--seed universe.json]
python scripts/universe.py maintain --universe U --changes C --output DIR
python scripts/universe.py validate universe.json
python -m pytest tests -q
```

## How the work is divided

The model researches. Python decides.

| The model supplies | Python owns |
|---|---|
| Taxonomy, roles, evidence, proposed operations | Normalization, eligibility gates, tier nesting, quotas, ordering, caps, hashing, rendering |

The model never writes the final watchlist. A hand-written membership list cannot be reviewed:
twenty silently dropped names, a reordered section and a mistyped venue all look identical to a
correct file. Operations can be checked one at a time, rejected one at a time and reversed.

## What it guarantees

- **Reproducible.** Policy hash, snapshot `as_of`, universe hash and a machine-readable reason for
  every rejected candidate.
- **Measured, not asserted.** Window-dependent statistics (liquidity, `factor_r2`, beta strength
  and stability) must declare their method, window and source. They cannot be submitted as
  judgement.
- **Low turnover.** Per-depth turnover budgets, hysteresis, flip-flop warnings and a `deferred`
  queue that the next round inherits.
- **Fail closed.** Incomplete facts, stale versions, missing evidence or a failed structural check
  produce nothing at all.

## Layout

```text
SKILL.md              routing; read first
references/           methodology, tiers, contracts, maintenance, sources, per-market overlays
scripts/universe.py   the only entry point (build | maintain | validate)
scripts/universe_core.py  every mutation and output invariant
assets/               default policy (counts, quotas, turnover budgets, freshness)
examples/             one working universe per market, rebuilt by the test suite
tests/                pytest
```

## Known limits

Stated plainly, because a limit you cannot see is a defect:

- **No network layer.** The snapshot is the boundary. Whatever fetches the facts, this skill only
  accepts the documented contract.
- **No evaluation loop.** Nothing here measures whether a universe was good after the fact, so the
  guidance ranges in `references/tier-profiles.md` remain an initial calibration rather than
  something recalibrated from outcomes.
- **The composite score is an ordinal tie-break**, deliberately. Role order carries the structural
  judgement; the weighted metric score only breaks ties inside a bucket, and nothing downstream
  should read it as a rating.
- **Three markets are hardcoded** (`cn`, `us`, `crypto`) along with their venue rules. A fourth
  market is a code change, not a policy change.

## Not investment advice

This skill produces an observation universe. It does not provide recommendations, allocations,
return expectations, order instructions or trade execution, and nothing it emits should be treated
as a solicitation to buy or sell anything.

## License

MIT. See [LICENSE](LICENSE).
