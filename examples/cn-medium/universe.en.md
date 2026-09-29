# CN Ticker Universe

- Profile: Medium
- Facts as of: 2026-09-29
- Version: `165b1f485b79`
- Tickers: 210
- Themes: 79
- Stability: 0.99 · 207 / 210 · ±1%
- Partially scored: 210 / 210
- Largest theme: 11_A · 6 · 3% · weighted share 4
- TradingView tokens: 289 / 1000
- Rejected or unselected candidates: 1131
- Validation: PASS

- 真实记录获取于 2026-09-29，完整日行情截止 2026-09-28。这是范围已披露的研究子集，不是全市场完成筛查的结论。
- 请求 1351 份行情，取得 1341 份，缺失或被排除 10 份；候选只使用成功核验的记录。
- 主题领先角色依据观察到的市值；未虚构 quality 或 heat 分数，评分缺项和桶比例警告原样保留。
- 主题权重按研究成员数平方根计算，经中位数归一化后截于 0.5–4；这是观察席位的研究判断，不是资金配置权重。
- 行业来自数据提供方的分类，仍需研究复核。
- 有活跃报价不等于已排除所有监管不利状态。
- 成交额为原始收盘价乘成交量的代理量，并非交易所公布的实际成交额。
- 本次行情候选集只是上市清单的子集。
- 同行因子采用剔除自身的等权篮子；少于两个有效同行时不生成因子指标，也不退回宽基指数。单一成员可作广度观察，不可冒充独立或 beta 传感器。
- 沿用旧池 78 个细分股票驱动主题，并重新核验现有成员的上市与行情；未逐项重做公司业务尽调。未映射股票在 Heavy 层采用来源行业分类。旧分类来源：big-apple ticker-pool/cn.txt，修订 007b118。
- A/H 双重上市的人民币 A 股按独立市场保留，不因数据源把港股标为全球 primary 而被误删。

## Roles

| Role | Count |
|---|---:|
| BENCHMARK | 3 |
| BETA_SATELLITE | 23 |
| BREADTH_PROXY | 16 |
| INDEPENDENT_SENSOR | 90 |
| THEME_LEADER | 78 |

## Themes

