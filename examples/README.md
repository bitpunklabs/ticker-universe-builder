# 当前输出格式示例

本轮只保留三份示例，供 review 可读报告的格式。使用 2026-10-08 已完成的在线研究输入，
此次重建不联网刷新市场事实，也不改变选股逻辑。

| 示例 | 主体数 | 参考工具数 | 报告 | TradingView |
|---|---:|---:|---|---|
| CN Medium | 302 | 42 | [简体中文](cn-medium/output/cn-medium-2026-10-08.zh-Hans.md) / [English](cn-medium/output/cn-medium-2026-10-08.en.md) | [TXT](cn-medium/output/cn-medium-2026-10-08.txt) |
| US Light | 100 | 44 | [English](us-light/output/us-light-2026-10-08.en.md) | [TXT](us-light/output/us-light-2026-10-08.txt) |
| US Medium | 294 | 44 | [English](us-medium/output/us-medium-2026-10-08.en.md) | [TXT](us-medium/output/us-medium-2026-10-08.txt) |

成员按主题分组，表格只保留代码、名称、角色和简短理由。`reason_summary` 来自原业务说明；
完整理由、准入证据、市值来源及逐标的测量诊断保留在 JSON，报告顶部提供链接。
部分交付缺口和重要验证警告仍会显示，不以隐藏诊断改变资格。

Medium 目录包含 `build-spec.json`、`snapshot.json` 和 `output/`；US Light 共用 US Medium
快照。标准产物由脚本生成，不手写名单。
[build-summary.json](build-summary.json) 保存数量、资格和哈希；
[input-provenance.json](input-provenance.json) 记录来源及展示摘要的转换。

```bash
python examples/build_examples.py

# 正式 CLI 构建到新的空目录
python scripts/universe.py build \
  --spec examples/us-light/build-spec.json \
  --snapshot examples/us-medium/snapshot.json --output temp/example-us-light
```

生成器先验证全部示例，再替换产物；实际 CLI 另存续跑记录，见
[标准输出](../references/output-artifacts.md)。其他市场和深度仍可构建，本轮不分发其示例。

CN 行情截至 **2026-09-30**，US 截至 **2026-10-06**；上市、市值和长期业务证据分别保留日期。
CN 快照保留 457 个已审查 Heavy 候选，不能据此生成合格 Max；US 保留完整 667 个候选。
原始价格和网络回执不分发，测量人口与哈希不因示例子集而改写。
资格通过表示证据契约、覆盖与容量检查通过，不代表独立证明所有龙头判断或全市场最优。
完整在线验收见 [测试记录](../docs/validation/codex-online-2026-10-08.md)。
