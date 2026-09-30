# 七个市场的 Medium 示例

**历史基线（0.4）**：这些快照保留当时的行业／产品标签分类和机械角色分配，用于离线回归和
新旧对照，不是 0.5 的研究模板。新建池应从当前 starter 开始，采用经济驱动分组，声明职责和
核心代表，并重新研究角色；不能照抄下文的市值／低 R² 角色规则。旧快照缺少职责约束时，
验证器会明确提示 legacy presence-only coverage。

以下示例基于 2026-09-29 获取的真实上市／报价记录，行情截止 2026-09-28。旧的十四套
Light 示例及人为生成的指标已删除。市场注册表仍支持十四个市场；本轮只提供下列七套示例。

| 市场 | Medium 数量 | 报告 | TradingView |
|---|---:|---|---|
| US | 215 | [English](us-medium/universe.en.md) | [txt](us-medium/watchlist.txt) |
| JP | 170 | [日本語](jp-medium/universe.ja.md) | [txt](jp-medium/watchlist.txt) |
| CN | 210 | [简体中文](cn-medium/universe.zh-Hans.md) | [txt](cn-medium/watchlist.txt) |
| KR | 145 | [한국어](kr-medium/universe.ko.md) | [txt](kr-medium/watchlist.txt) |
| HK | 145 | [繁體中文](hk-medium/universe.zh-Hant.md) | [txt](hk-medium/watchlist.txt) |
| UK | 135 | [English](uk-medium/universe.en.md) | [txt](uk-medium/watchlist.txt) |
| Crypto | 105 | [English](crypto-medium/universe.en.md) | [txt](crypto-medium/watchlist.txt) |

每个目录包含 `build-spec.json`、`snapshot.json`、`universe.json`、`validation.json`、市场语言和
英文报告，以及脚本生成的最终 watchlist。Crypto 另有同日 `NO_CHANGE` 维护例子；它演示契约，
不假装发生了真实换仓。离线重建：

```bash
python examples/build_examples.py
```

重建只消费已提交的研究快照，不联网、不重新估计数据、不改选输入。刷新时先用
[fetch](../references/providers.md) 获取新证据，重新研究分类和角色，再用
[measure](../references/measurement.md) 计算指标。数据日期不会因重建而变新。

这些是研究范围明确的观察池，不是全市场完成尽调的清单。股票来自 TradingView 当前普通股／
主要上市地及行业分类，Yahoo 提供复权价格；成交额采用原始收盘价乘成交量的代理量。股票主题
因子采用剔除自身的行业／主题等权篮子；同行不足时不生成因子数值。Crypto 使用 Binance 官方
上市记录、产品标签、quoted turnover，以及 BTC／ETH／SOL 联合 OLS。所有来源、人口基数、
日期、数据哈希、失败数量与评分缺项均保留；原始历史数据留在本地 temp，不随示例分发。

分类是透明的研究判断：股票示例以来源行业为基础，并非每个市场完整的产业驱动地图。CN
继承旧 ticker-pool（修订 `007b118`）的 78 个细分股票主题，再用 Heavy 层的来源行业补足
未映射候选；继承分类不等于本轮逐家公司重新做业务尽调。每个成员的 reason/tag 明示分类来源。
示例的 taxonomy 是本轮研究后的修订表，因此不要求与 assets 中的 starter 逐项相同。

THEME_LEADER 表示该研究主题内观察到的市值／成交额领先，不代表财务质量评级；其余角色由
实测因子决定。没有虚构 quality 或 heat 分数，也没有逐项确认所有监管不利状态。报告中的评分
缺项、桶比例偏离必须保留。样本可重建和校验，不证明观察覆盖优于旧池，也不构成前瞻验证。
