# CN overlay

Read [equity-common.md](equity-common.md) first: the universe boundary, the fund-versus-basket
redundancy test, the cash-management exclusion and the rule about regressing against the
theme rather than the index are the same in every equity market.

## Universe boundary

- Shanghai, Shenzhen and Beijing listings plus the indices and ETFs needed as gauges, all
  expressible in TradingView.
- A common share must have a confirmed six-digit code, the correct venue and a normal, tradable
  listing state.
- ST and \*ST names, delisting-transition names, long-halted names, names whose identity cannot be
  confirmed, and names without recent effective turnover are excluded by default.
- The venue is part of CN identity: `SSE:000001` and `SZSE:000001` are different instruments, so
  the default `asset_id` keeps the venue prefix.
- ETFs and single names are compared separately. ETFs carry structural gauges; single names carry
  company and supply-chain information.
- The report is written in Simplified Chinese, so write the snapshot in Simplified Chinese:
  `name` is the listed short name (`贵州茅台`, not `Kweichow Moutai`), and `l1_name`, `reason`
  and every `measurement.method` are Chinese prose. Theme codes and `theme_name` stay ASCII —
  they are identifiers that have to survive a TradingView import.

## Build focus

- Light: broad and style gauges, first-level sectors, core policy and industrial themes, and the
  most representative leaders.
- Medium: the major second-level themes, quality leaders, upstream and downstream positions, and a
  limited set of high-beta sensors.
- Heavy: mid-cap structural representatives, non-consensus sectors, turnover breadth, quantitative
  independent components and qualified new listings.

Do not let short-term heat decide a permanent taxonomy. A policy change can raise research
priority; it does not replace listing, turnover and industrial-relationship evidence.

## A size and turnover floor comes before any other judgement

Below a minimum fund size and daily turnover, the instrument's own price series is too noisy to
read a signal from — the spread alone moves the daily bar. Such a name is not "slightly worse
coverage", it is a **false sector anchor**: it will be quoted as if it represented its sector.

The only defensible exception is a theme's sole pure-play leader, and that exception is recorded
with its reason.

## Cash-management instruments

Short-term financing bond ETFs and money-market funds are excluded by instrument type. They post
the largest turnover in the entire ETF market, the tightest spreads and the best tracking, so every
quality ranking puts them first — which is exactly why the exclusion has to be written down rather
than left to whoever happens to be reviewing.

## Example

[`examples/cn-light/`](../../examples/cn-light/) is a full-size Light universe for this market: the seed table it is built from, the snapshot, the report in this market's language, and the TradingView watchlist. Every metric value in it is illustrative; the tickers, themes and roles are not.

## Suggested live fields

- Listing, risk-warning and halt status.
- 20-day and 60-day turnover percentiles.
- 63 / 126 / 252-day beta, R² and downside beta against the theme's own ETF or theme leader.
- Relative return, max drawdown and residual volatility.
- The update time of sector, core-business and theme evidence.
