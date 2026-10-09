# README images

Captured on 2026-10-09 from the [US Medium example](../../examples/us-medium/),
version `803482441ee9`: 294 company tickers, 44 reference instruments,
51 company themes and 338 exported symbols. Research facts are dated 2026-10-08;
the historical price cutoff is 2026-10-06.

- **[universe-report.jpg](universe-report.jpg)** — a styled excerpt of the generated
  report: three complete themes and their 19 original tickers and short reasons.
  Counts and validation status come from the example's JSON and validation receipt.
  The [HTML presentation source](universe-report.html) is retained for visual edits;
  this presentation is not an additional CLI output or a product dashboard.
- **[tradingview-watchlist.jpg](tradingview-watchlist.jpg)** — a real TradingView
  capture after importing the generated TXT into a separate watchlist, using the
  `Universe Demo` layout. The UI reports 338 symbols and shows the imported theme
  sections. Sharing remains off. Only the viewport's bottom edge is cropped;
  no UI or values were synthesized. Displayed quotes are TradingView's capture-time
  values, not the example's historical measurement inputs. The visible count and
  groups were checked; a full symbol/venue export round trip was not completed.

Both JPEGs are below 1 MB. Use these paths from the root README:

```markdown
![US Medium universe report excerpt](docs/media/universe-report.jpg)
![Generated universe imported into TradingView](docs/media/tradingview-watchlist.jpg)
```
