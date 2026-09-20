> `python examples/build_examples.py` が `examples/seeds/jp.tsv` から生成。
> これは build が書き出す `.md` 成果物で、何も実行せずに読めるようリポジトリに入れてある。
> 指標の数値はすべて例示にすぎない——[README.md](../README.md) を参照。

# JP 銘柄ユニバース

- 深度：簡易
- 事実の基準日：2026-09-17
- バージョン：`d3b0c82f38c1`
- 銘柄数：65
- テーマ数：34
- 最大テーマ：30_E · 5 · 8% · ウェイト換算 5
- TradingView 項目数：99 / 1000
- 不採用・見送りの候補：55
- 検証：合格

## 役割の分布

| 役割 | 件数 |
|---|---:|
| アンカー (ANCHOR) | 10 |
| ベンチマーク (BENCHMARK) | 2 |
| ベータ・サテライト (BETA_SATELLITE) | 8 |
| 広がりの代理 (BREADTH_PROXY) | 1 |
| 流動性観測 (LIQUIDITY_SENSOR) | 2 |
| 新規上場 (NEW_LISTING) | 1 |
| 質の主導銘柄 (QUALITY_LEADER) | 10 |
| テーマ主導銘柄 (THEME_LEADER) | 31 |

## テーマの網羅

| コード | 大分類 | テーマ | 階層 | 件数 |
|---|---|---|---:|---:|
| 00_A | 市場ベンチマーク | BROAD_MARKET_ETF | 1 | 3 |
| 00_B | 市場ベンチマーク | EQUAL_WEIGHT_AND_BREADTH | 2 | 0 |
| 00_C | 市場ベンチマーク | VOLATILITY_AND_HEDGES | 3 | 0 |
| 10_A | テクノロジー | MEGACAP_PLATFORMS | 1 | 1 |
| 10_B | テクノロジー | SEMICONDUCTORS | 1 | 3 |
| 10_C | テクノロジー | SEMICAP_EQUIPMENT | 1 | 4 |
| 10_D | テクノロジー | ENTERPRISE_SOFTWARE | 1 | 1 |
| 10_E | テクノロジー | CYBERSECURITY | 1 | 1 |
| 10_F | テクノロジー | INTERNET_AND_ADTECH | 1 | 2 |
| 10_G | テクノロジー | IT_SERVICES_AND_CONSULTING | 1 | 1 |
| 10_H | テクノロジー | HARDWARE_AND_NETWORKING | 3 | 0 |
| 11_A | AIインフラ | AI_COMPUTE | 1 | 1 |
| 11_B | AIインフラ | DATA_CENTER_AND_POWER | 1 | 1 |
| 20_A | 通信・メディア | STREAMING_AND_MEDIA | 1 | 2 |
| 20_B | 通信・メディア | TELECOM | 1 | 1 |
| 20_C | 通信・メディア | GAMING_AND_INTERACTIVE | 1 | 2 |
| 20_D | 通信・メディア | ADVERTISING_AND_MARKETING | 3 | 0 |
| 30_A | 消費 | DISCRETIONARY_LEADERS | 1 | 2 |
| 30_B | 消費 | STAPLES | 1 | 2 |
| 30_C | 消費 | RESTAURANTS_AND_TRAVEL | 1 | 2 |
| 30_D | 消費 | APPAREL_AND_LUXURY | 2 | 0 |
| 30_E | 消費 | AUTOS_AND_MOBILITY | 1 | 5 |
| 30_G | 消費 | LEISURE_AND_LODGING | 3 | 0 |
| 40_A | 金融 | MONEY_CENTER_BANKS | 1 | 2 |
| 40_B | 金融 | PAYMENTS | 1 | 1 |
| 40_C | 金融 | ASSET_MANAGERS_AND_EXCHANGES | 1 | 2 |
| 40_D | 金融 | INSURANCE | 1 | 2 |
| 40_E | 金融 | REGIONAL_BANKS | 2 | 0 |
| 50_A | ヘルスケア | PHARMA | 1 | 2 |
| 50_B | ヘルスケア | MEDTECH_AND_DEVICES | 1 | 2 |
| 50_C | ヘルスケア | MANAGED_CARE | 3 | 0 |
| 50_D | ヘルスケア | BIOTECH | 2 | 0 |
| 50_E | ヘルスケア | LIFE_SCIENCE_TOOLS | 2 | 0 |
| 50_F | ヘルスケア | HEALTHCARE_DISTRIBUTION | 3 | 0 |
| 60_A | 資本財 | AEROSPACE_AND_DEFENSE | 1 | 2 |
| 60_B | 資本財 | MACHINERY_AND_RAIL | 1 | 3 |
| 60_C | 資本財 | TRANSPORT_AND_LOGISTICS | 1 | 2 |
| 60_D | 資本財 | ELECTRICAL_EQUIPMENT | 2 | 0 |
| 60_E | 資本財 | ENGINEERING_AND_CONSTRUCTION | 3 | 0 |
| 60_F | 資本財 | DISTRIBUTION_AND_SUPPLY | 3 | 0 |
| 65_A | 商社 | TRADING_HOUSES | 1 | 2 |
| 65_B | 商社 | WHOLESALE_AND_DISTRIBUTION | 3 | 0 |
| 70_A | エネルギー | INTEGRATED_ENERGY | 1 | 2 |
| 70_B | エネルギー | OILFIELD_AND_MIDSTREAM | 1 | 1 |
| 70_C | エネルギー | EXPLORATION_AND_PRODUCTION | 2 | 0 |
| 70_D | エネルギー | COAL_AND_URANIUM | 3 | 0 |
| 80_A | 素材・公益 | MATERIALS | 1 | 2 |
| 80_B | 素材・公益 | UTILITIES | 1 | 2 |
| 80_C | 素材・公益 | METALS_AND_MINING | 2 | 0 |
| 80_D | 素材・公益 | CHEMICALS | 3 | 0 |
| 80_E | 素材・公益 | WATER_AND_WASTE | 3 | 0 |
| 90_A | 不動産 | REITS | 1 | 1 |
| 90_B | 不動産 | DATA_AND_TOWER_REITS | 2 | 0 |
| 90_C | 不動産 | REAL_ESTATE_SERVICES | 3 | 0 |
| 90_D | 不動産 | PROPERTY_DEVELOPERS | 1 | 2 |
| 95_A | デジタル資産 | DIGITAL_ASSET_EQUITIES | 1 | 1 |

