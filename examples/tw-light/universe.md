> 由 `python examples/build_examples.py` 從 `examples/seeds/tw.tsv` 產生。
> 這是一次 build 寫出的 `.md` 產物，提交進倉庫是為了不執行任何東西也能讀到它。
> 其中所有指標數值都只作示意——見 [README.md](../README.md)。

# TW 標的池

- 檔位：精簡檔
- 事實截至：2026-09-17
- 版本：`c5004ec33935`
- 標的數：50
- 主題數：27
- 抗擾動穩定性：0.94 · 47 / 50 · ±1%
- 最大主題：10_H · 7 · 14% · 權重應得 5
- TradingView 條目：77 / 1000
- 落選或被排除的候選：22
- 校驗：通過

## 角色分佈

| 角色 | 數量 |
|---|---:|
| 錨點 (ANCHOR) | 4 |
| 基準 (BENCHMARK) | 2 |
| 貝塔衛星 (BETA_SATELLITE) | 7 |
| 廣度代理 (BREADTH_PROXY) | 1 |
| 流動性觀測 (LIQUIDITY_SENSOR) | 2 |
| 質量龍頭 (QUALITY_LEADER) | 6 |
| 主題龍頭 (THEME_LEADER) | 28 |

## 主題覆蓋

| 編碼 | 一級分類 | 主題 | 層級 | 數量 |
|---|---|---|---:|---:|
| 00_A | 市場基準 | BROAD_MARKET_ETF | 1 | 3 |
| 00_B | 市場基準 | EQUAL_WEIGHT_AND_BREADTH | 2 | 0 |
| 00_C | 市場基準 | VOLATILITY_AND_HEDGES | 3 | 0 |
| 10_A | 半導體與電子 | MEGACAP_PLATFORMS | 3 | 0 |
| 10_B | 半導體與電子 | SEMICONDUCTORS | 1 | 5 |
| 10_C | 半導體與電子 | SEMICAP_EQUIPMENT | 1 | 2 |
| 10_D | 半導體與電子 | ENTERPRISE_SOFTWARE | 1 | 1 |
| 10_E | 半導體與電子 | CYBERSECURITY | 3 | 0 |
| 10_F | 半導體與電子 | INTERNET_AND_ADTECH | 1 | 1 |
| 10_G | 半導體與電子 | IT_SERVICES_AND_CONSULTING | 2 | 0 |
| 10_H | 半導體與電子 | HARDWARE_AND_NETWORKING | 1 | 7 |
| 10_I | 半導體與電子 | IC_DESIGN | 1 | 4 |
| 11_A | AI基礎建設 | AI_COMPUTE | 1 | 2 |
| 11_B | AI基礎建設 | DATA_CENTER_AND_POWER | 1 | 2 |
| 20_A | 通訊 | STREAMING_AND_MEDIA | 3 | 0 |
| 20_B | 通訊 | TELECOM | 1 | 1 |
| 30_A | 消費 | DISCRETIONARY_LEADERS | 1 | 1 |
| 30_B | 消費 | STAPLES | 1 | 1 |
| 30_C | 消費 | RESTAURANTS_AND_TRAVEL | 1 | 2 |
| 30_E | 消費 | AUTOS_AND_MOBILITY | 2 | 0 |
| 40_A | 金融 | MONEY_CENTER_BANKS | 1 | 2 |
| 40_B | 金融 | PAYMENTS | 1 | 1 |
| 40_C | 金融 | ASSET_MANAGERS_AND_EXCHANGES | 1 | 1 |
| 40_D | 金融 | INSURANCE | 1 | 1 |
| 40_E | 金融 | REGIONAL_BANKS | 2 | 0 |
| 50_A | 醫療健康 | PHARMA | 1 | 1 |
| 50_B | 醫療健康 | MEDTECH_AND_DEVICES | 1 | 1 |
| 50_D | 醫療健康 | BIOTECH | 2 | 0 |
| 60_A | 工業 | AEROSPACE_AND_DEFENSE | 1 | 1 |
| 60_B | 工業 | MACHINERY_AND_RAIL | 1 | 1 |
| 60_C | 工業 | TRANSPORT_AND_LOGISTICS | 1 | 3 |
| 60_D | 工業 | ELECTRICAL_EQUIPMENT | 2 | 0 |
| 70_A | 能源 | INTEGRATED_ENERGY | 1 | 1 |
| 70_B | 能源 | OILFIELD_AND_MIDSTREAM | 1 | 1 |
| 80_A | 原材料與公用事業 | MATERIALS | 1 | 2 |
| 80_B | 原材料與公用事業 | UTILITIES | 1 | 1 |
| 80_C | 原材料與公用事業 | METALS_AND_MINING | 2 | 0 |
| 80_D | 原材料與公用事業 | CHEMICALS | 3 | 0 |
| 90_A | 不動產 | REITS | 3 | 0 |
| 90_D | 不動產 | PROPERTY_DEVELOPERS | 1 | 1 |

## 指標是怎麼來的

| 指標 | 口徑 | 方法 | 窗口 |
|---|---|---|---|
| beta_stability | 實測 (measured) | beta 估計在視窗前後兩半之間的一致程度 | 180d |
| beta_strength | 實測 (measured) | 對 TWSE:0050 的 OLS beta 絕對值，beta 為 2.0 記 100 | 180d |
| heat | 判斷 (judged) | 成交額躍升，須以交易所資料確認，單日波動不算 | — |
| independence | 實測 (measured) | 100 減去日報酬對 TWSE:0050 迴歸的 R² | 180d |
| liquidity | 實測 (measured) | 30 日日均成交額的截面分位 | 30d |
| quality | 規則與判斷混合 (blended) | 上市時長與規模分位，疊加對經營延續性的判斷 | — |

