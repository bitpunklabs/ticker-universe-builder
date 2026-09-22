> 由 `python examples/build_examples.py` 從 `examples/seeds/hk.tsv` 產生。
> 這是一次 build 寫出的 `.md` 產物，提交進倉庫是為了不執行任何東西也能讀到它。
> 其中所有指標數值都只作示意——見 [README.md](../README.md)。

# HK 標的池

- 檔位：精簡檔
- 事實截至：2026-09-17
- 版本：`917ab5257359`
- 標的數：55
- 主題數：32
- 抗擾動穩定性：0.96 · 53 / 55 · ±1%
- 最大主題：10_F · 4 · 7% · 權重應得 4
- TradingView 條目：87 / 1000
- 落選或被排除的候選：40
- 校驗：通過

## 角色分佈

| 角色 | 數量 |
|---|---:|
| 錨點 (ANCHOR) | 8 |
| 基準 (BENCHMARK) | 2 |
| 貝塔衛星 (BETA_SATELLITE) | 7 |
| 廣度代理 (BREADTH_PROXY) | 1 |
| 流動性觀測 (LIQUIDITY_SENSOR) | 1 |
| 新上市 (NEW_LISTING) | 1 |
| 質量龍頭 (QUALITY_LEADER) | 7 |
| 主題龍頭 (THEME_LEADER) | 28 |

## 主題覆蓋

| 編碼 | 一級分類 | 主題 | 層級 | 數量 |
|---|---|---|---:|---:|
| 00_A | 市場基準 | BROAD_MARKET_ETF | 1 | 3 |
| 00_B | 市場基準 | EQUAL_WEIGHT_AND_BREADTH | 2 | 0 |
| 00_C | 市場基準 | VOLATILITY_AND_HEDGES | 3 | 0 |
| 10_A | 科技 | MEGACAP_PLATFORMS | 1 | 2 |
| 10_B | 科技 | SEMICONDUCTORS | 1 | 1 |
| 10_D | 科技 | ENTERPRISE_SOFTWARE | 1 | 2 |
| 10_E | 科技 | CYBERSECURITY | 3 | 0 |
| 10_F | 科技 | INTERNET_AND_ADTECH | 1 | 4 |
| 10_G | 科技 | IT_SERVICES_AND_CONSULTING | 2 | 0 |
| 10_H | 科技 | HARDWARE_AND_NETWORKING | 3 | 0 |
| 11_A | AI基建 | AI_COMPUTE | 1 | 1 |
| 11_B | AI基建 | DATA_CENTER_AND_POWER | 1 | 1 |
| 20_A | 通訊與博彩 | STREAMING_AND_MEDIA | 1 | 1 |
| 20_B | 通訊與博彩 | TELECOM | 1 | 1 |
| 20_C | 通訊與博彩 | GAMING_AND_INTERACTIVE | 1 | 3 |
| 20_E | 通訊與博彩 | MACAU_GAMING | 1 | 2 |
| 30_A | 消費 | DISCRETIONARY_LEADERS | 1 | 1 |
| 30_B | 消費 | STAPLES | 1 | 2 |
| 30_C | 消費 | RESTAURANTS_AND_TRAVEL | 1 | 1 |
| 30_D | 消費 | APPAREL_AND_LUXURY | 2 | 0 |
| 30_E | 消費 | AUTOS_AND_MOBILITY | 1 | 2 |
| 30_G | 消費 | LEISURE_AND_LODGING | 3 | 0 |
| 40_A | 金融 | MONEY_CENTER_BANKS | 1 | 3 |
| 40_B | 金融 | PAYMENTS | 1 | 1 |
| 40_C | 金融 | ASSET_MANAGERS_AND_EXCHANGES | 1 | 2 |
| 40_D | 金融 | INSURANCE | 1 | 2 |
| 40_E | 金融 | REGIONAL_BANKS | 2 | 0 |
| 40_F | 金融 | FINTECH_LENDERS | 3 | 0 |
| 50_A | 醫療健康 | PHARMA | 1 | 1 |
| 50_B | 醫療健康 | MEDTECH_AND_DEVICES | 1 | 2 |
| 50_C | 醫療健康 | MANAGED_CARE | 3 | 0 |
| 50_D | 醫療健康 | BIOTECH | 1 | 2 |
| 50_E | 醫療健康 | LIFE_SCIENCE_TOOLS | 2 | 0 |
| 50_F | 醫療健康 | HEALTHCARE_DISTRIBUTION | 3 | 0 |
| 60_A | 工業 | AEROSPACE_AND_DEFENSE | 1 | 1 |
| 60_B | 工業 | MACHINERY_AND_RAIL | 1 | 1 |
| 60_C | 工業 | TRANSPORT_AND_LOGISTICS | 1 | 2 |
| 60_D | 工業 | ELECTRICAL_EQUIPMENT | 2 | 0 |
| 60_E | 工業 | ENGINEERING_AND_CONSTRUCTION | 3 | 0 |
| 60_F | 工業 | DISTRIBUTION_AND_SUPPLY | 3 | 0 |
| 70_A | 能源 | INTEGRATED_ENERGY | 1 | 2 |
| 70_B | 能源 | OILFIELD_AND_MIDSTREAM | 1 | 1 |
| 70_C | 能源 | EXPLORATION_AND_PRODUCTION | 2 | 0 |
| 80_A | 原材料與公用事業 | MATERIALS | 1 | 2 |
| 80_B | 原材料與公用事業 | UTILITIES | 1 | 2 |
| 80_C | 原材料與公用事業 | METALS_AND_MINING | 2 | 0 |
| 80_D | 原材料與公用事業 | CHEMICALS | 3 | 0 |
| 90_A | 地產 | REITS | 1 | 1 |
| 90_B | 地產 | DATA_AND_TOWER_REITS | 2 | 0 |
| 90_C | 地產 | REAL_ESTATE_SERVICES | 3 | 0 |
| 90_D | 地產 | PROPERTY_DEVELOPERS | 1 | 2 |
| 95_A | 數字資產 | DIGITAL_ASSET_EQUITIES | 1 | 1 |

