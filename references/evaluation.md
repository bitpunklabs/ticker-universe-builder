# Evaluation

Evaluate observation coverage over a **forward** window, not portfolio returns. Design thresholds
are judgement-based; repeated evaluations can inform revisions, but one window does not calibrate them.

```bash
python scripts/universe.py evaluate --universe universe.json --prices window.csv \
  --benchmark BINANCE:BTCUSDT.P --benchmark BINANCE:ETHUSDT.P --output evaluation.json
```

Use the [measurement CSV shape](measurement.md). Only bars strictly after the universe `as_of`
enter; no forward bars is an error. Include rejected candidates or a wider eligible pool:
a member-only table cannot measure missed coverage. `member_share_of_pool` discloses this denominator.

| Section | Measures |
|---|---|
| `survival` | Missing members and histories with fewer than 10 bars |
| `coverage` | Membership among the pool's largest absolute moves and missed names |
| `rejections` | Realized moves grouped by exclusion code |
| `themes` | Theme volatility and its share of the total |
| `metrics` | Spearman correlation with realized moves/volatility; historical score diagnostics |
| `independence` | Declared independence versus measured `100 - R²` on the benchmark basket |
| `redundancy` | Most-correlated member pairs |

Fewer than eight scored members yields `null` rank correlations. Near-zero correlation does not
make a business-quality metric wrong; it is not necessarily a return predictor. Correlated pairs
prompt business review rather than automatic removal. Pair checks set aside flat histories and
members covering less than half the window instead of shortening every pair's calendar.

Output is JSON for subsequent research. Assess several windows before changing a rule;
current coverage selection does not use the legacy composite score weights.
