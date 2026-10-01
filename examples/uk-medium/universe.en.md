# UK Ticker Universe

- Profile: Medium
- Facts as of: 2026-09-29
- Version: `2513aaf8d6d9`
- Tickers: 135
- Themes: 87
- Stability: 0.99 · 134 / 135 · ±1%
- Partially scored: 135 / 135
- Largest theme: 30_A · 3 · 2% · weighted share 3
- TradingView tokens: 222 / 1000
- Rejected or unselected candidates: 256
- Validation: PASS

- Real observations acquired 2026-09-29; completed prices through 2026-09-28. This is a disclosed research subset, not a complete market screen.
- Price requests: 393; received: 391; unavailable/excluded: 2. Candidates use successful verified rows only.
- Role leaders use observed size (equities) or turnover (crypto). No synthetic quality or heat score; incomplete scoring and bucket warnings are retained.
- Weights are sqrt(researched theme membership), median-normalised and clipped to 0.5..4; this is an observation budget judgement, not an investment weight.
- Industry is a provider classification requiring research review.
- Active quotes do not certify the absence of every regulatory adverse flag.
- Turnover is a raw-close x volume proxy, not exchange-reported daily notional.
- The requested price bench is a subset of the listing inventory.
- Industry peer factors are equal-weighted leave-one-out baskets. Fewer than two peers => no factor metric; no broad-index fallback. A singleton can be a breadth/size observation, never an unmeasured independent or beta sensor.

## Roles

| Role | Count |
|---|---:|
| BENCHMARK | 2 |
| BETA_SATELLITE | 1 |
| INDEPENDENT_SENSOR | 46 |
| THEME_LEADER | 86 |

## Themes