## 指標是怎麼來的

| 指標 | 口徑 | 方法 | 窗口 |
|---|---|---|---|
| beta_stability | 實測 (measured) | beta 估計在視窗前後兩半之間的一致程度 | 180d |
| beta_strength | 實測 (measured) | 對 HKEX:2800 的 OLS beta 絕對值，beta 為 2.0 記 100 | 180d |
| heat | 判斷 (judged) | 成交額躍升，須以交易所資料確認，單日波動不算 | — |
| independence | 實測 (measured) | 100 減去日報酬對 HKEX:2800 迴歸的 R² | 180d |
| liquidity | 實測 (measured) | 30 日日均成交額的截面分位 | 30d |
| quality | 規則與判斷混合 (blended) | 上市時長與規模分位，疊加對經營延續性的判斷 | — |

全部 55 個成員中有 45 個的 quality 由規則與判斷各佔 50% 和 50%。規則的一半讀取上市時長、規模分位與不利標記；判斷的一半是任何統計量都覆蓋不到的部分。

## 候選未能入選的原因

| 理由 | 數量 |
|---|---:|
| 名額已用盡 (not_selected_under_budget) | 38 |
| 品種類型被排除 (excluded_instrument_type) | 1 |
| 與已有成員重複 (redundant_with_member) | 1 |

## 成員