## 指標の算出方法

| 指標 | 根拠 | 手法 | 期間 |
|---|---|---|---|
| beta_stability | 実測 (measured) | 期間を前後半に割ったときのベータ推定値の一致度 | 180d |
| beta_strength | 実測 (measured) | TSE:1306 に対する OLS ベータの絶対値。ベータ 2.0 を 100 とする | 180d |
| heat | 判断 (judged) | 売買代金の急増。取引所データで確認したもののみ、単日の変動は数えない | — |
| independence | 実測 (measured) | 日次リターンを TSE:1306 に回帰した決定係数を 100 から引いたもの | 180d |
| liquidity | 実測 (measured) | 30 日平均売買代金のクロスセクション分位 | 30d |
| quality | ルールと判断の混合 (blended) | 上場年数と規模分位に、事業継続性の判断を重ねたもの | — |

全 65 銘柄のうち 53 銘柄で、quality はルール 50%、判断 50% の配分です。ルール側は上場からの年数、規模の分位、不利な指定を読み、判断側はどの統計にも表れない部分です。

## 候補が入らなかった理由

| 理由 | 件数 |
|---|---:|
| 枠を使い切った (not_selected_under_budget) | 53 |
| 対象外の商品種別 (excluded_instrument_type) | 1 |
| 既存銘柄と重複 (redundant_with_member) | 1 |

## 構成銘柄

