# CRYPTO Ticker Universe

- Profile: Medium
- Facts as of: 2026-09-29
- Version: `9448c7e93933`
- Tickers: 105
- Themes: 13
- Stability: 0.98 · 103 / 105 · ±1%
- Partially scored: 105 / 105
- Largest theme: 14_A · 18 · 17% · weighted share 16
- TradingView tokens: 118 / 1000
- Rejected or unselected candidates: 144
- Validation: PASS

- Real observations acquired 2026-09-29; completed prices through 2026-09-28. This is a disclosed research subset, not a complete market screen.
- Price requests: 280; received: 261; unavailable/excluded: 19. Candidates use successful verified rows only.
- Role leaders use observed size (equities) or turnover (crypto). No synthetic quality or heat score; incomplete scoring and bucket warnings are retained.
- Weights are sqrt(researched theme membership), median-normalised and clipped to 0.5..4; this is an observation budget judgement, not an investment weight.
- Binance product tags classify the research bench; membership is selected later.
- Perpetual preferred only after history and $1m 30d notional floor; spot fallback.
- 180 effective days required for this measured example; new listings excluded.
- Factor R² uses joint BTC/ETH/SOL OLS; beta strength/stability refer to their equal-weight return basket. Product tags are broad categories, not detailed protocol economics.

## Roles

| Role | Count |
|---|---:|
| BENCHMARK | 3 |
| INDEPENDENT_SENSOR | 90 |
| THEME_LEADER | 12 |

## Themes

| Code | Group | Theme | Level | Weight | Count |
|---|---|---|---:|---:|---:|
| 00_A | Market gauges | CORE_GAUGES | 1 | 0.5 | 3 |
| 10_A | Ai | AI | 1 | 1.24 | 11 |
| 11_A | Real World Assets | REAL_WORLD_ASSETS | 1 | 0.99 | 9 |
| 12_A | Storage | STORAGE | 1 | 0.5 | 3 |
| 13_A | Payments | PAYMENTS | 1 | 0.68 | 6 |
| 14_A | Defi | DEFI | 1 | 1.96 | 18 |
| 15_A | Gaming | GAMING | 1 | 1.01 | 9 |
| 16_A | Nft | NFT | 1 | 0.63 | 6 |
| 17_A | Meme | MEME | 1 | 1.01 | 9 |
| 18_A | Fan Tokens | FAN_TOKENS | 1 | 0.5 | 1 |
| 19_A | Layer1 Layer2 | LAYER1_LAYER2 | 1 | 1.62 | 15 |
| 20_A | Infrastructure | INFRASTRUCTURE | 1 | 1.35 | 13 |
| 23_A | Mining | MINING | 1 | 0.5 | 2 |

## How the metrics were produced

| Metric | Basis | Method | Window |
|---|---|---|---|
| beta_stability | measured | agreement of the beta estimate across the two halves of the 180d window | 180d |
| beta_strength | measured | positive OLS beta against BINANCE:BTCUSDT.P + BINANCE:ETHUSDT.P + BINANCE:SOLUSDT.P, scaled so beta 2.0 reads 100 | 180d |
| factor_r2 | measured | multivariate OLS with intercept on BINANCE:BTCUSDT.P + BINANCE:ETHUSDT.P + BINANCE:SOLUSDT.P | 180d |
| independence | measured | derived as 100 - factor_r2 by the builder | 180d |
| liquidity | measured | cross-sectional percentile of mean daily turnover over 30 sessions | 30d |

## Why candidates did not make it

| Reason | Count |
|---|---:|
| not_selected_under_budget | 144 |

## Warnings

- 13 themes have no declared observation duty; legacy presence-only coverage applies
- satellite bucket holds 86% of the pool against a 25% target

## Members

