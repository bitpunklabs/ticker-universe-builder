# Crypto overlay

## Universe boundary

V1 uses Binance as the trading boundary:

1. Active USDⓈ-M USDT perpetual contracts;
2. Active Binance Spot USDT pairs;
3. When both exist, prefer the perpetual if it has continuous sessions and clears the 30-day
   notional floor, otherwise the spot pair. The same base asset never enters twice.
4. Delisted assets, delivery-only contracts, leveraged tokens, stablecoins themselves and anything
   without confirmable continuous trading are excluded by default.

Other venues can serve as theme or price evidence, but they do not widen the final ticker universe.
That keeps venue, turnover and maintainability consistent after the user imports the file.

## Why the count is so much smaller

Most altcoin returns are explained by BTC, ETH, SOL and a handful of sector factors. A highly
correlated token with no independent event, liquidity or ecosystem role does not add enough
information to justify a slot. Effective capacity is set by qualified high-turnover assets times
independent drivers, not by the number of tokens in existence.

## Build order

1. Market anchors — BTC, ETH, SOL.
2. Liquidity leaders of the core sectors.
3. Independent sensors that still leave residual information against the three factors.
4. High-turnover, high-beta sector satellites.
5. Recent heat or new listings, inside a strict tactical budget.

Recent heat can only enter as `LIQUIDITY_SENSOR` or `NEW_LISTING`. A price move alone never makes
a `THEME_LEADER`.

## Liquidity and redundancy gates

- Use cross-sectional percentiles of Binance 7-day and 30-day USDT quoted volume and notional,
  not a fixed dollar figure that ages badly.
- Light applies the strictest percentile gate, Medium the next; Heavy still holds a continuous-
  trading floor.
- Check effective trading days, zero-volume sessions, suspicious flat lines, contract and spot
  status, and listing age.
- Regress each member on BTC/ETH/SOL over 30 / 90 / 180 days and read beta, R² and residual
  volatility. Take the factors from the universe's own `00_A` theme rather than hardcoding them —
  `00_A` is the single declaration of what this market's rulers are.
- A very high R² with no independent theme role is a downgrade; a low R² with insufficient
  turnover is still not admissible.
- Confirm heat with a turnover jump, open interest or a verifiable theme event — never with a
  single day's price change.

## A note on measurement thresholds

Do not import an R² threshold from a document without testing it against this universe. A rule
calibrated elsewhere can easily sit above every value the market actually produces, in which case
it never fires and the universe is governed by a rule that does nothing. Measure the distribution
first, then set the gate.

## Measurement history and new tokens

Any regression-based gate requires history, so maintaining "by measurement" alone biases a universe
toward old tokens. A recently listed asset is admitted on standards that do not depend on history —
tradability, continuous sessions, order-book depth, ecosystem role, a dated event — and enters the
tactical budget as `NEW_LISTING`, not by loosening the retention rules for everyone else.

## Example

[`examples/crypto-light/`](../../examples/crypto-light/) is a full-size Light universe for this market: the seed table it is built from, the snapshot, the report in this market's language, and the TradingView watchlist. Every metric value in it is illustrative; the tickers, themes and roles are not.
