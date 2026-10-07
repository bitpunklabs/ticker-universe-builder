# 当前 coverage-first 示例

这组示例使用 2026-10-07 已完成人工 review 的研究快照，按当前默认策略重新构建；
旧版七市场的机械分组示例已移除。市场注册表仍支持十四个市场。

| 示例 | 主体数 | 参考工具数 | 报告 | TradingView |
|---|---:|---:|---|---|
| CN Medium | 302 | 42 | [简体中文](cn-medium/output/cn-medium-2026-10-07.zh-Hans.md) / [English](cn-medium/output/cn-medium-2026-10-07.en.md) | [TXT](cn-medium/output/cn-medium-2026-10-07.txt) |
| US Medium | 294 | 44 | [English](us-medium/output/us-medium-2026-10-07.en.md) | [TXT](us-medium/output/us-medium-2026-10-07.txt) |
| Crypto Medium | 35 | 0 | [English](crypto-medium/output/crypto-medium-2026-10-07.en.md) | [TXT](crypto-medium/output/crypto-medium-2026-10-07.txt) |
| Crypto Heavy | 50 | 0 | [English](crypto-heavy/output/crypto-heavy-2026-10-07.en.md) | [TXT](crypto-heavy/output/crypto-heavy-2026-10-07.txt) |
| Crypto Max | 65 | 0 | [English](crypto-max/output/crypto-max-2026-10-07.en.md) | [TXT](crypto-max/output/crypto-max-2026-10-07.txt) |

Medium 目录包含 `build-spec.json`、`snapshot.json` 和 `output/` 标准产物。
Crypto Heavy/Max 共用 `crypto-medium/snapshot.json`，只保留各自 spec 和产物，避免复制研究事实。
Max 使用这组 Heavy 作为 seed，保留全部 50 个主体及事实，新增 15 个 Beta，增幅 30%。
[build-summary.json](build-summary.json) 保存数量、资格、哈希和警告；
[input-provenance.json](input-provenance.json) 记录原始/示例快照哈希及候选子集转换。

```bash
# 离线重新生成全部示例和同日 NO_CHANGE 维护示例
python examples/build_examples.py

# 和用户实际运行一样，通过 CLI 构建到新目录
python scripts/universe.py build \
  --spec examples/cn-medium/build-spec.json \
  --snapshot examples/cn-medium/snapshot.json --output temp/example-cn
python scripts/universe.py build \
  --spec examples/crypto-heavy/build-spec.json \
  --snapshot examples/crypto-medium/snapshot.json --output temp/example-heavy
python scripts/universe.py build \
  --spec examples/crypto-max/build-spec.json \
  --snapshot examples/crypto-medium/snapshot.json \
  --seed temp/example-heavy/crypto-heavy-2026-10-07.json --output temp/example-max
```

生成器只替换本示例的标准产物，不联网、不改变研究输入。CLI 保留独立续跑记录，
见 [标准输出](../references/output-artifacts.md)。Crypto Medium 的
[changes.json](crypto-medium/changes.json) 演示同日 NO_CHANGE；维护产物在
[maintenance/](crypto-medium/maintenance/)，不宣称发生了新研究或换仓。

## 数据边界

股票价格窗口截至 **2026-09-28**，Crypto 截至 **2026-10-04**；上市和市值等证据有各自日期。
10 月 7 日为这轮研究/构建日期，不是全部行情刷新日期。上市、业务、准入、指标声明、
逐标的测量记录、数据哈希和来源 URL 都保留在输入/JSON 中；原始价格与抓取回执不随示例分发。

CN/US 为缩小示例体积，只保留已审查的 Heavy 主体候选：分别 457、370 个。
无关候选的未引用 source 索引条目一并删除；已保留事实的证据不变。
Medium 选择仍覆盖同一个完整审查龙头名册，主体名单与本轮已接受结果一致；原始测量人口和
来源记录来自更宽的研究，未重新计算为这个子集。这个示例候选不足以生成合格股票 Max，
也不能证明市场缺少 Beta。Crypto 保留 79 个候选以演示按 Heavy 分布、市值排序的扩展。

分组依据经济职责和主营业务；龙头/必要同行由逐标的 admission 和审查名册提供。
Beta 采用大体业务、对已命名核心的互补性和有来源的市值；股票使用本币权益市值，Crypto
使用 USD 流通市值。价格 Beta/R²/稳定性为辅助信息。合格代表事实契约、覆盖和容量检查通过，
不代表验证器独立证明每项龙头判断，也不保证已发现全市场最优候选。
