# Measuring the window statistics

Four metrics cannot be submitted as judgement — `liquidity`, `factor_r2`, `beta_strength` and
`beta_stability`. A model that has not run the computation does not have the number, and a
filled-in guess is indistinguishable from a measured one once it is in the file.

That rule is only honest if there is a legal way to satisfy it. `measure` is that way.

```bash
python scripts/universe.py measure \
  --prices prices.csv \
  --benchmark BINANCE:BTCUSDT.P --benchmark BINANCE:ETHUSDT.P \
  --source https://data.binance.vision/ \
  --window 180 --liquidity-window 30 \
  --into snapshot.json \
  --output snapshot.measured.json
```

## What it reads

A CSV of daily bars. Long format, one row per ticker per session:

```text
date,ticker,close,turnover
2026-09-15,BINANCE:BTCUSDT.P,62140.0,18400000000
```

`date`, `ticker` and `close` are required. Turnover comes from a `turnover` column if present,
otherwise from `close` × `volume`; without either, the ticker gets no liquidity score rather than
a low one. Where the file came from is not the same as where the data came from, so `--source`
takes the http(s) URL of the provider and lands in every declaration the command writes.

## What it computes

| Metric | Definition |
|---|---|
| `liquidity` | Cross-sectional percentile of mean daily turnover over `--liquidity-window` sessions |
| `factor_r2` | R² of an OLS of daily returns on the benchmark basket over `--window` sessions |
| `beta_strength` | Absolute OLS beta, scaled so beta 2.0 reads 100 |
| `beta_stability` | Agreement of the beta estimate across the two halves of the window |

`--benchmark` repeats to form an equal-weighted factor basket, which is what "the BTC/ETH/SOL
factor" means in the Crypto overlay. Liquidity is a percentile because the score has to be
comparable inside one market and is meaningless across markets.

Stability is a separate question from strength on purpose: a satellite whose beta halves between
the first and second half of the window is not a stable read on the factor, however large either
estimate was.

A series with fewer than 30 sessions overlapping the benchmark gets no factor statistics and one
line in `notes` saying so. Nothing is estimated to fill the gap.

## What it writes

Without `--into`, a bundle: `metrics` keyed by ticker plus the `measurement` declarations.

With `--into`, the same bundle folded into a researched snapshot, written to `--output` — never
back over the input, because the snapshot is the agent's work and this command only contributes
four of its fields. Judged metrics are left exactly as they were. `independence` is dropped from
the candidates because the builder derives it from `factor_r2`, so the two cannot contradict each
other. Any candidate the price table does not cover is listed in `notes`, and the build will
still refuse it for the metric it never received — which is the correct outcome, and the reason
the note exists.

## What it is not

Not a data layer. It does not fetch, does not know about providers, does not clean, and takes no
view on what the numbers mean. Fetching prices is outside this skill; turning a local table into
declarations that survive the validator is inside it.

## Afterwards

The same price table format is what [evaluation.md](evaluation.md) reads to measure a universe against
the window it lived through. `measure` fills a snapshot in; `evaluate` checks what the numbers
turned out to be worth.
