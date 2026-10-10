# CN overlay

Read [shared equity rules](equity-common.md) first.

## Universe boundary

- Shanghai, Shenzhen and Beijing listings plus the indices and ETFs needed as gauges, all
  expressible in TradingView.
- A common share must have a confirmed six-digit code, the correct venue and a normal, tradable
  listing state.
- ST and \*ST names, delisting-transition names, long-halted names, names whose identity cannot be
  confirmed, and names without recent effective turnover are excluded by default.
- The venue is part of CN identity: `SSE:000001` and `SZSE:000001` are different instruments, so
  the default `asset_id` keeps the venue prefix.
- ETFs and single names are compared separately. ETFs carry structural gauges; single names carry
  company and supply-chain information.
- Report language: `zh-Hans`, with authored English content for the companion.

## CN economic map

The starter preserves the legacy fine driver map: optical modules, servers/PCB, IDC, cooling and
power; equipment, materials, fabrication, packaging and chip functions; battery materials,
cells, equipment and storage; grid equipment versus power operations. Do not append a parallel
provider-industry taxonomy around these existing duties. Unmapped names require business
research into the same map, or an explicitly justified new durable theme.

Check mixed businesses before inheriting a section. The October 2026 review separates optical
fibre/network construction (`10_F`) from modules/components (`10_A`) and grid equipment
(`17_A`); EDA/IP (`11_I`) from enterprise software; and oilfield services (`21_D`) from
shipbuilding. Hengtong and Zhongtian can serve the fibre observation, but their substantial
power and submarine-cable businesses must remain disclosed. A chosen observation function is
not a claim about the largest revenue segment. Hengtong's
[2025 financial table](https://static.cninfo.com.cn/finalpage/2026-05-16/1225310932.PDF)
reports larger smart-grid than optical-communication revenue.

Other reviewed boundaries: [Yealink](https://static.cninfo.com.cn/finalpage/2026-04-22/1225142083.PDF)
supplies communication terminals, not general enterprise software;
[Empyrean](https://static.cninfo.com.cn/finalpage/2026-04-28/1225217315.PDF) supplies EDA;
[COSL](https://static.cninfo.com.cn/finalpage/2026-03-25/1225028515.PDF) supplies oilfield services.
These are dated research examples, not permanent ticker overrides in the selector.

Keep broad/style, sector and gold/duration gauges distinct from their stocks. A listed ETF may
stand in for an index observation only with a disclosed proxy reason. Quote activity and a clean
name string do not complete ST, halt, inquiry or issuer-quality checks. Policy news changes
research priority, not permanent membership without a durable industrial link.

## Research fields

Prioritize nationwide/shareholding/regional banks, insurance classes, power-operation models,
food/drink/retail and agriculture before optional semiconductor depth. Check listing, ST/halt
status, local turnover, theme factors and evidence dates. Small/noisy gauges need a disclosed
size/turnover floor; any sole-pure-play exception requires a reason and still obeys validation.
Short-term financing bond and money-market funds are cash substitutes, excluded by type.

## Example

[`examples/cn-medium/`](../../examples/cn-medium/) contains a current coverage-first Medium
research snapshot, measured statistics, dated listing evidence, reports and script-generated watchlist.
Read [the scope and limitations](../../examples/README.md) before reusing it.