| 主題 | 代碼 | 名稱 | 角色 | 理由 | 證據 |
|---|---|---|---|---|---|
| 00_A BROAD_MARKET_ETF | HKEX:2828 | 恒生中國企業指數ETF | 基準 (BENCHMARK) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 00_A BROAD_MARKET_ETF | HKEX:2800 | 盈富基金 | 基準 (BENCHMARK) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 00_A BROAD_MARKET_ETF | HKEX:3033 | 南方東英恒生科技指數ETF | 廣度代理 (BREADTH_PROXY) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_A MEGACAP_PLATFORMS | HKEX:700 | 騰訊控股 | 錨點 (ANCHOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_A MEGACAP_PLATFORMS | HKEX:9988 | 阿里巴巴-W | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_B SEMICONDUCTORS | HKEX:981 | 中芯國際 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_D ENTERPRISE_SOFTWARE | HKEX:268 | 金蝶國際 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_D ENTERPRISE_SOFTWARE | HKEX:3888 | 金山軟件 | 質量龍頭 (QUALITY_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_F INTERNET_AND_ADTECH | HKEX:1024 | 快手-W | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_F INTERNET_AND_ADTECH | HKEX:9898 | 微博 | 質量龍頭 (QUALITY_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_F INTERNET_AND_ADTECH | HKEX:780 | 同程旅行 | 質量龍頭 (QUALITY_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 10_F INTERNET_AND_ADTECH | HKEX:772 | 閱文集團 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 11_A AI_COMPUTE | HKEX:9660 | 地平線機器人-W | 新上市 (NEW_LISTING) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 11_B DATA_CENTER_AND_POWER | HKEX:9698 | 萬國數據-SW | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 20_A STREAMING_AND_MEDIA | HKEX:1060 | 阿里影業 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 20_B TELECOM | HKEX:941 | 中國移動 | 錨點 (ANCHOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 20_C GAMING_AND_INTERACTIVE | HKEX:9999 | 網易-S | 錨點 (ANCHOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 20_C GAMING_AND_INTERACTIVE | HKEX:9626 | 嗶哩嗶哩-W | 質量龍頭 (QUALITY_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 20_C GAMING_AND_INTERACTIVE | HKEX:2400 | 心動公司 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 20_E MACAU_GAMING | HKEX:27 | 銀河娛樂 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 20_E MACAU_GAMING | HKEX:880 | 澳博控股 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 30_A DISCRETIONARY_LEADERS | HKEX:2020 | 安踏體育 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 30_B STAPLES | HKEX:291 | 華潤啤酒 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 30_B STAPLES | HKEX:2319 | 蒙牛乳業 | 質量龍頭 (QUALITY_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 30_C RESTAURANTS_AND_TRAVEL | HKEX:9961 | 攜程集團-S | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 30_E AUTOS_AND_MOBILITY | HKEX:1211 | 比亞迪股份 | 錨點 (ANCHOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 30_E AUTOS_AND_MOBILITY | HKEX:9868 | 小鵬汽車-W | 貝塔衛星 (BETA_SATELLITE) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 40_A MONEY_CENTER_BANKS | HKEX:5 | 滙豐控股 | 錨點 (ANCHOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 40_A MONEY_CENTER_BANKS | HKEX:1398 | 工商銀行 | 錨點 (ANCHOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 40_A MONEY_CENTER_BANKS | HKEX:939 | 建設銀行 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 40_B PAYMENTS | HKEX:9923 | 移卡 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | HKEX:388 | 香港交易所 | 錨點 (ANCHOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | HKEX:6030 | 中信証券 | 質量龍頭 (QUALITY_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 40_D INSURANCE | HKEX:1299 | 友邦保險 | 錨點 (ANCHOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 40_D INSURANCE | HKEX:2318 | 中國平安 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 50_A PHARMA | HKEX:1177 | 中國生物製藥 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 50_B MEDTECH_AND_DEVICES | HKEX:1789 | 愛康醫療 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 50_B MEDTECH_AND_DEVICES | HKEX:853 | 微創醫療 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 50_D BIOTECH | HKEX:6160 | 百濟神州 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 50_D BIOTECH | HKEX:1801 | 信達生物 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 60_A AEROSPACE_AND_DEFENSE | HKEX:2357 | 中航科工 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 60_B MACHINERY_AND_RAIL | HKEX:1766 | 中國中車 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 60_C TRANSPORT_AND_LOGISTICS | HKEX:144 | 招商局港口 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 60_C TRANSPORT_AND_LOGISTICS | HKEX:1919 | 中遠海控 | 流動性觀測 (LIQUIDITY_SENSOR) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 70_A INTEGRATED_ENERGY | HKEX:857 | 中國石油股份 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 70_A INTEGRATED_ENERGY | HKEX:883 | 中國海洋石油 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 70_B OILFIELD_AND_MIDSTREAM | HKEX:2883 | 中海油田服務 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 80_A MATERIALS | HKEX:1088 | 中國神華 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 80_A MATERIALS | HKEX:3323 | 中國建材 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 80_B UTILITIES | HKEX:2 | 中電控股 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 80_B UTILITIES | HKEX:836 | 華潤電力 | 貝塔衛星 (BETA_SATELLITE) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 90_A REITS | HKEX:823 | 領展房產基金 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 90_D PROPERTY_DEVELOPERS | HKEX:16 | 新鴻基地產 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 90_D PROPERTY_DEVELOPERS | HKEX:12 | 恒基地產 | 質量龍頭 (QUALITY_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
| 95_A DIGITAL_ASSET_EQUITIES | HKEX:434 | 博雅互動 | 主題龍頭 (THEME_LEADER) |  | https://www.hkex.com.hk/eng/services/trading/securities/securitieslists/ListOfSecurities.xlsx |