| Code | Group | Theme | Level | Count |
|---|---|---|---:|---:|
| 00_A | 市场基准 | CORE_GAUGES | 1 | 3 |
| 10_A | AI算力基础设施 | OPTICAL_MODULES | 1 | 5 |
| 10_B | AI算力基础设施 | AI_SERVERS_PCB | 2 | 3 |
| 10_C | AI算力基础设施 | DATA_CENTRES | 2 | 2 |
| 10_D | AI算力基础设施 | LIQUID_COOLING | 2 | 2 |
| 10_E | AI算力基础设施 | DATACENTRE_POWER | 2 | 2 |
| 11_A | 半导体 | SEMICONDUCTOR_EQUIPMENT | 1 | 6 |
| 11_B | 半导体 | SEMICONDUCTOR_MATERIALS | 2 | 2 |
| 11_C | 半导体 | FOUNDRIES | 2 | 2 |
| 11_D | 半导体 | PACKAGING_TESTING | 2 | 2 |
| 11_E | 半导体 | COMPUTE_CHIPS | 2 | 2 |
| 11_F | 半导体 | MEMORY_CONTROLLERS | 2 | 2 |
| 11_G | 半导体 | ANALOG_POWER_RF | 2 | 2 |
| 11_H | 半导体 | IMAGE_COMMUNICATION_SOC | 2 | 2 |
| 11_J | 半导体 | PASSIVE_COMPONENTS | 2 | 2 |
| 12_A | 软件与数字经济 | AI_APPLICATIONS | 1 | 4 |
| 12_B | 软件与数字经济 | ENTERPRISE_INDUSTRIAL_SOFTWARE | 2 | 2 |
| 12_C | 软件与数字经济 | FINANCIAL_IT | 2 | 2 |
| 12_D | 软件与数字经济 | DOMESTIC_IT_SECURITY_QUANTUM | 2 | 2 |
| 12_F | 软件与数字经济 | MACHINE_VISION_AIOT | 2 | 3 |
| 13_A | 机械与自动化 | ROBOT_COMPONENTS | 1 | 5 |
| 13_B | 机械与自动化 | SERVO_MOTION_CONTROL | 2 | 2 |
| 13_C | 机械与自动化 | ROBOT_SYSTEMS | 2 | 2 |
| 13_D | 机械与自动化 | AUTOMATION_LASER_EQUIPMENT | 2 | 2 |
| 13_E | 机械与自动化 | SENSORS_ACTUATORS | 2 | 2 |
| 13_F | 机械与自动化 | CONSTRUCTION_MACHINERY | 2 | 2 |
| 14_A | 军工与航空航天 | MILITARY_AIRCRAFT_ENGINES | 1 | 3 |
| 14_B | 军工与航空航天 | DEFENCE_ELECTRONICS | 2 | 2 |
| 14_C | 军工与航空航天 | SATELLITE_COMMUNICATIONS | 2 | 2 |
| 14_E | 军工与航空航天 | DEFENCE_MATERIALS | 2 | 2 |
| 15_A | 汽车 | AUTOMAKERS | 1 | 5 |
| 15_B | 汽车 | SMART_AUTO_COMPONENTS | 2 | 3 |
| 16_A | 电池与新能源 | TRACTION_BATTERIES | 1 | 4 |
| 16_B | 电池与新能源 | BATTERY_MATERIALS | 2 | 2 |
| 16_C | 电池与新能源 | LITHIUM_RESOURCES | 2 | 2 |
| 16_D | 电池与新能源 | BATTERY_EQUIPMENT | 2 | 2 |
| 16_E | 电池与新能源 | SOLAR_MANUFACTURING | 2 | 2 |
| 16_F | 电池与新能源 | SOLAR_EQUIPMENT_MATERIALS | 2 | 2 |
| 16_G | 电池与新能源 | INVERTERS_STORAGE | 2 | 2 |
| 16_H | 电池与新能源 | WIND_POWER | 2 | 2 |
| 17_A | 电网与电力 | GRID_GENERATION_EQUIPMENT | 1 | 5 |
| 17_B | 电网与电力 | DISTRIBUTION_CHARGING_METERS | 2 | 2 |
| 17_C | 电网与电力 | POWER_GENERATION | 2 | 3 |
| 18_A | 医疗健康 | INNOVATIVE_DRUGS_BIO | 1 | 6 |
| 18_B | 医疗健康 | CRO_CDMO | 2 | 2 |
| 18_C | 医疗健康 | MEDICAL_DEVICES_AESTHETICS | 2 | 3 |
| 18_D | 医疗健康 | MEDICAL_SERVICES_TESTING | 2 | 2 |
| 18_E | 医疗健康 | CHINESE_MEDICINE_OTC | 2 | 2 |
| 18_F | 医疗健康 | DIVERSIFIED_PHARMA | 2 | 2 |
| 19_A | 金融 | BROKERS | 1 | 4 |
| 19_B | 金融 | BANKS | 2 | 3 |
| 19_C | 金融 | INSURANCE | 2 | 2 |
| 20_A | 金属与材料 | GOLD_MINING | 1 | 5 |
| 20_B | 金属与材料 | INDUSTRIAL_METALS_STEEL | 2 | 3 |
| 20_C | 金属与材料 | RARE_EARTH_MINOR_METALS | 2 | 3 |
| 20_D | 金属与材料 | COBALT_NICKEL_RECYCLING | 2 | 2 |
| 20_E | 金属与材料 | ADVANCED_NONMETALS | 2 | 2 |
| 21_A | 能源与化工 | COAL | 1 | 4 |
| 21_B | 能源与化工 | OIL_GAS | 2 | 2 |
| 21_C | 能源与化工 | CHEMICAL_MATERIALS | 2 | 3 |
| 22_A | 运输与基础设施 | SHIPPING | 1 | 4 |
| 22_B | 运输与基础设施 | SHIPBUILDING_OFFSHORE | 2 | 2 |
| 22_D | 运输与基础设施 | RAIL_ROADS | 2 | 2 |
| 22_E | 运输与基础设施 | CONSTRUCTION_INFRASTRUCTURE | 2 | 2 |
| 22_F | 运输与基础设施 | TELECOM_OPERATORS | 2 | 2 |
| 22_G | 运输与基础设施 | AIRLINES_AIRPORTS | 2 | 2 |
| 23_A | 房地产 | REAL_ESTATE | 1 | 4 |
| 24_A | 消费 | ALCOHOL | 1 | 5 |
| 24_B | 消费 | FOOD_BEVERAGES | 2 | 3 |
| 24_C | 消费 | HOME_APPLIANCES | 2 | 2 |
| 24_D | 消费 | HOME_FURNISHINGS | 2 | 2 |
| 24_E | 消费 | TOURISM_DUTY_FREE_HOTELS | 2 | 1 |
| 24_F | 消费 | JEWELLERY_RETAIL | 2 | 2 |
| 24_G | 消费 | CONSUMER_EXPORT_BRANDS | 2 | 2 |
| 24_H | 消费 | BEAUTY_PERSONAL_CARE | 2 | 1 |
| 25_A | 消费电子与传媒 | CONSUMER_ELECTRONICS_DISPLAYS | 1 | 4 |
| 25_B | 消费电子与传媒 | GAMES | 2 | 2 |
| 25_C | 消费电子与传媒 | MEDIA_ADVERTISING_EDUCATION | 2 | 2 |
| 26_A | 农业 | AGRICULTURE | 1 | 4 |
| 30_A | 商业服务 | MISCELLANEOUS_COMMERCIAL_SERVICES | 3 | 0 |
| 30_B | 商业服务 | ADVERTISING_MARKETING_SERVICES | 3 | 0 |
| 30_C | 商业服务 | COMMERCIAL_PRINTING_FORMS | 3 | 0 |
| 30_D | 商业服务 | PERSONNEL_SERVICES | 3 | 0 |
| 31_A | 通信 | WIRELESS_TELECOMMUNICATIONS | 3 | 0 |
| 31_B | 通信 | MAJOR_TELECOMMUNICATIONS | 3 | 0 |
| 32_A | 耐用消费 | HOME_FURNISHINGS | 3 | 0 |
| 32_B | 耐用消费 | MOTOR_VEHICLES | 3 | 0 |
| 32_C | 耐用消费 | ELECTRONICS_APPLIANCES | 3 | 0 |
| 32_D | 耐用消费 | AUTOMOTIVE_AFTERMARKET | 3 | 0 |
| 32_E | 耐用消费 | HOMEBUILDING | 3 | 0 |
| 32_F | 耐用消费 | RECREATIONAL_PRODUCTS | 3 | 0 |
| 32_G | 耐用消费 | TOOLS_HARDWARE | 3 | 0 |
| 32_H | 耐用消费 | OTHER_CONSUMER_SPECIALTIES | 3 | 0 |
| 33_A | 日常消费 | FOOD_SPECIALTY_CANDY | 3 | 0 |
| 33_B | 日常消费 | APPAREL_FOOTWEAR | 3 | 0 |
| 33_C | 日常消费 | FOOD_MEAT_FISH_DAIRY | 3 | 0 |
| 33_D | 日常消费 | BEVERAGES_ALCOHOLIC | 3 | 0 |
| 33_E | 日常消费 | FOOD_MAJOR_DIVERSIFIED | 3 | 0 |
| 33_F | 日常消费 | CONSUMER_SUNDRIES | 3 | 0 |
| 33_G | 日常消费 | HOUSEHOLD_PERSONAL_CARE | 3 | 0 |
| 33_H | 日常消费 | BEVERAGES_NON_ALCOHOLIC | 3 | 0 |
| 34_A | 消费服务 | PUBLISHING_BOOKS_MAGAZINES | 3 | 0 |
| 34_B | 消费服务 | CABLE_SATELLITE_TV | 3 | 0 |
| 34_C | 消费服务 | OTHER_CONSUMER_SERVICES | 3 | 0 |
| 34_D | 消费服务 | MOVIES_ENTERTAINMENT | 3 | 0 |
| 34_E | 消费服务 | HOTELS_RESORTS_CRUISE_LINES | 3 | 0 |
| 34_F | 消费服务 | RESTAURANTS | 3 | 0 |
| 34_G | 消费服务 | BROADCASTING | 3 | 0 |
| 34_H | 消费服务 | PUBLISHING_NEWSPAPERS | 3 | 0 |
| 34_I | 消费服务 | CASINOS_GAMING | 3 | 0 |
| 35_A | 分销 | WHOLESALE_DISTRIBUTORS | 3 | 0 |
| 35_B | 分销 | ELECTRONICS_DISTRIBUTORS | 3 | 0 |
| 35_C | 分销 | MEDICAL_DISTRIBUTORS | 3 | 0 |
| 35_D | 分销 | FOOD_DISTRIBUTORS | 3 | 0 |
| 36_A | 电子科技 | SEMICONDUCTORS | 3 | 0 |
| 36_B | 电子科技 | ELECTRONIC_COMPONENTS | 3 | 0 |
| 36_C | 电子科技 | ELECTRONIC_PRODUCTION_EQUIPMENT | 3 | 0 |
| 36_D | 电子科技 | ELECTRONIC_EQUIPMENT_INSTRUMENTS | 3 | 0 |
| 36_E | 电子科技 | COMPUTER_PERIPHERALS | 3 | 0 |
| 36_F | 电子科技 | TELECOMMUNICATIONS_EQUIPMENT | 3 | 0 |
| 36_G | 电子科技 | AEROSPACE_DEFENSE | 3 | 0 |
| 36_H | 电子科技 | COMPUTER_PROCESSING_HARDWARE | 3 | 0 |
| 36_I | 电子科技 | COMPUTER_COMMUNICATIONS | 3 | 0 |
| 37_A | 能源矿产 | COAL | 3 | 0 |
| 37_B | 能源矿产 | INTEGRATED_OIL | 3 | 0 |
| 37_C | 能源矿产 | OIL_GAS_PRODUCTION | 3 | 0 |
| 37_D | 能源矿产 | OIL_REFINING_MARKETING | 3 | 0 |
| 38_A | 金融 | MAJOR_BANKS | 3 | 0 |
| 38_B | 金融 | REGIONAL_BANKS | 3 | 0 |
| 38_C | 金融 | INVESTMENT_BANKS_BROKERS | 3 | 0 |
| 38_D | 金融 | INVESTMENT_MANAGERS | 3 | 0 |
| 38_E | 金融 | REAL_ESTATE_DEVELOPMENT | 3 | 0 |
| 38_F | 金融 | FINANCIAL_CONGLOMERATES | 3 | 0 |
| 38_G | 金融 | FINANCE_RENTAL_LEASING | 3 | 0 |
| 38_H | 金融 | LIFE_HEALTH_INSURANCE | 3 | 0 |
| 38_I | 金融 | REAL_ESTATE_INVESTMENT_TRUSTS | 3 | 0 |
| 39_A | 医疗服务 | HOSPITAL_NURSING_MANAGEMENT | 3 | 0 |
| 40_A | 医疗技术 | PHARMACEUTICALS_MAJOR | 3 | 0 |
| 40_B | 医疗技术 | BIOTECHNOLOGY | 3 | 0 |
| 40_C | 医疗技术 | MEDICAL_SPECIALTIES | 3 | 0 |
| 40_D | 医疗技术 | PHARMACEUTICALS_OTHER | 3 | 0 |
| 40_E | 医疗技术 | PHARMACEUTICALS_GENERIC | 3 | 0 |
| 41_A | 工业服务 | ENGINEERING_CONSTRUCTION | 3 | 0 |
| 41_B | 工业服务 | OILFIELD_SERVICES_EQUIPMENT | 3 | 0 |
| 41_C | 工业服务 | ENVIRONMENTAL_SERVICES | 3 | 0 |
| 41_D | 工业服务 | CONTRACT_DRILLING | 3 | 0 |
| 41_E | 工业服务 | OIL_GAS_PIPELINES | 3 | 0 |
| 42_A | 综合行业 | INVESTMENT_TRUSTS_MUTUAL_FUNDS | 3 | 0 |
| 43_A | 金属矿产 | OTHER_METALS_MINERALS | 3 | 0 |
| 43_B | 金属矿产 | STEEL | 3 | 0 |
| 43_C | 金属矿产 | ALUMINUM | 3 | 0 |
| 43_D | 金属矿产 | CONSTRUCTION_MATERIALS | 3 | 0 |
| 43_E | 金属矿产 | PRECIOUS_METALS | 3 | 0 |
| 43_F | 金属矿产 | FOREST_PRODUCTS | 3 | 0 |
| 44_A | 加工工业 | CHEMICALS_SPECIALTY | 3 | 0 |
| 44_B | 加工工业 | INDUSTRIAL_SPECIALTIES | 3 | 0 |
| 44_C | 加工工业 | TEXTILES | 3 | 0 |
| 44_D | 加工工业 | AGRICULTURAL_COMMODITIES_MILLING | 3 | 0 |
| 44_E | 加工工业 | CHEMICALS_MAJOR_DIVERSIFIED | 3 | 0 |
| 44_F | 加工工业 | CHEMICALS_AGRICULTURAL | 3 | 0 |
| 44_G | 加工工业 | CONTAINERS_PACKAGING | 3 | 0 |
| 44_H | 加工工业 | PULP_PAPER | 3 | 0 |
| 45_A | 装备制造 | ELECTRICAL_PRODUCTS | 3 | 0 |
| 45_B | 装备制造 | INDUSTRIAL_MACHINERY | 3 | 0 |
| 45_C | 装备制造 | METAL_FABRICATION | 3 | 0 |
| 45_D | 装备制造 | AUTO_PARTS_OEM | 3 | 0 |
| 45_E | 装备制造 | TRUCKS_CONSTRUCTION_FARM_MACHINERY | 3 | 0 |
| 45_F | 装备制造 | BUILDING_PRODUCTS | 3 | 0 |
| 45_G | 装备制造 | OFFICE_EQUIPMENT_SUPPLIES | 3 | 0 |
| 45_H | 装备制造 | MISCELLANEOUS_MANUFACTURING | 3 | 0 |
| 45_I | 装备制造 | INDUSTRIAL_CONGLOMERATES | 3 | 0 |
| 46_A | 零售 | DRUGSTORE_CHAINS | 3 | 0 |
| 46_B | 零售 | DEPARTMENT_STORES | 3 | 0 |
| 46_C | 零售 | INTERNET_RETAIL | 3 | 0 |
| 46_D | 零售 | FOOD_RETAIL | 3 | 0 |
| 46_E | 零售 | SPECIALTY_STORES | 3 | 0 |
| 46_F | 零售 | APPAREL_FOOTWEAR_RETAIL | 3 | 0 |
| 46_G | 零售 | CATALOG_SPECIALTY_DISTRIBUTION | 3 | 0 |
| 46_H | 零售 | ELECTRONICS_APPLIANCE_STORES | 3 | 0 |
| 47_A | 信息技术 | PACKAGED_SOFTWARE | 3 | 0 |
| 47_B | 信息技术 | INFORMATION_TECHNOLOGY_SERVICES | 3 | 0 |
| 47_C | 信息技术 | INTERNET_SOFTWARE_SERVICES | 3 | 0 |
| 47_D | 信息技术 | DATA_PROCESSING_SERVICES | 3 | 0 |
| 48_A | 交通运输 | OTHER_TRANSPORTATION | 3 | 0 |
| 48_B | 交通运输 | AIR_FREIGHT_COURIERS | 3 | 0 |
| 48_C | 交通运输 | AIRLINES | 3 | 0 |
| 48_D | 交通运输 | MARINE_SHIPPING | 3 | 0 |
| 48_E | 交通运输 | TRUCKING | 3 | 0 |
| 49_A | 公用事业 | ELECTRIC_UTILITIES | 3 | 0 |
| 49_B | 公用事业 | ALTERNATIVE_POWER_GENERATION | 3 | 0 |
| 49_C | 公用事业 | GAS_DISTRIBUTORS | 3 | 0 |
| 49_D | 公用事业 | WATER_UTILITIES | 3 | 0 |

