# Evaluation

Every threshold in this skill is a guess. The guidance ranges, `BETA_FULL_SCALE`, the listing-age
bands, the score weights, the theme weights — all set by judgement, none ever checked against an
outcome. `evaluate` is the only thing here that can change that, and it matters more for a
market whose rules were declared at run time than for one that was reviewed once by a person.

```bash
python scripts/universe.py evaluate \
  --universe crypto-light-2026-09-17.json \
  --prices window.csv \
  --benchmark BINANCE:BTCUSDT.P --benchmark BINANCE:ETHUSDT.P \
  --output evaluation.json
```

`--prices` is the same `date,ticker,close[,volume|turnover]` CSV [measurement.md](measurement.md)
describes, covering the window after the universe was built.

## This is not a backtest

A universe is an observation instrument, not a portfolio, so `evaluate` never computes what the
universe "returned" — that number would be meaningless and would invite exactly the reading the
whole design refuses. The question is whether the instrument saw what happened.

## Make the price table wider than the universe

Coverage is only answerable against a pool larger than the members. At minimum include the
rejected candidates from `selection_audit`; better, the whole eligible list. A table holding only
members reports perfect coverage and tells you nothing, which is why `member_share_of_pool` sits
beside every coverage number.

## What each section is for

| Section | Reads | Recalibrates |
|---|---|---|
| `survival` | members the table cannot see, or that print fewer than 10 bars | the freshness window and the review cadence |
| `coverage` | of the largest absolute moves in the pool, how many the universe held — and names the ones it missed | the per-market guidance ranges: was it wide enough |
| `rejections` | median move of the rejected candidates, **by exclusion code**, and which of them landed in the top cut | the eligibility rules. "Some rejections were expensive" changes nothing; "every candidate dropped for `insufficient_liquidity` was in the top ten" changes a threshold |
| `themes` | realised volatility per theme and its share of the total | the theme weights, and whether the taxonomy put its slots where the market moved |
| `metrics` | Spearman rank correlation of each metric against the realised move and against realised volatility | `SCORE_WEIGHTS` |
| `independence` | declared `independence` against `100 - R²` from an OLS on the benchmark basket | `BETA_FULL_SCALE` and the `INDEPENDENT_SENSOR >= 50` gate |

## Reading it honestly

- **A near-zero correlation is not automatically a bad metric.** `quality` is not supposed to
  predict a move; it is supposed to keep the pool observable. `liquidity` and `heat` are the ones
  where a flat number is a question.
- **Fewer than eight scored members produces `null`, not a number.** A rank correlation over four
  points is noise with a decimal point on it.
- **One window is one draw.** A threshold moved on a single evaluation has been fitted to one
  quarter. Two or three windows, in the same direction, is a finding.
- The output is JSON, not a localised report. It is an input to the next build rather than a
  document to hand to a reader — the universe's own `.md` is that.
