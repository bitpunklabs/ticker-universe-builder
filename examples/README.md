# 当前 coverage-first 示例

八份示例使用当前默认策略和标准输出契约。
US 四档及 CN/Crypto Medium 使用 2026-10-08 真实在线调用后的修正快照；
它们经过 agent 内容审查及独立契约验收，不宣称本轮已经取得用户手工认可。
JP/KR Medium 重新审查业务职责与准入，复用可核验的历史测量，研究边界见下文。

| 示例 | 主体数 | 参考工具数 | 报告 | TradingView |
|---|---:|---:|---|---|
| US Light | 100 | 44 | [English](us-light/output/us-light-2026-10-08.en.md) | [TXT](us-light/output/us-light-2026-10-08.txt) |
| US Medium | 294 | 44 | [English](us-medium/output/us-medium-2026-10-08.en.md) | [TXT](us-medium/output/us-medium-2026-10-08.txt) |
| US Heavy | 370 | 44 | [English](us-heavy/output/us-heavy-2026-10-08.en.md) | [TXT](us-heavy/output/us-heavy-2026-10-08.txt) |
| US Max | 481 | 44 | [English](us-max/output/us-max-2026-10-08.en.md) | [TXT](us-max/output/us-max-2026-10-08.txt) |
| CN Medium | 302 | 42 | [简体中文](cn-medium/output/cn-medium-2026-10-08.zh-Hans.md) / [English](cn-medium/output/cn-medium-2026-10-08.en.md) | [TXT](cn-medium/output/cn-medium-2026-10-08.txt) |
| Crypto Medium | 35 | 0 | [English](crypto-medium/output/crypto-medium-2026-10-08.en.md) | [TXT](crypto-medium/output/crypto-medium-2026-10-08.txt) |
| JP Medium | 131 | 2 | [日本語](jp-medium/output/jp-medium-2026-10-07.ja.md) / [English](jp-medium/output/jp-medium-2026-10-07.en.md) | [TXT](jp-medium/output/jp-medium-2026-10-07.txt) |
| KR Medium | 108 | 2 | [한국어](kr-medium/output/kr-medium-2026-10-07.ko.md) / [English](kr-medium/output/kr-medium-2026-10-07.en.md) | [TXT](kr-medium/output/kr-medium-2026-10-07.txt) |

Medium 目录包含 `build-spec.json`、`snapshot.json` 和 `output/` 标准产物。
US Light/Heavy/Max 共用 `us-medium/snapshot.json`，只保留各自 spec 和产物，避免复制研究事实。
Max 使用同组 Heavy 作为 seed，保留全部 370 个主体及事实，新增 111 个 Beta，增幅 30%。
[build-summary.json](build-summary.json) 保存数量、资格、哈希和警告；
[input-provenance.json](input-provenance.json) 记录原始/示例输入哈希、候选转换和来源边界。
JP/KR 的 `research-review.json` 保留审查后的业务摘要、实际财务字段、审查理由和来源回执哈希。

```bash
# 离线重新生成八份示例和同日 NO_CHANGE 维护示例
python examples/build_examples.py

# 通过正式 CLI 构建到新的空目录
python scripts/universe.py build \
  --spec examples/jp-medium/build-spec.json \
  --snapshot examples/jp-medium/snapshot.json --output temp/example-jp
python scripts/universe.py build \
  --spec examples/us-heavy/build-spec.json \
  --snapshot examples/us-medium/snapshot.json --output temp/example-heavy
python scripts/universe.py build \
  --spec examples/us-max/build-spec.json \
  --snapshot examples/us-medium/snapshot.json \
  --seed temp/example-heavy/us-heavy-2026-10-08.json --output temp/example-max
```

生成器先检查全部示例，再替换标准产物；不联网，不改变研究输入。
实际 CLI 会另存续跑记录，见 [标准输出](../references/output-artifacts.md)。
Crypto Medium 的 [changes.json](crypto-medium/changes.json) 演示同日 NO_CHANGE；
维护产物在 [maintenance/](crypto-medium/maintenance/)，不宣称发生新研究或换仓。
旧 Crypto Heavy/Max 示例已移除，不影响该市场的能力或历史测试 fixture。

## 数据边界

CN 行情截至 **2026-09-30**，US/Crypto 截至 **2026-10-06**；
JP/KR 仍保留 **2026-09-28** 的行情和原研究日期。上市、市值、业务证据分别记录日期。
重新生成不会刷新事实；逐标的测量人口、数据 SHA 和来源保持原值，完整原始行情不分发。
CN 为缩小体积保留 457 个最终 Heavy 候选，不能用来生成合格 Max，也不能推断市场缺 Beta。
US 保留 667 个候选与拒绝审计，Crypto 保留 79 个候选。

本轮在线修正包括 CN Beta 主营归类、逐标的成交量单位；US ET 的命名空间冲突、
WBD 企业行动后的职责替换及股类来源身份；Crypto 网页壳的证据刷新状态。
长期业务事实可沿用原日期，未知事项仍披露。ET 实际 venue 与 TradingView namespace
分别记录，不能据旧码推断新交易所代码。Crypto GRAM 短历史和 STX Monitoring 保留风险说明。
详见 [在线验收](../docs/validation/codex-online-2026-10-08.md)。

JP/KR 分别审查 131/108 个主要经营主体，覆盖金融、传统消费、通信、科技、医药、工业、
运输、能源、材料和公用事业；JP 另含商社和开发商。名单是明确范围内的研究名册，
不宣称已审查全市场的每个龙头。业务描述与标准化财务字段来自 10 月 7 日读取的 Tier 2 资料，
官方市场结构来自 JPX/KRX。财务供应商未提供报表期间标签，不推断半年报或 TTM。
负利润、负自由现金流和缺值逐标的披露；金融机构不按工业企业自由现金流排名。
主要经营代表的准入是读过业务后的研究判断，未独立审计所有发行人财报、市场份额或实时监管标记。
KR 的 YG（122870）未进入已测量人口，因此保留为研究缺口，不补造历史。

JP/KR 上市检查为 9 月 29 日，复用原始日期、价格数据哈希和流动性测量人口。
主营归类调整后，旧价格 Beta/R²/稳定性不再随输入保留：旧主题回归不能认证新职责。
两份 Medium 没有 Beta 扩展研究，不能直接充当合格 Max 输入。稀疏展示主题与相近职责合并，
底层分支和名册不合并。日/韩名称及审查理由按市场语言编写；英文报告翻译标题和固定词汇，
不会自动翻译这些研究文字。

合格代表事实契约、覆盖和容量检查通过；验证器不会独立证明每项龙头判断，也不保证全市场最优。
Beta 采用大体业务、与已命名核心的互补性及有来源的市值；股票使用本币权益市值，
Crypto 使用 USD 流通市值。价格 Beta/R²/稳定性为辅助信息。
