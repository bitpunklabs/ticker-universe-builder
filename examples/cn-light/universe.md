> 由 `python examples/build_examples.py` 从 `examples/seeds/cn.tsv` 生成。
> 这是一次 build 写出的 `.md` 产物,提交进仓库是为了不运行任何东西也能读到它。
> 其中所有指标数值都只作示意 — 见 [README.md](../README.md)。

# CN 标的池

- 档位: 轻量档
- 事实截止: 2026-09-17
- 版本: `b9a6036f930b`
- 标的数: 64
- 主题数: 18
- TradingView 条目: 82 / 1000
- 落选或被排除的候选: 23
- 校验: 通过

## 角色分布

| 角色 | 数量 |
|---|---:|
| 锚点 (ANCHOR) | 3 |
| 基准 (BENCHMARK) | 2 |
| 贝塔卫星 (BETA_SATELLITE) | 5 |
| 广度代理 (BREADTH_PROXY) | 3 |
| 流动性观测 (LIQUIDITY_SENSOR) | 1 |
| 质地龙头 (QUALITY_LEADER) | 27 |
| 主题龙头 (THEME_LEADER) | 23 |

## 主题覆盖

| 编码 | 一级分类 | 主题 | 层级 | 数量 |
|---|---|---|---:|---:|
| 00_A | 市场基准 | BROAD_INDEX_ETF | 1 | 4 |
| 10_A | 食品饮料 | BAIJIU | 1 | 4 |
| 10_B | 食品饮料 | FOOD_AND_DAIRY | 1 | 4 |
| 20_A | 金融 | LARGE_BANKS | 1 | 4 |
| 20_B | 金融 | BROKERS | 1 | 4 |
| 20_C | 金融 | INSURANCE | 1 | 3 |
| 30_A | 新能源 | BATTERY_CHAIN | 1 | 4 |
| 30_B | 新能源 | PHOTOVOLTAIC | 1 | 4 |
| 30_C | 新能源 | POWER_EQUIPMENT | 2 | 0 |
| 40_A | 汽车 | AUTO_OEM | 1 | 4 |
| 40_B | 汽车 | AUTO_PARTS | 2 | 0 |
| 50_A | 半导体与电子 | SEMICONDUCTORS | 1 | 4 |
| 50_B | 半导体与电子 | CONSUMER_ELECTRONICS_CHAIN | 1 | 4 |
| 50_C | 半导体与电子 | DISPLAY_AND_OPTICS | 2 | 0 |
| 60_A | 医药生物 | INNOVATIVE_PHARMA | 1 | 4 |
| 60_B | 医药生物 | MEDICAL_DEVICES | 2 | 0 |
| 60_C | 医药生物 | CRO_AND_CDMO | 2 | 0 |
| 70_A | 资源品 | NONFERROUS_METALS | 1 | 4 |
| 70_B | 资源品 | COAL_AND_OIL | 1 | 4 |
| 70_C | 资源品 | CHEMICALS | 2 | 0 |
| 80_A | 基建 | CONSTRUCTION_AND_RAIL | 1 | 1 |
| 80_B | 基建 | MACHINERY | 2 | 0 |
| 85_A | 公用事业与交运 | POWER_UTILITIES | 1 | 3 |
| 85_B | 公用事业与交运 | LOGISTICS_AND_SHIPPING | 2 | 0 |
| 90_A | 消费服务 | HOME_APPLIANCES | 1 | 2 |
| 90_B | 消费服务 | TRAVEL_AND_RETAIL | 2 | 0 |
| 95_A | 通信与计算机 | TELECOM_OPERATORS | 1 | 3 |
| 95_B | 通信与计算机 | SOFTWARE_AND_AI | 2 | 0 |

## 指标是怎么来的

| 指标 | 来路 | 方法 | 窗口 |
|---|---|---|---|
| beta_stability | 实测 (measured) | beta 估计在窗口前后两半之间的一致程度 | 180d |
| beta_strength | 实测 (measured) | 对 SSE:510300 的 OLS beta 绝对值,beta 为 2.0 记 100 | 180d |
| heat | 判断 (judged) | 成交额跃升,须以交易所数据确认,单日波动不算 | — |
| independence | 实测 (measured) | 100 减去日收益对 SSE:510300 回归的 R² | 180d |
| liquidity | 实测 (measured) | 30 日日均成交额的截面分位 | 30d |
| quality | 规则与判断混合 (blended) | 上市时长与规模分位,叠加对经营持续性的判断 | — |

全部 64 名成员中有 55 名的 quality 由规则与判断各占 50% 和 50%。规则的一半读取上市时长、规模分位与不利标记;判断的一半是任何统计量都覆盖不到的部分。

## 候选未能入选的原因

| 理由 | 数量 |
|---|---:|
| 超出本档的覆盖层级 (outside_profile_coverage) | 16 |
| 名额或主题上限已用尽 (not_selected_under_budget_or_theme_cap) | 5 |
| 品种类型被排除 (excluded_instrument_type) | 1 |
| 与已有成员重复 (redundant_with_member) | 1 |

## 提示

- member count 64 is below cn/light guidance 150

提示文本保留英文:它们指向策略字段与代码路径,`.validation.json` 里是同一份文本,便于逐字检索。

## 成员