| テーマ | ティッカー | 名称 | 役割 | 理由 | 出典 |
|---|---|---|---|---|---|
| 00_A BROAD_MARKET_ETF | TSE:1321 | NEXT FUNDS 日経225連動型上場投信 | ベンチマーク (BENCHMARK) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 00_A BROAD_MARKET_ETF | TSE:1306 | NEXT FUNDS TOPIX連動型上場投信 | ベンチマーク (BENCHMARK) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 00_A BROAD_MARKET_ETF | TSE:1475 | iシェアーズ・コア TOPIX ETF | 広がりの代理 (BREADTH_PROXY) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_A MEGACAP_PLATFORMS | TSE:9984 | ソフトバンクグループ | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_B SEMICONDUCTORS | TSE:6723 | ルネサスエレクトロニクス | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_B SEMICONDUCTORS | TSE:6963 | ローム | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_B SEMICONDUCTORS | TSE:285A | キオクシアホールディングス | 新規上場 (NEW_LISTING) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_C SEMICAP_EQUIPMENT | TSE:8035 | 東京エレクトロン | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_C SEMICAP_EQUIPMENT | TSE:6857 | アドバンテスト | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_C SEMICAP_EQUIPMENT | TSE:6146 | ディスコ | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_C SEMICAP_EQUIPMENT | TSE:6920 | レーザーテック | 流動性観測 (LIQUIDITY_SENSOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_D ENTERPRISE_SOFTWARE | TSE:4684 | オービック | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_E CYBERSECURITY | TSE:4704 | トレンドマイクロ | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_F INTERNET_AND_ADTECH | TSE:4755 | 楽天グループ | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_F INTERNET_AND_ADTECH | TSE:4385 | メルカリ | ベータ・サテライト (BETA_SATELLITE) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 10_G IT_SERVICES_AND_CONSULTING | TSE:4307 | 野村総合研究所 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 11_A AI_COMPUTE | TSE:3778 | さくらインターネット | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 11_B DATA_CENTER_AND_POWER | TSE:4485 | JTOWER | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 20_A STREAMING_AND_MEDIA | TSE:9602 | 東宝 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 20_A STREAMING_AND_MEDIA | TSE:9401 | TBSホールディングス | ベータ・サテライト (BETA_SATELLITE) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 20_B TELECOM | TSE:9432 | 日本電信電話 | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 20_C GAMING_AND_INTERACTIVE | TSE:6758 | ソニーグループ | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 20_C GAMING_AND_INTERACTIVE | TSE:7974 | 任天堂 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_A DISCRETIONARY_LEADERS | TSE:9983 | ファーストリテイリング | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_A DISCRETIONARY_LEADERS | TSE:4911 | 資生堂 | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_B STAPLES | TSE:2914 | 日本たばこ産業 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_B STAPLES | TSE:3382 | セブン&アイ・ホールディングス | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_C RESTAURANTS_AND_TRAVEL | TSE:7550 | ゼンショーホールディングス | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_C RESTAURANTS_AND_TRAVEL | TSE:9202 | ANAホールディングス | ベータ・サテライト (BETA_SATELLITE) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_E AUTOS_AND_MOBILITY | TSE:7203 | トヨタ自動車 | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_E AUTOS_AND_MOBILITY | TSE:7267 | ホンダ | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_E AUTOS_AND_MOBILITY | TSE:6902 | デンソー | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_E AUTOS_AND_MOBILITY | TSE:7269 | スズキ | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 30_E AUTOS_AND_MOBILITY | TSE:7201 | 日産自動車 | ベータ・サテライト (BETA_SATELLITE) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 40_A MONEY_CENTER_BANKS | TSE:8306 | 三菱UFJフィナンシャル・グループ | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 40_A MONEY_CENTER_BANKS | TSE:8316 | 三井住友フィナンシャルグループ | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 40_B PAYMENTS | TSE:3769 | GMOペイメントゲートウェイ | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | TSE:8604 | 野村ホールディングス | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | TSE:8601 | 大和証券グループ本社 | ベータ・サテライト (BETA_SATELLITE) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 40_D INSURANCE | TSE:8766 | 東京海上ホールディングス | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 40_D INSURANCE | TSE:8725 | MS&ADインシュアランスグループホールディングス | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 50_A PHARMA | TSE:4502 | 武田薬品工業 | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 50_A PHARMA | TSE:4568 | 第一三共 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 50_B MEDTECH_AND_DEVICES | TSE:7733 | オリンパス | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 50_B MEDTECH_AND_DEVICES | TSE:7741 | HOYA | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 60_A AEROSPACE_AND_DEFENSE | TSE:7011 | 三菱重工業 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 60_A AEROSPACE_AND_DEFENSE | TSE:7013 | IHI | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 60_B MACHINERY_AND_RAIL | TSE:6954 | ファナック | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 60_B MACHINERY_AND_RAIL | TSE:6301 | コマツ | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 60_B MACHINERY_AND_RAIL | TSE:9022 | 東海旅客鉄道 | ベータ・サテライト (BETA_SATELLITE) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 60_C TRANSPORT_AND_LOGISTICS | TSE:9101 | 日本郵船 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 60_C TRANSPORT_AND_LOGISTICS | TSE:9107 | 川崎汽船 | ベータ・サテライト (BETA_SATELLITE) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 65_A TRADING_HOUSES | TSE:8058 | 三菱商事 | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 65_A TRADING_HOUSES | TSE:8001 | 伊藤忠商事 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 70_A INTEGRATED_ENERGY | TSE:5020 | ENEOSホールディングス | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 70_A INTEGRATED_ENERGY | TSE:5019 | 出光興産 | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 70_B OILFIELD_AND_MIDSTREAM | TSE:6269 | 三井海洋開発 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 80_A MATERIALS | TSE:4063 | 信越化学工業 | アンカー (ANCHOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 80_A MATERIALS | TSE:4005 | 住友化学 | ベータ・サテライト (BETA_SATELLITE) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 80_B UTILITIES | TSE:9503 | 関西電力 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 80_B UTILITIES | TSE:9501 | 東京電力ホールディングス | 流動性観測 (LIQUIDITY_SENSOR) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 90_A REITS | TSE:8951 | 日本ビルファンド投資法人 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 90_D PROPERTY_DEVELOPERS | TSE:8801 | 三井不動産 | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 90_D PROPERTY_DEVELOPERS | TSE:8830 | 住友不動産 | 質の主導銘柄 (QUALITY_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
| 95_A DIGITAL_ASSET_EQUITIES | TSE:8698 | マネックスグループ | テーマ主導銘柄 (THEME_LEADER) |  | https://www.jpx.co.jp/markets/statistics-equities/misc/01.html |