全部 50 個成員中有 40 個的 quality 由規則與判斷各佔 50% 和 50%。規則的一半讀取上市時長、規模分位與不利標記；判斷的一半是任何統計量都覆蓋不到的部分。

## 候選未能入選的原因

| 理由 | 數量 |
|---|---:|
| 名額已用盡 (not_selected_under_budget) | 20 |
| 品種類型被排除 (excluded_instrument_type) | 1 |
| 與已有成員重複 (redundant_with_member) | 1 |

## 成員

| 主題 | 代碼 | 名稱 | 角色 | 理由 | 證據 |
|---|---|---|---|---|---|
| 00_A BROAD_MARKET_ETF | TWSE:006208 | 富邦台50 | 基準 (BENCHMARK) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 00_A BROAD_MARKET_ETF | TWSE:0050 | 元大台灣50 | 基準 (BENCHMARK) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 00_A BROAD_MARKET_ETF | TWSE:0056 | 元大高股息 | 廣度代理 (BREADTH_PROXY) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_B SEMICONDUCTORS | TWSE:2330 | 台積電 | 錨點 (ANCHOR) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_B SEMICONDUCTORS | TWSE:2303 | 聯電 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_B SEMICONDUCTORS | TWSE:3711 | 日月光投控 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_B SEMICONDUCTORS | TWSE:6239 | 力成 | 質量龍頭 (QUALITY_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_B SEMICONDUCTORS | TWSE:2408 | 南亞科 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_C SEMICAP_EQUIPMENT | TPEX:3680 | 家登 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_C SEMICAP_EQUIPMENT | TWSE:2467 | 志聖 | 質量龍頭 (QUALITY_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_D ENTERPRISE_SOFTWARE | TWSE:2480 | 敦陽科 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_F INTERNET_AND_ADTECH | TWSE:8454 | 富邦媒 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_H HARDWARE_AND_NETWORKING | TWSE:2317 | 鴻海 | 錨點 (ANCHOR) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_H HARDWARE_AND_NETWORKING | TWSE:2382 | 廣達 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_H HARDWARE_AND_NETWORKING | TWSE:2308 | 台達電 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_H HARDWARE_AND_NETWORKING | TWSE:2345 | 智邦 | 質量龍頭 (QUALITY_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_H HARDWARE_AND_NETWORKING | TWSE:6669 | 緯穎 | 質量龍頭 (QUALITY_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_H HARDWARE_AND_NETWORKING | TWSE:2356 | 英業達 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_H HARDWARE_AND_NETWORKING | TWSE:2377 | 微星 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_I IC_DESIGN | TWSE:2454 | 聯發科 | 錨點 (ANCHOR) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_I IC_DESIGN | TWSE:3034 | 聯詠 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_I IC_DESIGN | TWSE:3661 | 世芯-KY | 質量龍頭 (QUALITY_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 10_I IC_DESIGN | TPEX:8299 | 群聯 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 11_A AI_COMPUTE | TWSE:3017 | 奇鋐 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 11_A AI_COMPUTE | TWSE:3324 | 雙鴻 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 11_B DATA_CENTER_AND_POWER | TWSE:1519 | 華城 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 11_B DATA_CENTER_AND_POWER | TWSE:1513 | 中興電 | 質量龍頭 (QUALITY_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 20_B TELECOM | TWSE:2412 | 中華電 | 錨點 (ANCHOR) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 30_A DISCRETIONARY_LEADERS | TWSE:9910 | 豐泰 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 30_B STAPLES | TWSE:1216 | 統一 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 30_C RESTAURANTS_AND_TRAVEL | TWSE:2707 | 晶華酒店 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 30_C RESTAURANTS_AND_TRAVEL | TWSE:2610 | 華航 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 40_A MONEY_CENTER_BANKS | TWSE:2891 | 中信金 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 40_A MONEY_CENTER_BANKS | TWSE:2881 | 富邦金 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 40_B PAYMENTS | TPEX:6763 | 綠界科技 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | TWSE:6005 | 群益證 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 40_D INSURANCE | TWSE:2867 | 三商壽 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 50_A PHARMA | TWSE:1795 | 美時 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 50_B MEDTECH_AND_DEVICES | TPEX:4736 | 泰博 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 60_A AEROSPACE_AND_DEFENSE | TWSE:2634 | 漢翔 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 60_B MACHINERY_AND_RAIL | TWSE:2049 | 上銀 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 60_C TRANSPORT_AND_LOGISTICS | TWSE:2603 | 長榮 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 60_C TRANSPORT_AND_LOGISTICS | TWSE:2609 | 陽明 | 流動性觀測 (LIQUIDITY_SENSOR) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 60_C TRANSPORT_AND_LOGISTICS | TWSE:2615 | 萬海 | 流動性觀測 (LIQUIDITY_SENSOR) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 70_A INTEGRATED_ENERGY | TWSE:6505 | 台塑化 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 70_B OILFIELD_AND_MIDSTREAM | TWSE:9926 | 新海瓦斯 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 80_A MATERIALS | TWSE:2002 | 中鋼 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 80_A MATERIALS | TWSE:1303 | 南亞 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 80_B UTILITIES | TWSE:8926 | 台汽電 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
| 90_D PROPERTY_DEVELOPERS | TWSE:2542 | 興富發 | 主題龍頭 (THEME_LEADER) |  | https://www.twse.com.tw/zh/listed/profile/company.html |