| Theme | Ticker | Name | Role | Reason | Evidence |
|---|---|---|---|---|---|
| 00_A CORE_GAUGES | BINANCE:BTCUSDT.P | Bitcoin | BENCHMARK | Retained market/style gauge; observed active quotation and adjusted history. Broad market/style gauge | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 00_A CORE_GAUGES | BINANCE:ETHUSDT.P | Ethereum | BENCHMARK | Retained market/style gauge; observed active quotation and adjusted history. Broad market/style gauge | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 00_A CORE_GAUGES | BINANCE:SOLUSDT.P | Solana | BENCHMARK | Retained market/style gauge; observed active quotation and adjusted history. Broad market/style gauge | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:WLDUSDT.P | Worldcoin | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:NILUSDT.P | Nillion | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:ALLOUSDT.P | Allora | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:PHAUSDT.P | Phala.Network | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:KAITOUSDT.P | Kaito | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:0GUSDT.P | 0G | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:KITEUSDT.P | KITE | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:ROBOUSDT.P | Fabric Protocol | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:NMRUSDT.P | Numeraire | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:SAHARAUSDT.P | Sahara AI | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 10_A AI | BINANCE:SENTUSDT.P | Sentient | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: AI | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:AVAXUSDT.P | Avalanche | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:ONDOUSDT.P | Ondo | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:EDENUSDT.P | OpenEden | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:ICPUSDT.P | Internet Computer | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:CFGUSDT.P | Centrifuge | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:PLUMEUSDT.P | PLUME | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:SKYUSDT.P | Sky | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:BBUSDT.P | BounceBit | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 11_A REAL_WORLD_ASSETS | BINANCE:SYRUPUSDT.P | Maple Finance | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: RWA | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 12_A STORAGE | BINANCE:FILUSDT.P | Filecoin | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: storage-zone | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 12_A STORAGE | BINANCE:ARUSDT.P | Arweave | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: storage-zone | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 12_A STORAGE | BINANCE:SCUSDT | Siacoin | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: storage-zone | https://api.binance.com/api/v3/exchangeInfo |
| 13_A PAYMENTS | BINANCE:ZECUSDT.P | Zcash | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: Payments | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 13_A PAYMENTS | BINANCE:COTIUSDT.P | COTI | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Payments | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 13_A PAYMENTS | BINANCE:DASHUSDT.P | Dash | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Payments | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 13_A PAYMENTS | BINANCE:HUMAUSDT.P | Huma Finance | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Payments | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 13_A PAYMENTS | BINANCE:LTCUSDT.P | Litecoin | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Payments | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 13_A PAYMENTS | BINANCE:ACHUSDT.P | Alchemy Pay | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Payments | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:HYPEUSDT.P | Hyperliquid | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:FFUSDT.P | Falcon Finance | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:WLFIUSDT.P | World Liberty Financial | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:BANKUSDT.P | Lorenzo Protocol | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:DEXEUSDT.P | DeXe | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:ENAUSDT.P | Ethena | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:KATUSDT.P | Katana | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:HOMEUSDT.P | Defi App | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:REZUSDT.P | Renzo | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:ASTERUSDT.P | Aster | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:JTOUSDT.P | JITO | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:FORMUSDT.P | Four | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:MORPHOUSDT.P | Morpho Token | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:JSTUSDT.P | JUST | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:ORCAUSDT.P | Orca | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:SPKUSDT.P | Spark | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:OPNUSDT.P | OPINION | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 14_A DEFI | BINANCE:CRVUSDT.P | Curve | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: defi | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:ACEUSDT.P | Fusionist | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:ENJUSDT.P | Enjin Coin | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:AXSUSDT.P | Axie Infinity | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:XAIUSDT.P | Xai | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:ALICEUSDT.P | My Neighbor Alice | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:NOTUSDT.P | Notcoin | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:GUNUSDT.P | GUNZ | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:HMSTRUSDT.P | Hamster Kombat | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 15_A GAMING | BINANCE:AGLDUSDT.P | Adventure Gold | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Gaming | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 16_A NFT | BINANCE:PENGUUSDT.P | Pudgy Penguins | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: NFT | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 16_A NFT | BINANCE:APEUSDT.P | ApeCoin | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: NFT | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 16_A NFT | BINANCE:TNSRUSDT.P | Tensor | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: NFT | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 16_A NFT | BINANCE:CHZUSDT.P | Chiliz | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: NFT | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 16_A NFT | BINANCE:GMTUSDT.P | Green Metaverse Token | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: NFT | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 16_A NFT | BINANCE:MEUSDT.P | Magic Eden | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: NFT | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:DOGEUSDT.P | Dogecoin | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:MUBARAKUSDT.P | Mubarak | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:TUTUSDT.P | Tutorial | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:GIGGLEUSDT.P | Giggle Fund | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:ORDIUSDT.P | ORDI | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:TSTUSDT.P | Test | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:BROCCOLI714USDT.P | CZ’s Dog | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:BOMEUSDT.P | BOOK OF MEME | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 17_A MEME | BINANCE:PEOPLEUSDT.P | ConstitutionDAO | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Meme | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 18_A FAN_TOKENS | BINANCE:OGUSDT.P | OG Fan Token | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: fan_token | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:NEARUSDT.P | NEAR Protocol | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:IOSTUSDT.P | IOST | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:ONEUSDT.P | Harmony | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:SAGAUSDT.P | Saga | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:HEMIUSDT.P | HEMI | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:TRXUSDT.P | TRON | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:XLMUSDT.P | Stellar Lumens | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:ARBUSDT.P | Arbitrum | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:HBARUSDT.P | Hedera Hashgraph | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:CELRUSDT.P | Celer Network | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:ALGOUSDT.P | Algorand | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:DOTUSDT.P | Polkadot | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:ATOMUSDT.P | Cosmos | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:POLUSDT.P | Polygon Ecosystem Token | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 19_A LAYER1_LAYER2 | BINANCE:EGLDUSDT.P | MultiversX | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Layer1_Layer2 | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:QNTUSDT.P | Quant | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:PROMUSDT.P | Prometeus | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:ZAMAUSDT.P | ZAMA | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:ZROUSDT.P | LayerZero | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:ZKCUSDT.P | Boundless | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:BICOUSDT.P | Biconomy | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:GPSUSDT.P | GoPlus Security | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:CVCUSDT.P | Civic | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:LAUSDT.P | Lagrange | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:ENSOUSDT.P | Enso | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:PYTHUSDT.P | Pyth Network | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:REDUSDT.P | RedStone | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 20_A INFRASTRUCTURE | BINANCE:ESPUSDT.P | Espresso | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: Infrastructure | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 23_A MINING | BINANCE:XVGUSDT.P | Verge | THEME_LEADER | Largest observed 30-session quoted turnover within this researched product-tag group. Binance product tag: mining-zone | https://fapi.binance.com/fapi/v1/exchangeInfo |
| 23_A MINING | BINANCE:RVNUSDT.P | Ravencoin | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. Binance product tag: mining-zone | https://fapi.binance.com/fapi/v1/exchangeInfo |
