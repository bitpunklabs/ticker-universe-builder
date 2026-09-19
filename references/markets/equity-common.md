# Equity markets — the part that is the same everywhere

Read this once, then read the one overlay for the market you were asked about. Eleven of the
fourteen registered markets are ordinary listed-equity markets, and repeating this in eleven
files would mean a correction landing in one of them and not the other ten.

## Universe boundary

- Common stock, plus the index and sector funds needed as gauges. Warrants, rights, units,
  preferred lines, shells and pre-revenue listings without a confirmed quote are excluded by
  default.
- Confirm the TradingView venue, an active listing and enough turnover to trade the position the
  universe implies — not the position the user holds. This is an observation instrument.
- Never treat two lines of one economic entity as two information sources: a dual share class, a
  local line and its ADR or GDR, a company listed on two venues of the same market. One of them
  is the member and the rest belong in the audit as `duplicate_asset`.

## Funds and single names compete for the same seats

A sector fund covering a theme the universe already holds through several single names may be a
low-information copy of a basket it already owns. Test it: build an equal-weighted,
daily-rebalanced basket from the members that cover the fund's mandate and ask two questions —
does the basket track the fund, and does it beat it over both a one-year and a two-year leg? Both
yes means the fund is redundant. Failure to track means it is an independent factor and stays,
however redundant its holdings look on paper.

Daily rebalancing is not a detail: a buy-and-hold basket silently becomes a bet on its best
member, and the excess return you then measure belongs to that one name rather than to coverage.

Before deleting on that test, drop the basket's largest contributor and recompute. A conclusion
that rests on a single name is a conclusion about that name.

## Cash-management instruments

Money-market, ultra-short and cash-management funds win every liquidity test in the market and
carry no observable signal. They are excluded by instrument type, not scored. This has to be
stated as a rule, because any ranking built on AUM, turnover, spread and tracking quality will
otherwise rank them first.

## Measure against the theme, not against the index

Regress a member against **its own sector or theme gauge**, never against the broad index. A
broad-index regression makes every semiconductor a high-beta winner and credits the sector's move
to each component's alpha. Where a market has no investable sector fund, build the gauge as an
equal-weighted basket of that theme's own members and say so in `measurement.method`.

## Suggested live fields

- Listing and quote status; 20 and 60-session turnover in the local currency.
- Beta, downside beta, R², excess return, volatility and max drawdown against the theme's gauge.
- Beta stability across 63 / 126 / 252 sessions.
- Sector-appropriate quality fields, not one threshold applied across every industry.
- Results dates, regulatory filings or fund holdings as evidence.

Public sector classifications routinely place companies with entirely different drivers in one
bucket. When the classification is ambiguous, map ticker by ticker and record the reason; never
let a wrong sector label decide the theme.

## Weights are the market's opinion of itself

Every theme in the starter table carries a `weight`, and the slots left after each theme has its
first member are apportioned to it. This is where a market says that semiconductors matter more
to it than property development does — and where a stale table says a market still looks the way
it did five years ago. Revisit the weights before the tickers: a weight is one number and it
moves dozens of members.

## The language of the report

The `.md` report is written in the market's own language by default. That means the snapshot has
to be written in that language too — `name` is the listed short name as the market prints it,
and `reason`, `l1_name` and every `measurement.method` are prose in the same language. Theme
codes and `theme_name` stay ASCII: they are identifiers that have to survive a TradingView
import.
