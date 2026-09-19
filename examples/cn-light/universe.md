> 由 `python examples/build_examples.py` 从 `examples/seeds/cn.tsv` 生成。
> 这是一次 build 写出的 `.md` 产物，提交进仓库是为了不运行任何东西也能读到它。
> 其中所有指标数值都只作示意——见 [README.md](../README.md)。

# CN 标的池

- 档位：精简档
- 事实截至：2026-09-17
- 版本：`07d23f2bf129`
- 标的数：80
- 主题数：32
- 每主题上限：4
- TradingView 条目：112 / 1000
- 落选或被排除的候选：21
- 校验：通过

## 角色分布

| 角色 | 数量 |
|---|---:|
| 锚点 (ANCHOR) | 3 |
| 基准 (BENCHMARK) | 2 |
| 贝塔卫星 (BETA_SATELLITE) | 9 |
| 广度代理 (BREADTH_PROXY) | 2 |
| 独立观测 (INDEPENDENT_SENSOR) | 1 |
| 流动性观测 (LIQUIDITY_SENSOR) | 4 |
| 质量龙头 (QUALITY_LEADER) | 22 |
| 主题龙头 (THEME_LEADER) | 37 |

## 主题覆盖

| 编码 | 一级分类 | 主题 | 层级 | 数量 |
|---|---|---|---:|---:|
| 00_A | 市场基准 | BROAD_INDEX_ETF | 1 | 4 |
| 00_B | 市场基准 | SECTOR_ROTATION_ETF | 2 | 0 |
| 00_C | 市场基准 | THEMATIC_ETF | 3 | 0 |
| 10_A | 食品饮料 | BAIJIU | 1 | 4 |
| 10_B | 食品饮料 | FOOD_AND_DAIRY | 1 | 3 |
| 10_C | 食品饮料 | BEVERAGE_AND_BREWING | 2 | 0 |
| 10_D | 食品饮料 | CONDIMENTS_AND_SNACKS | 3 | 0 |
| 15_A | 农林牧渔 | LIVESTOCK_AND_FEED | 1 | 3 |
| 15_B | 农林牧渔 | SEED_AND_AGRITECH | 3 | 0 |
| 20_A | 金融 | LARGE_BANKS | 1 | 4 |
| 20_B | 金融 | BROKERS | 1 | 4 |
| 20_C | 金融 | INSURANCE | 1 | 3 |
| 20_D | 金融 | REGIONAL_BANKS | 2 | 0 |
| 20_E | 金融 | DIVERSIFIED_FINANCIALS | 3 | 0 |
| 25_A | 房地产 | PROPERTY_DEVELOPERS | 1 | 3 |
| 25_B | 房地产 | PROPERTY_SERVICES | 3 | 0 |
| 30_A | 新能源 | BATTERY_CHAIN | 1 | 4 |
| 30_B | 新能源 | PHOTOVOLTAIC | 1 | 4 |
| 30_C | 新能源 | POWER_EQUIPMENT | 1 | 2 |
| 30_D | 新能源 | WIND_POWER | 2 | 0 |
| 30_E | 新能源 | HYDROGEN_AND_STORAGE | 3 | 0 |
| 40_A | 汽车 | AUTO_OEM | 1 | 4 |
| 40_B | 汽车 | AUTO_PARTS | 1 | 2 |
| 40_C | 汽车 | COMMERCIAL_VEHICLES | 2 | 0 |
| 40_D | 汽车 | AUTO_ELECTRONICS | 3 | 0 |
| 50_A | 半导体与电子 | SEMICONDUCTORS | 1 | 4 |
| 50_B | 半导体与电子 | CONSUMER_ELECTRONICS_CHAIN | 1 | 4 |
| 50_C | 半导体与电子 | DISPLAY_AND_OPTICS | 1 | 1 |
| 50_D | 半导体与电子 | SEMICAP_AND_MATERIALS | 2 | 0 |
| 50_E | 半导体与电子 | PCB_AND_COMPONENTS | 2 | 0 |
| 60_A | 医药生物 | INNOVATIVE_PHARMA | 1 | 3 |
| 60_B | 医药生物 | MEDICAL_DEVICES | 1 | 2 |
| 60_C | 医药生物 | CRO_AND_CDMO | 1 | 1 |
| 60_D | 医药生物 | TCM_AND_GENERICS | 2 | 0 |
| 60_E | 医药生物 | VACCINES_AND_BIOLOGICS | 3 | 0 |
| 60_F | 医药生物 | PHARMACY_AND_DISTRIBUTION | 3 | 0 |
| 65_A | 国防军工 | AEROSPACE_AND_DEFENSE | 1 | 2 |
| 65_B | 国防军工 | DEFENSE_ELECTRONICS | 2 | 0 |
| 70_A | 资源品 | NONFERROUS_METALS | 1 | 2 |
| 70_B | 资源品 | COAL_AND_OIL | 1 | 3 |
| 70_C | 资源品 | CHEMICALS | 1 | 1 |
| 70_D | 资源品 | STEEL_AND_BUILDING_MATERIALS | 2 | 0 |
| 70_E | 资源品 | RARE_EARTH_AND_LITHIUM | 2 | 0 |
| 70_F | 资源品 | GOLD_MINERS | 3 | 0 |
| 80_A | 机械与基建 | CONSTRUCTION_AND_RAIL | 1 | 1 |
| 80_B | 机械与基建 | MACHINERY | 1 | 1 |
| 80_C | 机械与基建 | ROBOTICS_AND_AUTOMATION | 2 | 0 |
| 80_D | 机械与基建 | ENGINEERING_SERVICES | 3 | 0 |
| 85_A | 公用事业与交运 | POWER_UTILITIES | 1 | 1 |
| 85_B | 公用事业与交运 | LOGISTICS_AND_SHIPPING | 1 | 2 |
| 85_C | 公用事业与交运 | AIRLINES_AND_AIRPORTS | 2 | 0 |
| 85_D | 公用事业与交运 | WATER_AND_ENVIRONMENT | 3 | 0 |
| 85_E | 公用事业与交运 | HIGHWAYS_AND_PORTS | 3 | 0 |
| 90_A | 消费服务 | HOME_APPLIANCES | 1 | 2 |
| 90_B | 消费服务 | TRAVEL_AND_RETAIL | 1 | 2 |
| 90_C | 消费服务 | APPAREL_AND_TEXTILES | 2 | 0 |
| 90_D | 消费服务 | EDUCATION_AND_SERVICES | 3 | 0 |
| 95_A | 通信与计算机 | TELECOM_OPERATORS | 1 | 1 |
| 95_B | 通信与计算机 | SOFTWARE_AND_AI | 1 | 1 |
| 95_C | 通信与计算机 | COMMUNICATION_EQUIPMENT | 2 | 0 |
| 95_D | 通信与计算机 | CLOUD_AND_IDC | 2 | 0 |
| 95_E | 通信与计算机 | FINTECH_SOFTWARE | 3 | 0 |
| 96_A | 传媒 | MEDIA_AND_GAMING | 1 | 2 |
| 96_B | 传媒 | PUBLISHING_AND_MARKETING | 3 | 0 |