| Code | Group | Theme | Level | Weight | Count |
|---|---|---|---:|---:|---:|
| 00_A | Market gauges | CORE_GAUGES | 1 | 0.5 | 2 |
| 30_A | Commercial Services | MISCELLANEOUS_COMMERCIAL_SERVICES | 1 | 2.08 | 3 |
| 30_B | Commercial Services | FINANCIAL_PUBLISHING_SERVICES | 2 | 0.58 | 1 |
| 30_C | Commercial Services | ADVERTISING_MARKETING_SERVICES | 2 | 1 | 1 |
| 30_D | Commercial Services | PERSONNEL_SERVICES | 2 | 1 | 1 |
| 30_E | Commercial Services | COMMERCIAL_PRINTING_FORMS | 2 | 1 | 1 |
| 31_A | Communications | WIRELESS_TELECOMMUNICATIONS | 1 | 0.82 | 1 |
| 31_B | Communications | MAJOR_TELECOMMUNICATIONS | 2 | 0.82 | 1 |
| 31_C | Communications | SPECIALTY_TELECOMMUNICATIONS | 2 | 0.58 | 1 |
| 32_A | Consumer Durables | HOMEBUILDING | 1 | 1.53 | 3 |
| 32_B | Consumer Durables | RECREATIONAL_PRODUCTS | 2 | 1 | 1 |
| 32_C | Consumer Durables | ELECTRONICS_APPLIANCES | 2 | 0.58 | 1 |
| 32_D | Consumer Durables | HOME_FURNISHINGS | 3 | 1 | 0 |
| 32_E | Consumer Durables | MOTOR_VEHICLES | 3 | 0.58 | 0 |
| 33_A | Consumer Non-Durables | HOUSEHOLD_PERSONAL_CARE | 1 | 1 | 2 |
| 33_B | Consumer Non-Durables | TOBACCO | 2 | 0.82 | 1 |
| 33_C | Consumer Non-Durables | BEVERAGES_ALCOHOLIC | 2 | 1 | 1 |
| 33_D | Consumer Non-Durables | APPAREL_FOOTWEAR | 2 | 1 | 1 |
| 33_E | Consumer Non-Durables | BEVERAGES_NON_ALCOHOLIC | 2 | 1.15 | 2 |
| 33_F | Consumer Non-Durables | FOOD_MAJOR_DIVERSIFIED | 2 | 0.58 | 1 |
| 33_G | Consumer Non-Durables | FOOD_SPECIALTY_CANDY | 2 | 1.15 | 2 |
| 33_H | Consumer Non-Durables | FOOD_MEAT_FISH_DAIRY | 2 | 1 | 1 |
| 33_I | Consumer Non-Durables | CONSUMER_SUNDRIES | 3 | 0.82 | 0 |
| 34_A | Consumer Services | PUBLISHING_BOOKS_MAGAZINES | 1 | 1 | 2 |
| 34_B | Consumer Services | RESTAURANTS | 2 | 1.15 | 2 |
| 34_C | Consumer Services | HOTELS_RESORTS_CRUISE_LINES | 2 | 1 | 1 |
| 34_D | Consumer Services | OTHER_CONSUMER_SERVICES | 2 | 1 | 1 |
| 34_E | Consumer Services | MOVIES_ENTERTAINMENT | 2 | 1 | 1 |
| 34_F | Consumer Services | CASINOS_GAMING | 2 | 0.58 | 1 |
| 34_G | Consumer Services | CABLE_SATELLITE_TV | 2 | 0.58 | 1 |
| 34_H | Consumer Services | PUBLISHING_NEWSPAPERS | 3 | 0.58 | 0 |
| 34_I | Consumer Services | BROADCASTING | 3 | 0.58 | 0 |
| 35_A | Distribution Services | WHOLESALE_DISTRIBUTORS | 1 | 1.73 | 3 |
| 35_B | Distribution Services | FOOD_DISTRIBUTORS | 3 | 1 | 0 |
| 35_C | Distribution Services | ELECTRONICS_DISTRIBUTORS | 3 | 0.82 | 0 |
| 35_D | Distribution Services | MEDICAL_DISTRIBUTORS | 3 | 0.82 | 0 |
| 36_A | Electronic Technology | AEROSPACE_DEFENSE | 1 | 1.73 | 3 |
| 36_B | Electronic Technology | ELECTRONIC_EQUIPMENT_INSTRUMENTS | 2 | 1.15 | 2 |
| 36_C | Electronic Technology | COMPUTER_PROCESSING_HARDWARE | 2 | 0.82 | 1 |
| 36_D | Electronic Technology | ELECTRONIC_PRODUCTION_EQUIPMENT | 2 | 1 | 1 |
| 36_E | Electronic Technology | TELECOMMUNICATIONS_EQUIPMENT | 2 | 1 | 1 |
| 36_F | Electronic Technology | ELECTRONIC_COMPONENTS | 3 | 1 | 0 |
| 36_G | Electronic Technology | COMPUTER_COMMUNICATIONS | 3 | 1 | 0 |
| 36_H | Electronic Technology | SEMICONDUCTORS | 3 | 1 | 0 |
| 37_A | Energy Minerals | INTEGRATED_OIL | 1 | 1 | 2 |
| 37_B | Energy Minerals | OIL_GAS_PRODUCTION | 2 | 1.53 | 2 |
| 37_C | Energy Minerals | COAL | 3 | 1 | 0 |
| 38_A | Finance | MAJOR_BANKS | 1 | 1.53 | 3 |
| 38_B | Finance | INVESTMENT_BANKS_BROKERS | 2 | 1.41 | 2 |
| 38_C | Finance | MULTI_LINE_INSURANCE | 2 | 1.41 | 2 |
| 38_D | Finance | REAL_ESTATE_INVESTMENT_TRUSTS | 2 | 2.16 | 3 |
| 38_E | Finance | INVESTMENT_MANAGERS | 2 | 2.24 | 3 |
| 38_F | Finance | LIFE_HEALTH_INSURANCE | 2 | 0.82 | 1 |
| 38_G | Finance | FINANCIAL_CONGLOMERATES | 2 | 1 | 1 |
| 38_H | Finance | PROPERTY_CASUALTY_INSURANCE | 2 | 1 | 1 |
| 38_I | Finance | REAL_ESTATE_DEVELOPMENT | 2 | 1.29 | 2 |
| 38_J | Finance | FINANCE_RENTAL_LEASING | 2 | 1.15 | 2 |
| 38_K | Finance | SAVINGS_BANKS | 2 | 0.82 | 1 |
| 38_L | Finance | REGIONAL_BANKS | 2 | 1 | 1 |
| 38_M | Finance | SPECIALTY_INSURANCE | 2 | 0.58 | 1 |
| 38_N | Finance | INSURANCE_BROKERS_SERVICES | 3 | 1 | 0 |
| 39_A | Health Services | HOSPITAL_NURSING_MANAGEMENT | 1 | 0.82 | 1 |
| 39_B | Health Services | MEDICAL_NURSING_SERVICES | 3 | 1 | 0 |
| 40_A | Health Technology | PHARMACEUTICALS_MAJOR | 1 | 1 | 2 |
| 40_B | Health Technology | MEDICAL_SPECIALTIES | 2 | 1 | 1 |
| 40_C | Health Technology | PHARMACEUTICALS_GENERIC | 2 | 0.58 | 1 |
| 40_D | Health Technology | BIOTECHNOLOGY | 2 | 1 | 1 |
| 40_E | Health Technology | PHARMACEUTICALS_OTHER | 2 | 1 | 1 |
| 41_A | Industrial Services | ENGINEERING_CONSTRUCTION | 1 | 1.53 | 3 |
| 41_B | Industrial Services | OILFIELD_SERVICES_EQUIPMENT | 2 | 1 | 1 |
| 41_C | Industrial Services | ENVIRONMENTAL_SERVICES | 3 | 0.58 | 0 |
| 42_A | Miscellaneous | INVESTMENT_TRUSTS_MUTUAL_FUNDS | 1 | 1.63 | 3 |
| 42_B | Miscellaneous | MISCELLANEOUS | 3 | 0.82 | 0 |
| 43_A | Non-Energy Minerals | OTHER_METALS_MINERALS | 1 | 1.53 | 3 |
| 43_B | Non-Energy Minerals | PRECIOUS_METALS | 2 | 1.63 | 2 |
| 43_C | Non-Energy Minerals | CONSTRUCTION_MATERIALS | 2 | 1 | 1 |
| 43_D | Non-Energy Minerals | STEEL | 3 | 1 | 0 |
| 44_A | Process Industries | CHEMICALS_SPECIALTY | 1 | 1 | 2 |
| 44_B | Process Industries | CHEMICALS_MAJOR_DIVERSIFIED | 2 | 1 | 1 |
| 44_C | Process Industries | CONTAINERS_PACKAGING | 2 | 0.82 | 1 |
| 44_D | Process Industries | AGRICULTURAL_COMMODITIES_MILLING | 2 | 1 | 1 |
| 44_E | Process Industries | TEXTILES | 2 | 0.58 | 1 |
| 44_F | Process Industries | INDUSTRIAL_SPECIALTIES | 2 | 1 | 1 |
| 44_G | Process Industries | CHEMICALS_AGRICULTURAL | 3 | 1 | 0 |
| 45_A | Producer Manufacturing | INDUSTRIAL_MACHINERY | 1 | 1.63 | 3 |
| 45_B | Producer Manufacturing | ELECTRICAL_PRODUCTS | 2 | 1.41 | 2 |
| 45_C | Producer Manufacturing | TRUCKS_CONSTRUCTION_FARM_MACHINERY | 2 | 1 | 1 |
| 45_D | Producer Manufacturing | MISCELLANEOUS_MANUFACTURING | 2 | 1 | 1 |
| 45_E | Producer Manufacturing | BUILDING_PRODUCTS | 2 | 1 | 1 |
| 45_F | Producer Manufacturing | METAL_FABRICATION | 3 | 0.82 | 0 |
| 45_G | Producer Manufacturing | AUTO_PARTS_OEM | 3 | 1 | 0 |
| 46_A | Retail Trade | FOOD_RETAIL | 1 | 1.15 | 2 |
| 46_B | Retail Trade | SPECIALTY_STORES | 2 | 1.53 | 2 |
| 46_C | Retail Trade | DEPARTMENT_STORES | 2 | 0.58 | 1 |
| 46_D | Retail Trade | HOME_IMPROVEMENT_CHAINS | 2 | 0.82 | 1 |
| 46_E | Retail Trade | APPAREL_FOOTWEAR_RETAIL | 2 | 0.82 | 1 |
| 46_F | Retail Trade | DISCOUNT_STORES | 2 | 0.58 | 1 |
| 46_G | Retail Trade | INTERNET_RETAIL | 2 | 1 | 1 |
| 46_H | Retail Trade | ELECTRONICS_APPLIANCE_STORES | 3 | 0.82 | 0 |
| 47_A | Technology Services | INTERNET_SOFTWARE_SERVICES | 1 | 1.53 | 3 |
| 47_B | Technology Services | PACKAGED_SOFTWARE | 2 | 1.41 | 2 |
| 47_C | Technology Services | INFORMATION_TECHNOLOGY_SERVICES | 2 | 1.15 | 2 |
| 47_D | Technology Services | DATA_PROCESSING_SERVICES | 3 | 1 | 0 |
| 48_A | Transportation | AIRLINES | 1 | 1 | 2 |
| 48_B | Transportation | MARINE_SHIPPING | 2 | 0.82 | 1 |
| 48_C | Transportation | OTHER_TRANSPORTATION | 2 | 1 | 1 |
| 48_D | Transportation | AIR_FREIGHT_COURIERS | 3 | 0.58 | 0 |
| 49_A | Utilities | ELECTRIC_UTILITIES | 1 | 1.15 | 2 |
| 49_B | Utilities | WATER_UTILITIES | 2 | 1 | 1 |
| 49_C | Utilities | GAS_DISTRIBUTORS | 2 | 1 | 2 |
| 49_D | Utilities | ALTERNATIVE_POWER_GENERATION | 3 | 0.58 | 0 |