## How the metrics were produced

| Metric | Basis | Method | Window |
|---|---|---|---|
| beta_stability | measured | 180 个重叠交易日窗口前后两半的 beta 一致程度 | 180d |
| beta_strength | measured | 对主题量尺的正向 OLS beta；beta 为 2.0 对应评分 100 | 180d |
| factor_r2 | measured | 日收益对逐标的主题量尺的 OLS R² | 180d |
| independence | measured | 由构建器按 100 − factor_r2 推导 | 180d |
| liquidity | measured | 最近 30 个交易日平均成交额的截面百分位，研究总体数量另列 | 30d |

## Why candidates did not make it

| Reason | Count |
|---|---:|
| outside_profile_coverage | 876 |
| not_selected_under_budget | 255 |

## Warnings

- satellite bucket holds 61% of the pool against a 25% target

## Members

| Theme | Ticker | Name | Role | Reason | Evidence |
|---|---|---|---|---|---|
| 00_A CORE_GAUGES | SSE:588000 | 科创50 | BENCHMARK | 保留市场／风格量尺；已核验当前报价和复权行情。 Broad market/style gauge | https://scanner.tradingview.com/china/scan |
| 00_A CORE_GAUGES | SSE:510300 | 沪深300ETF华泰柏瑞 | BENCHMARK | 保留市场／风格量尺；已核验当前报价和复权行情。 Broad market/style gauge | https://scanner.tradingview.com/china/scan |
| 00_A CORE_GAUGES | SSE:510500 | 中证500ETF南方 | BENCHMARK | 保留市场／风格量尺；已核验当前报价和复权行情。 Broad market/style gauge | https://scanner.tradingview.com/china/scan |
| 10_A OPTICAL_MODULES | SZSE:300308 | 中际旭创 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：10_A_光模块；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_A OPTICAL_MODULES | SZSE:002281 | 光迅科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：10_A_光模块；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_A OPTICAL_MODULES | SZSE:300570 | 太辰光 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：10_A_光模块；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_A OPTICAL_MODULES | SZSE:300502 | 新易盛 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：10_A_光模块；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_A OPTICAL_MODULES | SSE:688498 | 源杰科技 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：10_A_光模块；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_B AI_SERVERS_PCB | SSE:601138 | 工业富联 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：10_B_AI服务器及PCB；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_B AI_SERVERS_PCB | SZSE:000938 | 紫光股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：10_B_AI服务器及PCB；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_B AI_SERVERS_PCB | SZSE:301165 | 锐捷网络 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：10_B_AI服务器及PCB；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_C DATA_CENTRES | SZSE:300442 | 润泽科技 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：10_C_IDC；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_C DATA_CENTRES | SSE:603881 | 数据港 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：10_C_IDC；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_D LIQUID_COOLING | SZSE:002837 | 英维克 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：10_D_液冷温控；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_D LIQUID_COOLING | SZSE:300684 | 中石科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：10_D_液冷温控；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_E DATACENTRE_POWER | SZSE:002851 | 麦格米特 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：10_E_数据中心电源；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 10_E DATACENTRE_POWER | SZSE:002335 | 科华数据 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：10_E_数据中心电源；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_A SEMICONDUCTOR_EQUIPMENT | SZSE:002371 | 北方华创 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_A_设备厂务；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_A SEMICONDUCTOR_EQUIPMENT | SSE:688596 | 正帆科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：11_A_设备厂务；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_A SEMICONDUCTOR_EQUIPMENT | SZSE:300567 | 精测电子 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：11_A_设备厂务；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_A SEMICONDUCTOR_EQUIPMENT | SSE:688409 | 富创精密 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：11_A_设备厂务；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_A SEMICONDUCTOR_EQUIPMENT | SSE:688200 | 华峰测控 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：11_A_设备厂务；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_A SEMICONDUCTOR_EQUIPMENT | SZSE:300604 | 长川科技 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：11_A_设备厂务；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_B SEMICONDUCTOR_MATERIALS | SSE:688146 | 中船派瑞特气 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_B_半导体材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_B SEMICONDUCTOR_MATERIALS | SSE:600206 | 有研新材 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：11_B_半导体材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_C FOUNDRIES | SSE:688981 | 中芯国际 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_C_晶圆制造；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_C FOUNDRIES | SSE:688347 | 华虹宏力半导体 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：11_C_晶圆制造；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_D PACKAGING_TESTING | SSE:688820 | 盛合晶微 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_D_封装测试；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_D PACKAGING_TESTING | SZSE:002185 | 华天科技 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：11_D_封装测试；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_E COMPUTE_CHIPS | SSE:688256 | 寒武纪科技 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_E_算力芯片；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_E COMPUTE_CHIPS | SSE:688008 | 澜起科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：11_E_算力芯片；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_F MEMORY_CONTROLLERS | SSE:603986 | 兆易创新 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_F_存储控制；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_F MEMORY_CONTROLLERS | SZSE:001309 | 德明利 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：11_F_存储控制；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_G ANALOG_POWER_RF | SZSE:300661 | 圣邦股份 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_G_模拟功率射频；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_G ANALOG_POWER_RF | SZSE:300782 | 卓胜微 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：11_G_模拟功率射频；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_H IMAGE_COMMUNICATION_SOC | SSE:603501 | 豪威集团 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_H_CIS通信SOC；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_H IMAGE_COMMUNICATION_SOC | SSE:688213 | 思特威电子科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：11_H_CIS通信SOC；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_J PASSIVE_COMPONENTS | SZSE:300408 | 三环集团 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：11_J_被动元件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 11_J PASSIVE_COMPONENTS | SZSE:300285 | 国瓷材料 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：11_J_被动元件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_A AI_APPLICATIONS | SSE:688111 | 金山办公 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：12_A_AI应用；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_A AI_APPLICATIONS | SZSE:002261 | 拓维信息 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：12_A_AI应用；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_A AI_APPLICATIONS | SZSE:300418 | 昆仑万维 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：12_A_AI应用；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_A AI_APPLICATIONS | SZSE:002230 | 科大讯飞 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：12_A_AI应用；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_B ENTERPRISE_INDUSTRIAL_SOFTWARE | SSE:688777 | 中控技术 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：12_B_企业工业软件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_B ENTERPRISE_INDUSTRIAL_SOFTWARE | SZSE:301269 | 华大九天 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：12_B_企业工业软件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_C FINANCIAL_IT | SZSE:300059 | 东方财富 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：12_C_金融IT；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_C FINANCIAL_IT | SZSE:300033 | 同花顺 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：12_C_金融IT；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_D DOMESTIC_IT_SECURITY_QUANTUM | SZSE:300454 | 深信服 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：12_D_信创安全与量子；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_D DOMESTIC_IT_SECURITY_QUANTUM | SSE:600536 | 中国软件 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：12_D_信创安全与量子；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_F MACHINE_VISION_AIOT | SZSE:002415 | 海康威视 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：12_F_机器视觉AIOT；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_F MACHINE_VISION_AIOT | SSE:603236 | 移远通信 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：12_F_机器视觉AIOT；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 12_F MACHINE_VISION_AIOT | SSE:688001 | 苏州华兴源创科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：12_F_机器视觉AIOT；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_A ROBOT_COMPONENTS | SZSE:002050 | 三花智控 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：13_A_机器人零部件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_A ROBOT_COMPONENTS | SSE:603308 | 应流股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：13_A_机器人零部件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_A ROBOT_COMPONENTS | SZSE:002896 | 中大力德 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：13_A_机器人零部件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_A ROBOT_COMPONENTS | SSE:688017 | 绿的谐波 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：13_A_机器人零部件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_A ROBOT_COMPONENTS | SSE:603667 | 五洲新春 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：13_A_机器人零部件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_B SERVO_MOTION_CONTROL | SZSE:300124 | 汇川技术 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：13_B_伺服运动控制；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_B SERVO_MOTION_CONTROL | SZSE:300503 | 昊志机电 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：13_B_伺服运动控制；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_C ROBOT_SYSTEMS | SZSE:002747 | 埃斯顿 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：13_C_机器人本体；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_C ROBOT_SYSTEMS | SZSE:300607 | 拓斯达 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：13_C_机器人本体；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_D AUTOMATION_LASER_EQUIPMENT | SZSE:000988 | 华工科技 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：13_D_工业自动化与激光装备；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_D AUTOMATION_LASER_EQUIPMENT | SZSE:002008 | 大族激光 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：13_D_工业自动化与激光装备；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_E SENSORS_ACTUATORS | SSE:688002 | 睿创微纳 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：13_E_传感执行器；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_E SENSORS_ACTUATORS | SSE:688322 | 奥比中光 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：13_E_传感执行器；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_F CONSTRUCTION_MACHINERY | SSE:600031 | 三一重工 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：13_F_工程机械；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 13_F CONSTRUCTION_MACHINERY | SSE:601100 | 恒立液压 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：13_F_工程机械；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_A MILITARY_AIRCRAFT_ENGINES | SSE:600760 | 中航沈飞 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：14_A_军机航发；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_A MILITARY_AIRCRAFT_ENGINES | SSE:600893 | 航发动力 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：14_A_军机航发；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_A MILITARY_AIRCRAFT_ENGINES | SSE:688297 | 中航无人机 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：14_A_军机航发；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_B DEFENCE_ELECTRONICS | SZSE:002179 | 中航光电 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：14_B_军工电子；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_B DEFENCE_ELECTRONICS | SSE:600879 | 航天电子 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：14_B_军工电子；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_C SATELLITE_COMMUNICATIONS | SSE:601698 | 中国卫通 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：14_C_卫星通信；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_C SATELLITE_COMMUNICATIONS | SZSE:001270 | 铖昌科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：14_C_卫星通信；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_E DEFENCE_MATERIALS | SSE:688122 | 西部超导 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：14_E_军工材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 14_E DEFENCE_MATERIALS | SSE:688281 | 华秦科技实业 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：14_E_军工材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 15_A AUTOMAKERS | SZSE:002594 | 比亚迪 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：15_A_整车；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 15_A AUTOMAKERS | SZSE:000338 | 潍柴动力 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：15_A_整车；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 15_A AUTOMAKERS | SSE:600066 | 宇通客车 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：15_A_整车；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 15_A AUTOMAKERS | SSE:601127 | 赛力斯 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：15_A_整车；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 15_A AUTOMAKERS | SSE:600104 | 上汽集团 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：15_A_整车；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 15_B SMART_AUTO_COMPONENTS | SSE:600660 | 福耀玻璃 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：15_B_智能汽车零部件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 15_B SMART_AUTO_COMPONENTS | SZSE:002126 | 银轮股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：15_B_智能汽车零部件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 15_B SMART_AUTO_COMPONENTS | SSE:601689 | 拓普集团 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：15_B_智能汽车零部件；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_A TRACTION_BATTERIES | SZSE:300750 | 宁德时代 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：16_A_动力电池；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_A TRACTION_BATTERIES | SZSE:002245 | 蔚蓝锂芯 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_A_动力电池；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_A TRACTION_BATTERIES | SZSE:300207 | 欣旺达 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_A_动力电池；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_A TRACTION_BATTERIES | SZSE:002074 | 国轩高科 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_A_动力电池；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_B BATTERY_MATERIALS | SZSE:002709 | 天赐材料 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：16_B_锂电材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_B BATTERY_MATERIALS | SZSE:002407 | 多氟多 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_B_锂电材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_C LITHIUM_RESOURCES | SZSE:000792 | 盐湖股份 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：16_C_锂资源；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_C LITHIUM_RESOURCES | SZSE:002738 | 中矿资源 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：16_C_锂资源；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_D BATTERY_EQUIPMENT | SZSE:300450 | 先导智能 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：16_D_锂电设备结构；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_D BATTERY_EQUIPMENT | SSE:688700 | 东威科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_D_锂电设备结构；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_E SOLAR_MANUFACTURING | SSE:601012 | 隆基绿能 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：16_E_光伏主链；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_E SOLAR_MANUFACTURING | SZSE:002129 | TCL中环 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_E_光伏主链；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_F SOLAR_EQUIPMENT_MATERIALS | SZSE:300757 | 罗博特科 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：16_F_光伏设备材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_F SOLAR_EQUIPMENT_MATERIALS | SZSE:300724 | 捷佳伟创 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_F_光伏设备材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_G INVERTERS_STORAGE | SZSE:300274 | 阳光电源 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：16_G_逆变器储能；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_G INVERTERS_STORAGE | SSE:605117 | 德业股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_G_逆变器储能；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_H WIND_POWER | SZSE:002202 | 金风科技 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：16_H_风电产业链；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 16_H WIND_POWER | SZSE:002487 | 大金重工 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：16_H_风电产业链；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_A GRID_GENERATION_EQUIPMENT | SSE:600487 | 亨通光电 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：17_A_电网与发电设备；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_A GRID_GENERATION_EQUIPMENT | SSE:600522 | 中天科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：17_A_电网与发电设备；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_A GRID_GENERATION_EQUIPMENT | SZSE:002028 | 思源电气 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：17_A_电网与发电设备；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_A GRID_GENERATION_EQUIPMENT | SSE:600089 | 特变电工 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：17_A_电网与发电设备；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_A GRID_GENERATION_EQUIPMENT | SSE:600885 | 宏发股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：17_A_电网与发电设备；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_B DISTRIBUTION_CHARGING_METERS | SSE:600406 | 国电南瑞 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：17_B_配网充电表计；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_B DISTRIBUTION_CHARGING_METERS | SZSE:300001 | 特锐德 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：17_B_配网充电表计；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_C POWER_GENERATION | SSE:600900 | 长江电力 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：17_C_电力运营；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_C POWER_GENERATION | SSE:601985 | 中国核电 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：17_C_电力运营；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 17_C POWER_GENERATION | SSE:600886 | 国投电力 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：17_C_电力运营；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_A INNOVATIVE_DRUGS_BIO | SSE:600276 | 恒瑞医药 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：18_A_创新药生物；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_A INNOVATIVE_DRUGS_BIO | SZSE:300558 | 贝达药业 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_A_创新药生物；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_A INNOVATIVE_DRUGS_BIO | SSE:688578 | 艾力斯医药科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_A_创新药生物；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_A INNOVATIVE_DRUGS_BIO | SSE:688266 | 泽璟制药 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_A_创新药生物；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_A INNOVATIVE_DRUGS_BIO | SSE:688506 | 百利天恒药业 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_A_创新药生物；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_A INNOVATIVE_DRUGS_BIO | SSE:688336 | 三生国健 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_A_创新药生物；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_B CRO_CDMO | SSE:603259 | 药明康德 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：18_B_CXO_CDMO；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_B CRO_CDMO | SSE:603127 | 昭衍新药 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：18_B_CXO_CDMO；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_C MEDICAL_DEVICES_AESTHETICS | SZSE:300760 | 迈瑞医疗 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：18_C_医疗器械医美；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_C MEDICAL_DEVICES_AESTHETICS | SSE:688301 | 奕瑞科技股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_C_医疗器械医美；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_C MEDICAL_DEVICES_AESTHETICS | SSE:688617 | 惠泰医疗 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_C_医疗器械医美；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_D MEDICAL_SERVICES_TESTING | SZSE:300015 | 爱尔眼科 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：18_D_医疗服务检验；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_D MEDICAL_SERVICES_TESTING | SZSE:002044 | 美年健康 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_D_医疗服务检验；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_E CHINESE_MEDICINE_OTC | SZSE:000538 | 云南白药 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：18_E_中药OTC；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_E CHINESE_MEDICINE_OTC | SSE:600436 | 片仔癀 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_E_中药OTC；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_F DIVERSIFIED_PHARMA | SZSE:002422 | 科伦药业 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：18_F_综合药企；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 18_F DIVERSIFIED_PHARMA | SZSE:002294 | 信立泰 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：18_F_综合药企；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_A BROKERS | SSE:600030 | 中信证券 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：19_A_券商；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_A BROKERS | SZSE:000783 | 长江证券 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：19_A_券商；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_A BROKERS | SZSE:000776 | 广发证券 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：19_A_券商；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_A BROKERS | SSE:601211 | 国泰海通 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：19_A_券商；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_B BANKS | SSE:601398 | 工商银行 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：19_B_银行；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_B BANKS | SZSE:002142 | 宁波银行 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：19_B_银行；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_B BANKS | SSE:601288 | 农业银行 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：19_B_银行；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_C INSURANCE | SSE:601628 | 中国人寿 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：19_C_保险；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 19_C INSURANCE | SSE:601336 | 新华保险 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：19_C_保险；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_A GOLD_MINING | SSE:601899 | 紫金矿业 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：20_A_黄金矿业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_A GOLD_MINING | SZSE:002155 | 湖南黄金 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：20_A_黄金矿业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_A GOLD_MINING | SSE:600988 | 赤峰黄金 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：20_A_黄金矿业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_A GOLD_MINING | SSE:600547 | 山东黄金 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：20_A_黄金矿业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_A GOLD_MINING | SZSE:000975 | 山金国际 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：20_A_黄金矿业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_B INDUSTRIAL_METALS_STEEL | SSE:603993 | 洛阳钼业 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：20_B_工业金属钢铁；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_B INDUSTRIAL_METALS_STEEL | SSE:600019 | 宝钢股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：20_B_工业金属钢铁；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_B INDUSTRIAL_METALS_STEEL | SSE:601168 | 西部矿业 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：20_B_工业金属钢铁；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_C RARE_EARTH_MINOR_METALS | SSE:600111 | 北方稀土 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：20_C_稀土小金属；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_C RARE_EARTH_MINOR_METALS | SZSE:000603 | 盛达资源 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：20_C_稀土小金属；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_C RARE_EARTH_MINOR_METALS | SSE:600549 | 厦门钨业 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：20_C_稀土小金属；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_D COBALT_NICKEL_RECYCLING | SSE:603799 | 华友钴业 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：20_D_钴镍资源回收；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_D COBALT_NICKEL_RECYCLING | SSE:600711 | 盛屯矿业 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：20_D_钴镍资源回收；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_E ADVANCED_NONMETALS | SSE:600176 | 中国巨石 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：20_E_高端非金属；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 20_E ADVANCED_NONMETALS | SSE:600516 | 方大炭素 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：20_E_高端非金属；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_A COAL | SSE:601088 | 中国神华 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：21_A_煤炭；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_A COAL | SSE:600188 | 兖矿能源 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：21_A_煤炭；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_A COAL | SSE:601898 | 中煤能源 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：21_A_煤炭；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_A COAL | SZSE:000983 | 山西焦煤 | BREADTH_PROXY | 来自已核验候选集，补充行业观察广度；不据此声称基本面优质。 沿用旧池研究分类：21_A_煤炭；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_B OIL_GAS | SSE:601857 | 中国石油 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：21_B_石油天然气；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_B OIL_GAS | SSE:600256 | 广汇能源 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：21_B_石油天然气；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_C CHEMICAL_MATERIALS | SSE:600309 | 万华化学 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：21_C_化工材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_C CHEMICAL_MATERIALS | SSE:600989 | 宝丰能源 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：21_C_化工材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 21_C CHEMICAL_MATERIALS | SSE:600141 | 兴发集团 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：21_C_化工材料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_A SHIPPING | SSE:601919 | 中远海控 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：22_A_航运；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_A SHIPPING | SSE:603565 | 中谷物流 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：22_A_航运；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_A SHIPPING | SSE:600428 | 中远海特 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：22_A_航运；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_A SHIPPING | SSE:601866 | 中远海发 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：22_A_航运；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_B SHIPBUILDING_OFFSHORE | SSE:600150 | 中国船舶 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：22_B_船舶海工；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_B SHIPBUILDING_OFFSHORE | SSE:601808 | 中海油服 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：22_B_船舶海工；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_D RAIL_ROADS | SSE:601816 | 京沪高铁 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：22_D_铁路公路；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_D RAIL_ROADS | SSE:601006 | 大秦铁路 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：22_D_铁路公路；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_E CONSTRUCTION_INFRASTRUCTURE | SSE:601668 | 中国建筑 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：22_E_建筑基建；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_E CONSTRUCTION_INFRASTRUCTURE | SSE:601611 | 中国核建 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：22_E_建筑基建；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_F TELECOM_OPERATORS | SSE:600941 | 中国移动 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：22_F_电信运营；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_F TELECOM_OPERATORS | SSE:601728 | 中国电信 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：22_F_电信运营；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_G AIRLINES_AIRPORTS | SSE:601111 | 中国国航 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：22_G_民航机场；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 22_G AIRLINES_AIRPORTS | SSE:600004 | 白云机场 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：22_G_民航机场；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 23_A REAL_ESTATE | SSE:600048 | 保利发展 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：23_A_房地产；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 23_A REAL_ESTATE | SSE:600895 | 张江高科 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：23_A_房地产；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 23_A REAL_ESTATE | SZSE:002244 | 滨江集团 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：23_A_房地产；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 23_A REAL_ESTATE | SSE:601155 | 新城控股 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：23_A_房地产；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_A ALCOHOL | SSE:600519 | 贵州茅台 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：24_A_酒类；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_A ALCOHOL | SZSE:002568 | 百润股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：24_A_酒类；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_A ALCOHOL | SZSE:000596 | 古井贡酒 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：24_A_酒类；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_A ALCOHOL | SSE:603369 | 今世缘 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：24_A_酒类；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_A ALCOHOL | SSE:603198 | 迎驾贡酒 | BETA_SATELLITE | 对已披露因子具有实测正向、稳定 beta，为主题增加敏感度观察。 沿用旧池研究分类：24_A_酒类；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_B FOOD_BEVERAGES | SSE:603288 | 海天味业 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：24_B_食品饮料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_B FOOD_BEVERAGES | SSE:600887 | 伊利股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：24_B_食品饮料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_B FOOD_BEVERAGES | SSE:605499 | 东鹏饮料 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：24_B_食品饮料；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_C HOME_APPLIANCES | SZSE:000333 | 美的集团 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：24_C_家电；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_C HOME_APPLIANCES | SZSE:000651 | 格力电器 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：24_C_家电；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_D HOME_FURNISHINGS | SSE:603195 | 公牛集团 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：24_D_家居与民用电工；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_D HOME_FURNISHINGS | SSE:603833 | 欧派家居 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：24_D_家居与民用电工；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_E TOURISM_DUTY_FREE_HOTELS | SSE:601888 | 中国中免 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：24_E_旅游免税酒店；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_F JEWELLERY_RETAIL | SSE:600655 | 豫园股份 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：24_F_珠宝零售；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_F JEWELLERY_RETAIL | SSE:600916 | 中国黄金 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：24_F_珠宝零售；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_G CONSUMER_EXPORT_BRANDS | SZSE:300866 | 安克创新 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：24_G_品牌消费出海；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_G CONSUMER_EXPORT_BRANDS | SSE:688036 | 传音控股 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：24_G_品牌消费出海；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 24_H BEAUTY_PERSONAL_CARE | SSE:603605 | 珀莱雅 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：24_H_美妆个护；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 25_A CONSUMER_ELECTRONICS_DISPLAYS | SZSE:002475 | 立讯精密 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：25_A_消费电子与显示制造；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 25_A CONSUMER_ELECTRONICS_DISPLAYS | SZSE:000725 | 京东方Ａ | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：25_A_消费电子与显示制造；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 25_A CONSUMER_ELECTRONICS_DISPLAYS | SZSE:002241 | 歌尔股份 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：25_A_消费电子与显示制造；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 25_A CONSUMER_ELECTRONICS_DISPLAYS | SZSE:000100 | TCL科技 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：25_A_消费电子与显示制造；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 25_B GAMES | SZSE:002602 | 世纪华通 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：25_B_游戏；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 25_B GAMES | SSE:603444 | 吉比特 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：25_B_游戏；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 25_C MEDIA_ADVERTISING_EDUCATION | SZSE:002027 | 分众传媒 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：25_C_传媒广告教育；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 25_C MEDIA_ADVERTISING_EDUCATION | SZSE:300058 | 蓝色光标 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：25_C_传媒广告教育；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 26_A AGRICULTURE | SZSE:002714 | 牧原股份 | THEME_LEADER | 按观察日市值位居该研究主题前列；角色不代表已完成财务质量审查。 沿用旧池研究分类：26_A_农牧种业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 26_A AGRICULTURE | SSE:600598 | 北大荒 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：26_A_农牧种业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 26_A AGRICULTURE | SZSE:002311 | 海大集团 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：26_A_农牧种业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
| 26_A AGRICULTURE | SZSE:000998 | 隆平高科 | INDEPENDENT_SENSOR | 实测因子 R² 评分不高于 50，在已有分类内补充残差信息观察。 沿用旧池研究分类：26_A_农牧种业；本次重新核验上市与行情，未逐项重做业务尽调。 | https://scanner.tradingview.com/china/scan |