## 指标是怎么来的

| 指标 | 口径 | 方法 | 窗口 |
|---|---|---|---|
| beta_stability | 实测 (measured) | beta 估计在窗口前后两半之间的一致程度 | 180d |
| beta_strength | 实测 (measured) | 对 SSE:510300 的 OLS beta 绝对值，beta 为 2.0 记 100 | 180d |
| heat | 判断 (judged) | 成交额跃升，须以交易所数据确认，单日波动不算 | — |
| independence | 实测 (measured) | 100 减去日收益对 SSE:510300 回归的 R² | 180d |
| liquidity | 实测 (measured) | 30 日日均成交额的截面分位 | 30d |
| quality | 规则与判断混合 (blended) | 上市时长与规模分位，叠加对经营持续性的判断 | — |

全部 80 个成员中有 64 个的 quality 由规则与判断各占 50% 和 50%。规则的一半读取上市时长、规模分位与不利标记；判断的一半是任何统计量都覆盖不到的部分。

## 候选未能入选的原因

| 理由 | 数量 |
|---|---:|
| 名额或主题上限已用尽 (not_selected_under_budget_or_theme_cap) | 18 |
| 品种类型被排除 (excluded_instrument_type) | 1 |
| 超出本档的覆盖层级 (outside_profile_coverage) | 1 |
| 与已有成员重复 (redundant_with_member) | 1 |