## How the metrics were produced

| Metric | Basis | Method | Window |
|---|---|---|---|
| beta_stability | measured | agreement of the beta estimate across the two halves of the 180d window | 180d |
| beta_strength | measured | positive OLS beta against per-ticker theme gauge (measurement_record), scaled so beta 2.0 reads 100 | 180d |
| factor_r2 | measured | OLS R-squared of daily returns on per-ticker theme gauge (measurement_record) | 180d |
| independence | measured | derived as 100 - factor_r2 by the builder | 180d |
| liquidity | measured | cross-sectional percentile of mean daily turnover over 30 sessions | 30d |

## Why candidates did not make it

| Reason | Count |
|---|---:|
| not_selected_under_budget | 202 |
| outside_profile_coverage | 54 |

## Warnings

- 87 themes have no declared observation duty; legacy presence-only coverage applies

## Members

| Theme | Ticker | Name | Role | Reason | Evidence |
|---|---|---|---|---|---|
| 00_A CORE_GAUGES | LSE:ISF | iShares Core FTSE 100 UCITS ETF GBP (Dist) | BENCHMARK | Retained market/style gauge; observed active quotation and adjusted history. Broad market/style gauge | https://scanner.tradingview.com/uk/scan |
| 00_A CORE_GAUGES | LSE:VMID | Vanguard FTSE 250 UCITS ETF | BENCHMARK | Retained market/style gauge; observed active quotation and adjusted history. Broad market/style gauge | https://scanner.tradingview.com/uk/scan |
| 30_A MISCELLANEOUS_COMMERCIAL_SERVICES | LSE:REL | RELX PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Commercial Services / Miscellaneous Commercial Services | https://scanner.tradingview.com/uk/scan |
| 30_A MISCELLANEOUS_COMMERCIAL_SERVICES | LSE:MTO | MITIE Group PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Commercial Services / Miscellaneous Commercial Services | https://scanner.tradingview.com/uk/scan |
| 30_A MISCELLANEOUS_COMMERCIAL_SERVICES | LSE:RTO | Rentokil Initial plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Commercial Services / Miscellaneous Commercial Services | https://scanner.tradingview.com/uk/scan |
| 30_B FINANCIAL_PUBLISHING_SERVICES | LSE:LSEG | London Stock Exchange Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Commercial Services / Financial Publishing/Services | https://scanner.tradingview.com/uk/scan |
| 30_C ADVERTISING_MARKETING_SERVICES | LSE:WPP | WPP Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Commercial Services / Advertising/Marketing Services | https://scanner.tradingview.com/uk/scan |
| 30_D PERSONNEL_SERVICES | LSE:HAS | Hays plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Commercial Services / Personnel Services | https://scanner.tradingview.com/uk/scan |
| 30_E COMMERCIAL_PRINTING_FORMS | LSE:FOUR | 4imprint Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Commercial Services / Commercial Printing/Forms | https://scanner.tradingview.com/uk/scan |
| 31_A WIRELESS_TELECOMMUNICATIONS | LSE:VOD | Vodafone Group Public Limited Company | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Communications / Wireless Telecommunications | https://scanner.tradingview.com/uk/scan |
| 31_B MAJOR_TELECOMMUNICATIONS | LSE:BT.A | BT Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Communications / Major Telecommunications | https://scanner.tradingview.com/uk/scan |
| 31_C SPECIALTY_TELECOMMUNICATIONS | LSE:HTWS | Helios Towers Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Communications / Specialty Telecommunications | https://scanner.tradingview.com/uk/scan |
| 32_A HOMEBUILDING | LSE:BTRW | Barratt Redrow plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Durables / Homebuilding | https://scanner.tradingview.com/uk/scan |
| 32_A HOMEBUILDING | LSE:BKG | Berkeley Group Holdings plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Consumer Durables / Homebuilding | https://scanner.tradingview.com/uk/scan |
| 32_A HOMEBUILDING | LSE:CRN | Cairn Homes PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Consumer Durables / Homebuilding | https://scanner.tradingview.com/uk/scan |
| 32_B RECREATIONAL_PRODUCTS | LSE:GAW | Games Workshop Group PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Durables / Recreational Products | https://scanner.tradingview.com/uk/scan |
| 32_C ELECTRONICS_APPLIANCES | LSE:HWDN | Howden Joinery Group PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Durables / Electronics/Appliances | https://scanner.tradingview.com/uk/scan |
| 33_A HOUSEHOLD_PERSONAL_CARE | LSE:ULVR | Unilever PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Non-Durables / Household/Personal Care | https://scanner.tradingview.com/uk/scan |
| 33_A HOUSEHOLD_PERSONAL_CARE | LSE:RKT | Reckitt Benckiser Group plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Consumer Non-Durables / Household/Personal Care | https://scanner.tradingview.com/uk/scan |
| 33_B TOBACCO | LSE:BATS | British American Tobacco p.l.c. | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Non-Durables / Tobacco | https://scanner.tradingview.com/uk/scan |
| 33_C BEVERAGES_ALCOHOLIC | LSE:DGE | Diageo plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Non-Durables / Beverages: Alcoholic | https://scanner.tradingview.com/uk/scan |
| 33_D APPAREL_FOOTWEAR | LSE:NXT | Next plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Non-Durables / Apparel/Footwear | https://scanner.tradingview.com/uk/scan |
| 33_E BEVERAGES_NON_ALCOHOLIC | LSE:CCH | Coca-Cola HBC AG | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Non-Durables / Beverages: Non-Alcoholic | https://scanner.tradingview.com/uk/scan |
| 33_E BEVERAGES_NON_ALCOHOLIC | LSE:PRN | Princes Group Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Consumer Non-Durables / Beverages: Non-Alcoholic | https://scanner.tradingview.com/uk/scan |
| 33_F FOOD_MAJOR_DIVERSIFIED | LSE:ABF | Associated British Foods plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Non-Durables / Food: Major Diversified | https://scanner.tradingview.com/uk/scan |
| 33_G FOOD_SPECIALTY_CANDY | LSE:TATE | Tate & Lyle PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Non-Durables / Food: Specialty/Candy | https://scanner.tradingview.com/uk/scan |
| 33_G FOOD_SPECIALTY_CANDY | LSE:GRG | Greggs plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Consumer Non-Durables / Food: Specialty/Candy | https://scanner.tradingview.com/uk/scan |
| 33_H FOOD_MEAT_FISH_DAIRY | LSE:CWK | Cranswick plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Non-Durables / Food: Meat/Fish/Dairy | https://scanner.tradingview.com/uk/scan |
| 34_A PUBLISHING_BOOKS_MAGAZINES | LSE:PSON | Pearson PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Services / Publishing: Books/Magazines | https://scanner.tradingview.com/uk/scan |
| 34_A PUBLISHING_BOOKS_MAGAZINES | LSE:BMY | Bloomsbury Publishing Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Consumer Services / Publishing: Books/Magazines | https://scanner.tradingview.com/uk/scan |
| 34_B RESTAURANTS | LSE:MAB | Mitchells & Butlers plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Services / Restaurants | https://scanner.tradingview.com/uk/scan |
| 34_B RESTAURANTS | LSE:DOM | Domino's Pizza Group plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Consumer Services / Restaurants | https://scanner.tradingview.com/uk/scan |
| 34_C HOTELS_RESORTS_CRUISE_LINES | LSE:WTB | Whitbread PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Services / Hotels/Resorts/Cruise lines | https://scanner.tradingview.com/uk/scan |
| 34_D OTHER_CONSUMER_SERVICES | LSE:JET2 | Jet2 PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Services / Other Consumer Services | https://scanner.tradingview.com/uk/scan |
| 34_E MOVIES_ENTERTAINMENT | LSE:ITV | ITV PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Services / Movies/Entertainment | https://scanner.tradingview.com/uk/scan |
| 34_F CASINOS_GAMING | LSE:ENT | Entain PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Services / Casinos/Gaming | https://scanner.tradingview.com/uk/scan |
| 34_G CABLE_SATELLITE_TV | LSE:CAN | Canal+ SA | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Consumer Services / Cable/Satellite TV | https://scanner.tradingview.com/uk/scan |
| 35_A WHOLESALE_DISTRIBUTORS | LSE:GLEN | Glencore plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Distribution Services / Wholesale Distributors | https://scanner.tradingview.com/uk/scan |
| 35_A WHOLESALE_DISTRIBUTORS | LSE:BNZL | Bunzl plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Distribution Services / Wholesale Distributors | https://scanner.tradingview.com/uk/scan |
| 35_A WHOLESALE_DISTRIBUTORS | LSE:DPLM | Diploma PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Distribution Services / Wholesale Distributors | https://scanner.tradingview.com/uk/scan |
| 36_A AEROSPACE_DEFENSE | LSE:RR. | Rolls-Royce Holdings plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Electronic Technology / Aerospace & Defense | https://scanner.tradingview.com/uk/scan |
| 36_A AEROSPACE_DEFENSE | LSE:SNR | Senior plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Electronic Technology / Aerospace & Defense | https://scanner.tradingview.com/uk/scan |
| 36_A AEROSPACE_DEFENSE | LSE:BOY | Bodycote plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Electronic Technology / Aerospace & Defense | https://scanner.tradingview.com/uk/scan |
| 36_B ELECTRONIC_EQUIPMENT_INSTRUMENTS | LSE:HLMA | Halma plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Electronic Technology / Electronic Equipment/Instruments | https://scanner.tradingview.com/uk/scan |
| 36_B ELECTRONIC_EQUIPMENT_INSTRUMENTS | LSE:ONT | Oxford Nanopore Technologies Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Electronic Technology / Electronic Equipment/Instruments | https://scanner.tradingview.com/uk/scan |
| 36_C COMPUTER_PROCESSING_HARDWARE | LSE:RPI | Raspberry PI Holdings plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Electronic Technology / Computer Processing Hardware | https://scanner.tradingview.com/uk/scan |
| 36_D ELECTRONIC_PRODUCTION_EQUIPMENT | LSE:CWR | Ceres Power Holdings plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Electronic Technology / Electronic Production Equipment | https://scanner.tradingview.com/uk/scan |
| 36_E TELECOMMUNICATIONS_EQUIPMENT | LSE:FTC | Filtronic plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Electronic Technology / Telecommunications Equipment | https://scanner.tradingview.com/uk/scan |
| 37_A INTEGRATED_OIL | LSE:SHEL | Shell Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Energy Minerals / Integrated Oil | https://scanner.tradingview.com/uk/scan |
| 37_A INTEGRATED_OIL | LSE:ITH | Ithaca Energy PLC | BETA_SATELLITE | Positive, stable measured beta to the disclosed factor; adds sensitivity within this theme. TradingView: Energy Minerals / Integrated Oil | https://scanner.tradingview.com/uk/scan |
| 37_B OIL_GAS_PRODUCTION | LSE:SEPL | Seplat Energy PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Energy Minerals / Oil & Gas Production | https://scanner.tradingview.com/uk/scan |
| 37_B OIL_GAS_PRODUCTION | LSE:RKH | Rockhopper Exploration plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Energy Minerals / Oil & Gas Production | https://scanner.tradingview.com/uk/scan |
| 38_A MAJOR_BANKS | LSE:HSBA | HSBC Holdings Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Major Banks | https://scanner.tradingview.com/uk/scan |
| 38_A MAJOR_BANKS | LSE:OSB | OSB Group PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Major Banks | https://scanner.tradingview.com/uk/scan |
| 38_A MAJOR_BANKS | LSE:TBCG | TBC Bank Group Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Major Banks | https://scanner.tradingview.com/uk/scan |
| 38_B INVESTMENT_BANKS_BROKERS | LSE:BARC | Barclays PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Investment Banks/Brokers | https://scanner.tradingview.com/uk/scan |
| 38_B INVESTMENT_BANKS_BROKERS | LSE:INVP | Investec plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Investment Banks/Brokers | https://scanner.tradingview.com/uk/scan |
| 38_C MULTI_LINE_INSURANCE | LSE:PRU | Prudential plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Multi-Line Insurance | https://scanner.tradingview.com/uk/scan |
| 38_C MULTI_LINE_INSURANCE | LSE:BEZ | Beazley Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Multi-Line Insurance | https://scanner.tradingview.com/uk/scan |
| 38_D REAL_ESTATE_INVESTMENT_TRUSTS | LSE:SGRO | SEGRO plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Real Estate Investment Trusts | https://scanner.tradingview.com/uk/scan |
| 38_D REAL_ESTATE_INVESTMENT_TRUSTS | LSE:CREI | Custodian Property Income REIT plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Real Estate Investment Trusts | https://scanner.tradingview.com/uk/scan |
| 38_D REAL_ESTATE_INVESTMENT_TRUSTS | LSE:WKP | Workspace Group PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Real Estate Investment Trusts | https://scanner.tradingview.com/uk/scan |
| 38_E INVESTMENT_MANAGERS | LSE:SDR | Schroders PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Investment Managers | https://scanner.tradingview.com/uk/scan |
| 38_E INVESTMENT_MANAGERS | LSE:AJB | AJ Bell Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Investment Managers | https://scanner.tradingview.com/uk/scan |
| 38_E INVESTMENT_MANAGERS | LSE:TAM | Tatton Asset Management Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Investment Managers | https://scanner.tradingview.com/uk/scan |
| 38_F LIFE_HEALTH_INSURANCE | LSE:SDLF | Standard Life plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Life/Health Insurance | https://scanner.tradingview.com/uk/scan |
| 38_G FINANCIAL_CONGLOMERATES | LSE:MNG | M&G Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Financial Conglomerates | https://scanner.tradingview.com/uk/scan |
| 38_H PROPERTY_CASUALTY_INSURANCE | LSE:ADM | Admiral Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Property/Casualty Insurance | https://scanner.tradingview.com/uk/scan |
| 38_I REAL_ESTATE_DEVELOPMENT | LSE:UTG | UNITE Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Real Estate Development | https://scanner.tradingview.com/uk/scan |
| 38_I REAL_ESTATE_DEVELOPMENT | LSE:HWG | Harworth Group PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Real Estate Development | https://scanner.tradingview.com/uk/scan |
| 38_J FINANCE_RENTAL_LEASING | LSE:MTRO | Metro Bank Holdings Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Finance/Rental/Leasing | https://scanner.tradingview.com/uk/scan |
| 38_J FINANCE_RENTAL_LEASING | LSE:FCH | Funding Circle Holdings Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Finance / Finance/Rental/Leasing | https://scanner.tradingview.com/uk/scan |
| 38_K SAVINGS_BANKS | LSE:SHAW | Shawbrook Group Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Savings Banks | https://scanner.tradingview.com/uk/scan |
| 38_L REGIONAL_BANKS | LSE:PAG | Paragon Banking Group PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Regional Banks | https://scanner.tradingview.com/uk/scan |
| 38_M SPECIALTY_INSURANCE | LSE:CRE | Conduit Holdings Ltd. | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Finance / Specialty Insurance | https://scanner.tradingview.com/uk/scan |
| 39_A HOSPITAL_NURSING_MANAGEMENT | LSE:SPI | Spire Healthcare Group PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Health Services / Hospital/Nursing Management | https://scanner.tradingview.com/uk/scan |
| 40_A PHARMACEUTICALS_MAJOR | LSE:AZN | AstraZeneca PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Health Technology / Pharmaceuticals: Major | https://scanner.tradingview.com/uk/scan |
| 40_A PHARMACEUTICALS_MAJOR | LSE:HLN | Haleon PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Health Technology / Pharmaceuticals: Major | https://scanner.tradingview.com/uk/scan |
| 40_B MEDICAL_SPECIALTIES | LSE:SN. | Smith & Nephew plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Health Technology / Medical Specialties | https://scanner.tradingview.com/uk/scan |
| 40_C PHARMACEUTICALS_GENERIC | LSE:HIK | Hikma Pharmaceuticals Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Health Technology / Pharmaceuticals: Generic | https://scanner.tradingview.com/uk/scan |
| 40_D BIOTECHNOLOGY | LSE:OXB | Oxford BioMedica plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Health Technology / Biotechnology | https://scanner.tradingview.com/uk/scan |
| 40_E PHARMACEUTICALS_OTHER | LSE:APN | Applied Nutrition PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Health Technology / Pharmaceuticals: Other | https://scanner.tradingview.com/uk/scan |
| 41_A ENGINEERING_CONSTRUCTION | LSE:BBY | Balfour Beatty plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Industrial Services / Engineering & Construction | https://scanner.tradingview.com/uk/scan |
| 41_A ENGINEERING_CONSTRUCTION | LSE:KLR | Keller Group plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Industrial Services / Engineering & Construction | https://scanner.tradingview.com/uk/scan |
| 41_A ENGINEERING_CONSTRUCTION | LSE:COST | Costain Group PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Industrial Services / Engineering & Construction | https://scanner.tradingview.com/uk/scan |
| 41_B OILFIELD_SERVICES_EQUIPMENT | LSE:HTG | Hunting PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Industrial Services / Oilfield Services/Equipment | https://scanner.tradingview.com/uk/scan |
| 42_A INVESTMENT_TRUSTS_MUTUAL_FUNDS | LSE:III | 3i Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Miscellaneous / Investment Trusts/Mutual Funds | https://scanner.tradingview.com/uk/scan |
| 42_A INVESTMENT_TRUSTS_MUTUAL_FUNDS | LSE:BBOX | Tritax Big Box REIT PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Miscellaneous / Investment Trusts/Mutual Funds | https://scanner.tradingview.com/uk/scan |
| 42_A INVESTMENT_TRUSTS_MUTUAL_FUNDS | LSE:GROW | Molten Ventures PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Miscellaneous / Investment Trusts/Mutual Funds | https://scanner.tradingview.com/uk/scan |
| 43_A OTHER_METALS_MINERALS | LSE:RIO | Rio Tinto plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Non-Energy Minerals / Other Metals/Minerals | https://scanner.tradingview.com/uk/scan |
| 43_A OTHER_METALS_MINERALS | LSE:YCA | Yellow Cake Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Non-Energy Minerals / Other Metals/Minerals | https://scanner.tradingview.com/uk/scan |
| 43_A OTHER_METALS_MINERALS | LSE:RHIM | RHI Magnesita NV | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Non-Energy Minerals / Other Metals/Minerals | https://scanner.tradingview.com/uk/scan |
| 43_B PRECIOUS_METALS | LSE:FRES | Fresnillo PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Non-Energy Minerals / Precious Metals | https://scanner.tradingview.com/uk/scan |
| 43_B PRECIOUS_METALS | LSE:TUN | Tungsten West Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Non-Energy Minerals / Precious Metals | https://scanner.tradingview.com/uk/scan |
| 43_C CONSTRUCTION_MATERIALS | LSE:SRC | SigmaRoc Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Non-Energy Minerals / Construction Materials | https://scanner.tradingview.com/uk/scan |
| 44_A CHEMICALS_SPECIALTY | LSE:CRDA | Croda International Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Process Industries / Chemicals: Specialty | https://scanner.tradingview.com/uk/scan |
| 44_A CHEMICALS_SPECIALTY | LSE:ZTF | Zotefoams plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Process Industries / Chemicals: Specialty | https://scanner.tradingview.com/uk/scan |
| 44_B CHEMICALS_MAJOR_DIVERSIFIED | LSE:JMAT | Johnson Matthey Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Process Industries / Chemicals: Major Diversified | https://scanner.tradingview.com/uk/scan |
| 44_C CONTAINERS_PACKAGING | LSE:MNDI | Mondi plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Process Industries / Containers/Packaging | https://scanner.tradingview.com/uk/scan |
| 44_D AGRICULTURAL_COMMODITIES_MILLING | LSE:GNS | Genus plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Process Industries / Agricultural Commodities/Milling | https://scanner.tradingview.com/uk/scan |
| 44_E TEXTILES | LSE:COA | Coats Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Process Industries / Textiles | https://scanner.tradingview.com/uk/scan |
| 44_F INDUSTRIAL_SPECIALTIES | LSE:MGAM | Morgan Advanced Materials plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Process Industries / Industrial Specialties | https://scanner.tradingview.com/uk/scan |
| 45_A INDUSTRIAL_MACHINERY | LSE:IMI | IMI plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Producer Manufacturing / Industrial Machinery | https://scanner.tradingview.com/uk/scan |
| 45_A INDUSTRIAL_MACHINERY | LSE:ROR | Rotork plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Producer Manufacturing / Industrial Machinery | https://scanner.tradingview.com/uk/scan |
| 45_A INDUSTRIAL_MACHINERY | LSE:IQE | IQE plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Producer Manufacturing / Industrial Machinery | https://scanner.tradingview.com/uk/scan |
| 45_B ELECTRICAL_PRODUCTS | LSE:SMIN | Smiths Group Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Producer Manufacturing / Electrical Products | https://scanner.tradingview.com/uk/scan |
| 45_B ELECTRICAL_PRODUCTS | LSE:ROSE | Rosebank Industries Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Producer Manufacturing / Electrical Products | https://scanner.tradingview.com/uk/scan |
| 45_C TRUCKS_CONSTRUCTION_FARM_MACHINERY | LSE:WEIR | Weir PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Producer Manufacturing / Trucks/Construction/Farm Machinery | https://scanner.tradingview.com/uk/scan |
| 45_D MISCELLANEOUS_MANUFACTURING | LSE:HILS | Hill & Smith PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Producer Manufacturing / Miscellaneous Manufacturing | https://scanner.tradingview.com/uk/scan |
| 45_E BUILDING_PRODUCTS | LSE:JHD | James Halstead plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Producer Manufacturing / Building Products | https://scanner.tradingview.com/uk/scan |
| 46_A FOOD_RETAIL | LSE:TSCO | Tesco PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Retail Trade / Food Retail | https://scanner.tradingview.com/uk/scan |
| 46_A FOOD_RETAIL | LSE:SBRY | J Sainsbury plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Retail Trade / Food Retail | https://scanner.tradingview.com/uk/scan |
| 46_B SPECIALTY_STORES | LSE:FRAS | Frasers Group PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Retail Trade / Specialty Stores | https://scanner.tradingview.com/uk/scan |
| 46_B SPECIALTY_STORES | LSE:DNLM | Dunelm Group plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Retail Trade / Specialty Stores | https://scanner.tradingview.com/uk/scan |
| 46_C DEPARTMENT_STORES | LSE:MKS | Marks and Spencer Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Retail Trade / Department Stores | https://scanner.tradingview.com/uk/scan |
| 46_D HOME_IMPROVEMENT_CHAINS | LSE:KGF | Kingfisher Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Retail Trade / Home Improvement Chains | https://scanner.tradingview.com/uk/scan |
| 46_E APPAREL_FOOTWEAR_RETAIL | LSE:JD. | JD Sports Fashion Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Retail Trade / Apparel/Footwear Retail | https://scanner.tradingview.com/uk/scan |
| 46_F DISCOUNT_STORES | LSE:BME | B&M European Value Retail PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Retail Trade / Discount Stores | https://scanner.tradingview.com/uk/scan |
| 46_G INTERNET_RETAIL | LSE:ASC | ASOS Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Retail Trade / Internet Retail | https://scanner.tradingview.com/uk/scan |
| 47_A INTERNET_SOFTWARE_SERVICES | LSE:INF | Informa Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Technology Services / Internet Software/Services | https://scanner.tradingview.com/uk/scan |
| 47_A INTERNET_SOFTWARE_SERVICES | LSE:RMV | Rightmove plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Technology Services / Internet Software/Services | https://scanner.tradingview.com/uk/scan |
| 47_A INTERNET_SOFTWARE_SERVICES | LSE:MOON | Moonpig Group Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Technology Services / Internet Software/Services | https://scanner.tradingview.com/uk/scan |
| 47_B PACKAGED_SOFTWARE | LSE:SGE | Sage Group plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Technology Services / Packaged Software | https://scanner.tradingview.com/uk/scan |
| 47_B PACKAGED_SOFTWARE | LSE:PINE | Pinewood Technologies Group PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Technology Services / Packaged Software | https://scanner.tradingview.com/uk/scan |
| 47_C INFORMATION_TECHNOLOGY_SERVICES | LSE:CCC | Computacenter Plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Technology Services / Information Technology Services | https://scanner.tradingview.com/uk/scan |
| 47_C INFORMATION_TECHNOLOGY_SERVICES | LSE:KNOS | Kainos Group PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Technology Services / Information Technology Services | https://scanner.tradingview.com/uk/scan |
| 48_A AIRLINES | LSE:IAG | International Consolidated Airlines Group SA | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Transportation / Airlines | https://scanner.tradingview.com/uk/scan |
| 48_A AIRLINES | LSE:EZJ | easyJet plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Transportation / Airlines | https://scanner.tradingview.com/uk/scan |
| 48_B MARINE_SHIPPING | LSE:CKN | Clarkson PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Transportation / Marine Shipping | https://scanner.tradingview.com/uk/scan |
| 48_C OTHER_TRANSPORTATION | LSE:FGP | FirstGroup plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Transportation / Other Transportation | https://scanner.tradingview.com/uk/scan |
| 49_A ELECTRIC_UTILITIES | LSE:NG. | National Grid plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Utilities / Electric Utilities | https://scanner.tradingview.com/uk/scan |
| 49_A ELECTRIC_UTILITIES | LSE:TEP | Telecom Plus PLC | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Utilities / Electric Utilities | https://scanner.tradingview.com/uk/scan |
| 49_B WATER_UTILITIES | LSE:UU. | United Utilities Group PLC | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Utilities / Water Utilities | https://scanner.tradingview.com/uk/scan |
| 49_C GAS_DISTRIBUTORS | LSE:CNA | Centrica plc | THEME_LEADER | Largest researched company in this source industry by observed market capitalization; not a fundamental quality judgement. TradingView: Utilities / Gas Distributors | https://scanner.tradingview.com/uk/scan |
| 49_C GAS_DISTRIBUTORS | LSE:DCC | DCC Energy Plc | INDEPENDENT_SENSOR | Measured factor R² score at most 50; adds residual observation within this source classification. TradingView: Utilities / Gas Distributors | https://scanner.tradingview.com/uk/scan |
