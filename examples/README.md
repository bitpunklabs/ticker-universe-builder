# Worked examples

十份示例包含研究输入与脚本生成的标准产物。成员表仅显示代码、名称、角色和简短理由；
完整推理、证据及逐标的测量诊断保留在 JSON，报告顶部提供链接。
HTML 为完整暗色响应式页面，下载后用浏览器打开；GitHub 文件页显示源代码。

| 示例 | 主体数 | 参考工具数 | Markdown | HTML | TradingView |
|---|---:|---:|---|---|---|
| CN Medium | 302 | 42 | [简体中文](cn-medium/output/cn-medium-2026-10-08.zh-Hans.md) / [English](cn-medium/output/cn-medium-2026-10-08.en.md) | [HTML](cn-medium/output/cn-medium-2026-10-08.zh-Hans.html) | [TXT](cn-medium/output/cn-medium-2026-10-08.txt) |
| US Light | 100 | 44 | [English](us-light/output/us-light-2026-10-08.en.md) | [HTML](us-light/output/us-light-2026-10-08.en.html) | [TXT](us-light/output/us-light-2026-10-08.txt) |
| US Medium | 294 | 44 | [English](us-medium/output/us-medium-2026-10-08.en.md) | [HTML](us-medium/output/us-medium-2026-10-08.en.html) | [TXT](us-medium/output/us-medium-2026-10-08.txt) |
| US Heavy | 370 | 44 | [English](us-heavy/output/us-heavy-2026-10-08.en.md) | [HTML](us-heavy/output/us-heavy-2026-10-08.en.html) | [TXT](us-heavy/output/us-heavy-2026-10-08.txt) |
| US Max | 481 | 44 | [English](us-max/output/us-max-2026-10-08.en.md) | [HTML](us-max/output/us-max-2026-10-08.en.html) | [TXT](us-max/output/us-max-2026-10-08.txt) |
| Crypto Medium | 35 | 0 | [English](crypto-medium/output/crypto-medium-2026-10-08.en.md) | [HTML](crypto-medium/output/crypto-medium-2026-10-08.en.html) | [TXT](crypto-medium/output/crypto-medium-2026-10-08.txt) |
| HK Medium | 123 | 2 | [繁體中文](hk-medium/output/hk-medium-2026-10-08.zh-Hant.md) / [English](hk-medium/output/hk-medium-2026-10-08.en.md) | [HTML](hk-medium/output/hk-medium-2026-10-08.zh-Hant.html) | [TXT](hk-medium/output/hk-medium-2026-10-08.txt) |
| JP Medium | 131 | 2 | [日本語](jp-medium/output/jp-medium-2026-10-07.ja.md) / [English](jp-medium/output/jp-medium-2026-10-07.en.md) | [HTML](jp-medium/output/jp-medium-2026-10-07.ja.html) | [TXT](jp-medium/output/jp-medium-2026-10-07.txt) |
| KR Medium | 108 | 2 | [한국어](kr-medium/output/kr-medium-2026-10-07.ko.md) / [English](kr-medium/output/kr-medium-2026-10-07.en.md) | [HTML](kr-medium/output/kr-medium-2026-10-07.ko.html) | [TXT](kr-medium/output/kr-medium-2026-10-07.txt) |
| UK Medium | 127 | 2 | [English](uk-medium/output/uk-medium-2026-10-08.en.md) | [HTML](uk-medium/output/uk-medium-2026-10-08.en.html) | [TXT](uk-medium/output/uk-medium-2026-10-08.txt) |

成员按主题分组，表格只保留代码、名称、角色和简短理由。`reason_summary` 来自原业务说明；
完整理由、准入证据、市值来源及逐标的测量诊断保留在 JSON，报告顶部提供链接。
中文摘要直接陈述主营；英文人类可读内容通过 `report_translations.en` 保存并由 CLI 渲染。
部分交付缺口和重要验证警告仍会显示，不以隐藏诊断改变资格。

Medium 目录包含 `build-spec.json`、`snapshot.json` 和 `output/`；US 四个档位共用 US Medium
快照。Max 保留全部 370 个 Heavy 主体，新增 111 个 Beta（30%）。
标准产物包含 HTML、Markdown、TXT、完整 JSON、验证 JSON，由脚本生成，不手写名单。
[build-summary.json](build-summary.json) 保存数量、资格和哈希；
[input-provenance.json](input-provenance.json) 记录来源及展示摘要的转换。

```bash
python examples/build_examples.py

# 正式 CLI 构建到新的空目录
python scripts/universe.py build \
  --spec examples/us-heavy/build-spec.json \
  --snapshot examples/us-medium/snapshot.json --output temp/example-us-heavy

python scripts/universe.py build \
  --spec examples/us-max/build-spec.json \
  --snapshot examples/us-medium/snapshot.json \
  --seed temp/example-us-heavy/us-heavy-2026-10-08.json --output temp/example-us-max
```

生成器先验证全部示例，再替换产物；实际 CLI 另存续跑记录，见
[标准输出](../references/output-artifacts.md)。重建使用保存的事实，不联网刷新。

## Research dates and limits

| 市场 | 快照日期 | 价格截至 | 本轮工作 |
|---|---|---|---|
| CN | 2026-10-08 | 2026-09-30 | 保留已完成在线研究与短理由格式 |
| US / Crypto | 2026-10-08 | 2026-10-06 | 使用已完成在线研究，增加所需档位示例 |
| HK / UK | 2026-10-08 | 2026-10-07 | 新在线业务、财务、有效报价与历史价格研究 |
| JP / KR | 2026-10-07 | 2026-09-28 | 恢复已审查业务输入，补齐短理由和英文展示；上市观察仍为 2026-09-29 |

HK/UK 修正失效代码和供应商业务串码，见
[HK review](hk-medium/research-review.json)、[UK review](uk-medium/research-review.json)。
JP/KR 保留原价格、日期、测量人口与哈希，见
[JP review](jp-medium/research-review.json)、[KR review](kr-medium/research-review.json)。
HK 以 123 条 HKD 历史排序流动性；UK 以 128 条已采集历史排序，GBp/GBX 成交额归一到 GBP，
其中投资基金 SMT 仅属于测量人口、不进入名单。主题因子使用同职责任务的留一法篮子；
不足三条历史时不声称已测得主题回归，也不用全市场指数补值。

CN 快照保留 457 个已审查 Heavy 候选，不能据此生成合格 Max；US 保留完整 667 个候选。
HK/UK/JP/KR Medium 是明确范围内的主要业务代表，未提供 Beta bench，不代表查遍全部龙头。
供应商财务期间未知处保留未知，亏损与缺少现金流字段逐标的记录。
原始价格和网络回执不分发，测量人口与哈希不因示例子集而改写。
资格通过表示证据契约、覆盖与容量检查通过，不独立证明所有龙头判断、全市场最优或
TradingView 界面导入效果。
完整在线验收见 [测试记录](../docs/validation/codex-online-2026-10-08.md)。