## 成员

| 主题 | 代码 | 名称 | 角色 | 理由 | 证据 |
|---|---|---|---|---|---|
| 00_A BROAD_INDEX_ETF | SSE:510300 | 沪深300ETF | 基准 (BENCHMARK) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 00_A BROAD_INDEX_ETF | SSE:510050 | 上证50ETF | 基准 (BENCHMARK) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 00_A BROAD_INDEX_ETF | SSE:588000 | 科创50ETF | 广度代理 (BREADTH_PROXY) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 00_A BROAD_INDEX_ETF | SZSE:159915 | 创业板ETF | 广度代理 (BREADTH_PROXY) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_A BAIJIU | SSE:600519 | 贵州茅台 | 锚点 (ANCHOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_A BAIJIU | SZSE:000858 | 五粮液 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_A BAIJIU | SSE:600809 | 山西汾酒 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_A BAIJIU | SZSE:000568 | 泸州老窖 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_B FOOD_AND_DAIRY | SSE:600887 | 伊利股份 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_B FOOD_AND_DAIRY | SSE:603288 | 海天味业 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_B FOOD_AND_DAIRY | SSE:600298 | 安琪酵母 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 15_A LIVESTOCK_AND_FEED | SZSE:002714 | 牧原股份 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 15_A LIVESTOCK_AND_FEED | SZSE:002311 | 海大集团 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 15_A LIVESTOCK_AND_FEED | SZSE:300498 | 温氏股份 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_A LARGE_BANKS | SSE:600036 | 招商银行 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_A LARGE_BANKS | SSE:601398 | 工商银行 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_A LARGE_BANKS | SSE:601288 | 农业银行 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_A LARGE_BANKS | SSE:601939 | 建设银行 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_B BROKERS | SSE:600030 | 中信证券 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_B BROKERS | SZSE:300059 | 东方财富 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_B BROKERS | SSE:601688 | 华泰证券 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_B BROKERS | SSE:600837 | 海通证券 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_C INSURANCE | SSE:601318 | 中国平安 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_C INSURANCE | SSE:601601 | 中国太保 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_C INSURANCE | SSE:601628 | 中国人寿 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 25_A PROPERTY_DEVELOPERS | SSE:600048 | 保利发展 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 25_A PROPERTY_DEVELOPERS | SZSE:001979 | 招商蛇口 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 25_A PROPERTY_DEVELOPERS | SZSE:000002 | 万科A | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_A BATTERY_CHAIN | SZSE:300750 | 宁德时代 | 锚点 (ANCHOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_A BATTERY_CHAIN | SZSE:300014 | 亿纬锂能 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_A BATTERY_CHAIN | SZSE:002812 | 恩捷股份 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_A BATTERY_CHAIN | SZSE:002460 | 赣锋锂业 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_B PHOTOVOLTAIC | SSE:600438 | 通威股份 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_B PHOTOVOLTAIC | SSE:601012 | 隆基绿能 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_B PHOTOVOLTAIC | SSE:688599 | 天合光能 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_B PHOTOVOLTAIC | SZSE:002129 | TCL中环 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_C POWER_EQUIPMENT | SZSE:300124 | 汇川技术 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_C POWER_EQUIPMENT | SSE:688187 | 时代电气 | 流动性观测 (LIQUIDITY_SENSOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_A AUTO_OEM | SSE:601633 | 长城汽车 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_A AUTO_OEM | SZSE:002594 | 比亚迪 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_A AUTO_OEM | SSE:600104 | 上汽集团 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_A AUTO_OEM | SSE:601127 | 赛力斯 | 流动性观测 (LIQUIDITY_SENSOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_B AUTO_PARTS | SZSE:002475 | 立讯精密 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_B AUTO_PARTS | SSE:601689 | 拓普集团 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_A SEMICONDUCTORS | SSE:603501 | 韦尔股份 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_A SEMICONDUCTORS | SSE:688981 | 中芯国际 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_A SEMICONDUCTORS | SSE:603986 | 兆易创新 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_A SEMICONDUCTORS | SSE:688041 | 海光信息 | 流动性观测 (LIQUIDITY_SENSOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_B CONSUMER_ELECTRONICS_CHAIN | SZSE:002415 | 海康威视 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_B CONSUMER_ELECTRONICS_CHAIN | SZSE:002241 | 歌尔股份 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_B CONSUMER_ELECTRONICS_CHAIN | SSE:688036 | 传音控股 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_B CONSUMER_ELECTRONICS_CHAIN | SZSE:000725 | 京东方A | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_C DISPLAY_AND_OPTICS | SSE:600703 | 三安光电 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_A INNOVATIVE_PHARMA | SSE:600276 | 恒瑞医药 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_A INNOVATIVE_PHARMA | SZSE:000538 | 云南白药 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_A INNOVATIVE_PHARMA | SSE:600436 | 片仔癀 | 独立观测 (INDEPENDENT_SENSOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_B MEDICAL_DEVICES | SZSE:300760 | 迈瑞医疗 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_B MEDICAL_DEVICES | SSE:688271 | 联影医疗 | 流动性观测 (LIQUIDITY_SENSOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_C CRO_AND_CDMO | SSE:603259 | 药明康德 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 65_A AEROSPACE_AND_DEFENSE | SSE:600760 | 中航沈飞 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 65_A AEROSPACE_AND_DEFENSE | SSE:600893 | 航发动力 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_A NONFERROUS_METALS | SSE:601899 | 紫金矿业 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_A NONFERROUS_METALS | SSE:600111 | 北方稀土 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_B COAL_AND_OIL | SSE:601857 | 中国石油 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_B COAL_AND_OIL | SSE:601088 | 中国神华 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_B COAL_AND_OIL | SSE:601225 | 陕西煤业 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_C CHEMICALS | SZSE:002601 | 龙佰集团 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 80_A CONSTRUCTION_AND_RAIL | SSE:601668 | 中国建筑 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 80_B MACHINERY | SSE:600031 | 三一重工 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 85_A POWER_UTILITIES | SSE:600900 | 长江电力 | 锚点 (ANCHOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 85_B LOGISTICS_AND_SHIPPING | SZSE:002352 | 顺丰控股 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 85_B LOGISTICS_AND_SHIPPING | SSE:601919 | 中远海控 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 90_A HOME_APPLIANCES | SZSE:000333 | 美的集团 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 90_A HOME_APPLIANCES | SZSE:000651 | 格力电器 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 90_B TRAVEL_AND_RETAIL | SSE:601888 | 中国中免 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 90_B TRAVEL_AND_RETAIL | SSE:600009 | 上海机场 | 质量龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 95_A TELECOM_OPERATORS | SSE:600941 | 中国移动 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 95_B SOFTWARE_AND_AI | SZSE:002230 | 科大讯飞 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 96_A MEDIA_AND_GAMING | SZSE:002027 | 分众传媒 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 96_A MEDIA_AND_GAMING | SZSE:002555 | 三七互娱 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
