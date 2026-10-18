# Global: bounded five-market pilot

This is a reproducible composition example, not a completed worldwide leadership screen.
It reuses qualified dated CN/US/JP/HK/KR worked sources and three index identities read on
2026-10-18. Company research, listing and measurement dates remain inherited. The default
pilot has sixteen companies and five direct index references; it contains no ETF because the
older examples' fund fields do not satisfy the new Global fund evidence contract.

```bash
# Only needed if native example output directories are missing:
python examples/build_examples.py

python examples/global/build_example.py --output temp/global-pilot
python scripts/universe.py validate-global \
  temp/global-pilot/bundle/global-2026-10-18.json \
  --contract temp/global-pilot/inputs/coverage-contract.json
python scripts/universe.py check-watchlist \
  temp/global-pilot/bundle/global-2026-10-18.txt --ticker-only
```

Use a new output destination when rerunning. The pilot is tied to the stated source dates;
replaying it preserves those dates, not today's market facts. `build_example.py` authors research
inputs and calls the maintained composition engine; it never writes final watchlists itself.
Output sources are portable byte-preserved copies.

An optional `--fund-catalog PATH` adds an independently researched `NASDAQ:SOXX` reference and
requires it in the pilot contract. That catalog must satisfy every [Global fund gate](../../references/global.md).
Missing histories, full holdings or dated costs/spreads block publication. Synthetic adverse
ETF cases live in the tests and do not become market-research records. Neither this bounded
pilot nor those tests establish live TradingView import or complete Global coverage.

## Reviewed Core companion

```bash
python examples/global/build_example.py --output temp/global-core-pilot --with-core
python scripts/universe.py validate-global-core \
  temp/global-core-pilot/core-bundle/global-core-2026-10-18.json \
  --contract temp/global-core-pilot/inputs/core-review.json
```

This bounded example reviews all parent tickers and themes, then keeps SK hynix as the direct
memory representative while Samsung remains full-only additional depth. Default full/Core
counts are 21/20, or 22/21 with the optional qualified SOXX catalog. All original pilot duties
remain mandatory. The portable Core bundle revalidates its complete copied parent and native
sources. It is a worked [Core contract](../../references/global-core.md), not an automatically
generated production selection or a finding that one company has better returns.