| 主题 | 代码 | 名称 | 角色 | 理由 | 证据 |
|---|---|---|---|---|---|
| 00_A BROAD_INDEX_ETF | SSE:510050 | 上证50ETF | 基准 (BENCHMARK) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 00_A BROAD_INDEX_ETF | SSE:510300 | 沪深300ETF | 基准 (BENCHMARK) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 00_A BROAD_INDEX_ETF | SZSE:159915 | 创业板ETF | 广度代理 (BREADTH_PROXY) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 00_A BROAD_INDEX_ETF | SSE:588000 | 科创50ETF | 广度代理 (BREADTH_PROXY) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_A BAIJIU | SSE:600519 | 贵州茅台 | 锚点 (ANCHOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_A BAIJIU | SZSE:000858 | 五粮液 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_A BAIJIU | SSE:600809 | 山西汾酒 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_A BAIJIU | SZSE:000568 | 泸州老窖 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_B FOOD_AND_DAIRY | SSE:600887 | 伊利股份 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_B FOOD_AND_DAIRY | SSE:603288 | 海天味业 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_B FOOD_AND_DAIRY | SZSE:002714 | 牧原股份 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 10_B FOOD_AND_DAIRY | SSE:600298 | 安琪酵母 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_A LARGE_BANKS | SSE:601398 | 工商银行 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_A LARGE_BANKS | SSE:600036 | 招商银行 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_A LARGE_BANKS | SSE:601288 | 农业银行 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_A LARGE_BANKS | SSE:601939 | 建设银行 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_B BROKERS | SSE:600030 | 中信证券 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_B BROKERS | SZSE:300059 | 东方财富 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_B BROKERS | SSE:601688 | 华泰证券 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_B BROKERS | SSE:600837 | 海通证券 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_C INSURANCE | SSE:601318 | 中国平安 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_C INSURANCE | SSE:601628 | 中国人寿 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 20_C INSURANCE | SSE:601601 | 中国太保 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_A BATTERY_CHAIN | SZSE:300750 | 宁德时代 | 锚点 (ANCHOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_A BATTERY_CHAIN | SZSE:300014 | 亿纬锂能 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_A BATTERY_CHAIN | SZSE:002812 | 恩捷股份 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_A BATTERY_CHAIN | SZSE:002460 | 赣锋锂业 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_B PHOTOVOLTAIC | SSE:601012 | 隆基绿能 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_B PHOTOVOLTAIC | SSE:600438 | 通威股份 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_B PHOTOVOLTAIC | SSE:688599 | 天合光能 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 30_B PHOTOVOLTAIC | SZSE:002129 | TCL中环 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_A AUTO_OEM | SZSE:002594 | 比亚迪 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_A AUTO_OEM | SSE:601633 | 长城汽车 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_A AUTO_OEM | SSE:600104 | 上汽集团 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 40_A AUTO_OEM | SSE:601127 | 赛力斯 | 流动性观测 (LIQUIDITY_SENSOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_A SEMICONDUCTORS | SSE:688981 | 中芯国际 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_A SEMICONDUCTORS | SSE:603501 | 韦尔股份 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_A SEMICONDUCTORS | SSE:603986 | 兆易创新 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_A SEMICONDUCTORS | SSE:688012 | 中微公司 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_B CONSUMER_ELECTRONICS_CHAIN | SZSE:002415 | 海康威视 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_B CONSUMER_ELECTRONICS_CHAIN | SZSE:002241 | 歌尔股份 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_B CONSUMER_ELECTRONICS_CHAIN | SSE:688036 | 传音控股 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 50_B CONSUMER_ELECTRONICS_CHAIN | SZSE:000725 | 京东方A | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_A INNOVATIVE_PHARMA | SSE:600276 | 恒瑞医药 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_A INNOVATIVE_PHARMA | SZSE:000538 | 云南白药 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_A INNOVATIVE_PHARMA | SSE:600436 | 片仔癀 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 60_A INNOVATIVE_PHARMA | SSE:688180 | 君实生物 | 广度代理 (BREADTH_PROXY) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_A NONFERROUS_METALS | SSE:601899 | 紫金矿业 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_A NONFERROUS_METALS | SSE:603993 | 洛阳钼业 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_A NONFERROUS_METALS | SSE:600362 | 江西铜业 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_A NONFERROUS_METALS | SSE:600111 | 北方稀土 | 贝塔卫星 (BETA_SATELLITE) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_B COAL_AND_OIL | SSE:601088 | 中国神华 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_B COAL_AND_OIL | SSE:601857 | 中国石油 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_B COAL_AND_OIL | SSE:601225 | 陕西煤业 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 70_B COAL_AND_OIL | SSE:600028 | 中国石化 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 80_A CONSTRUCTION_AND_RAIL | SSE:601668 | 中国建筑 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 85_A POWER_UTILITIES | SSE:600900 | 长江电力 | 锚点 (ANCHOR) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 85_A POWER_UTILITIES | SSE:600886 | 国投电力 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 85_A POWER_UTILITIES | SSE:601985 | 中国核电 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 90_A HOME_APPLIANCES | SZSE:000333 | 美的集团 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 90_A HOME_APPLIANCES | SZSE:000651 | 格力电器 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 95_A TELECOM_OPERATORS | SSE:600941 | 中国移动 | 主题龙头 (THEME_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 95_A TELECOM_OPERATORS | SSE:600050 | 中国联通 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
| 95_A TELECOM_OPERATORS | SSE:601728 | 中国电信 | 质地龙头 (QUALITY_LEADER) |  | http://www.sse.com.cn/assortment/stock/list/share/ |
