> Gerado por `python examples/build_examples.py`, a partir de
> `examples/seeds/br.tsv`. Este é o artefato `.md` que um build escreve, versionado para
> ser lido sem executar nada.
> Todo valor de métrica aqui é ilustrativo — veja [README.md](../README.md).

# Universo de tickers BR

- Profundidade: Enxuto
- Fatos apurados em: 2026-09-17
- Versão: `8dd01f54afeb`
- Ativos: 35
- Temas: 23
- Estabilidade: 0.97 · 34 / 35 · ±1%
- Maior tema: 80_C · 5 · 14% · participação ponderada 4
- Entradas no TradingView: 58 / 1000
- Candidatos descartados ou não selecionados: 27
- Validação: APROVADO

## Distribuição de papéis

| Papel | Quantidade |
|---|---:|
| Âncora (ANCHOR) | 4 |
| Referência (BENCHMARK) | 1 |
| Satélite beta (BETA_SATELLITE) | 4 |
| Proxy de amplitude (BREADTH_PROXY) | 1 |
| Sensor de liquidez (LIQUIDITY_SENSOR) | 2 |
| Líder de qualidade (QUALITY_LEADER) | 1 |
| Líder do tema (THEME_LEADER) | 22 |

## Cobertura temática

| Código | Grupo | Tema | Nível | Quantidade |
|---|---|---|---:|---:|
| 00_A | Índices de mercado | BROAD_MARKET_ETF | 1 | 2 |
| 00_B | Índices de mercado | EQUAL_WEIGHT_AND_BREADTH | 2 | 0 |
| 00_C | Índices de mercado | VOLATILITY_AND_HEDGES | 3 | 0 |
| 10_D | Tecnologia | ENTERPRISE_SOFTWARE | 1 | 1 |
| 10_F | Tecnologia | INTERNET_AND_ADTECH | 1 | 1 |
| 10_G | Tecnologia | IT_SERVICES_AND_CONSULTING | 2 | 0 |
| 15_A | Agronegócio | AGRIBUSINESS | 1 | 2 |
| 15_B | Agronegócio | PULP_AND_PAPER | 2 | 0 |
| 20_A | Comunicação | STREAMING_AND_MEDIA | 3 | 0 |
| 20_B | Comunicação | TELECOM | 1 | 1 |
| 30_A | Consumo | DISCRETIONARY_LEADERS | 1 | 1 |
| 30_B | Consumo | STAPLES | 1 | 3 |
| 30_C | Consumo | RESTAURANTS_AND_TRAVEL | 1 | 2 |
| 30_E | Consumo | AUTOS_AND_MOBILITY | 2 | 0 |
| 40_A | Financeiro | MONEY_CENTER_BANKS | 1 | 2 |
| 40_B | Financeiro | PAYMENTS | 3 | 0 |
| 40_C | Financeiro | ASSET_MANAGERS_AND_EXCHANGES | 1 | 1 |
| 40_D | Financeiro | INSURANCE | 1 | 1 |
| 40_E | Financeiro | REGIONAL_BANKS | 2 | 0 |
| 50_A | Saúde | PHARMA | 1 | 1 |
| 50_B | Saúde | MEDTECH_AND_DEVICES | 3 | 0 |
| 50_C | Saúde | MANAGED_CARE | 1 | 1 |
| 50_D | Saúde | BIOTECH | 2 | 0 |
| 60_A | Industrial | AEROSPACE_AND_DEFENSE | 1 | 1 |
| 60_B | Industrial | MACHINERY_AND_RAIL | 1 | 1 |
| 60_C | Industrial | TRANSPORT_AND_LOGISTICS | 1 | 1 |
| 60_E | Industrial | ENGINEERING_AND_CONSTRUCTION | 3 | 0 |
| 70_A | Energia | INTEGRATED_ENERGY | 1 | 1 |
| 70_B | Energia | OILFIELD_AND_MIDSTREAM | 1 | 1 |
| 70_C | Energia | EXPLORATION_AND_PRODUCTION | 1 | 1 |
| 80_A | Materiais e utilidades | MATERIALS | 1 | 2 |
| 80_B | Materiais e utilidades | UTILITIES | 1 | 2 |
| 80_C | Materiais e utilidades | METALS_AND_MINING | 1 | 5 |
| 80_D | Materiais e utilidades | CHEMICALS | 3 | 0 |
| 90_A | Imóveis | REITS | 1 | 1 |

## Como as métricas foram produzidas

| Métrica | Base | Método | Janela |
|---|---|---|---|
| beta_stability | medido (measured) | concordância da estimativa de beta entre as duas metades da janela | 180d |
| beta_strength | medido (measured) | módulo do beta OLS contra BMFBOVESPA:BOVA11; beta de 2,0 vale 100 | 180d |
| heat | julgado (judged) | salto de volume confirmado nos dados da bolsa, nunca um movimento de um dia | — |
| independence | medido (measured) | 100 menos o R² dos retornos diários regredidos sobre BMFBOVESPA:BOVA11 | 180d |
| liquidity | medido (measured) | percentil transversal do volume financeiro médio diário | 30d |
| quality | misto (blended) | tempo de listagem e percentil de tamanho, somados a um juízo de durabilidade | — |

Em 28 de 35 componentes, quality combina 50% de regra e 50% de julgamento. A metade regrada lê tempo de listagem, percentil de tamanho e sinais desfavoráveis; a metade julgada é o que nenhuma estatística cobre.

## Por que candidatos ficaram de fora

| Motivo | Quantidade |
|---|---:|
| vagas já preenchidas (not_selected_under_budget) | 25 |
| ativo duplicado (duplicate_asset) | 1 |
| tipo de instrumento excluído (excluded_instrument_type) | 1 |

## Componentes

| Tema | Ticker | Nome | Papel | Motivo | Fonte |
|---|---|---|---|---|---|
| 00_A BROAD_MARKET_ETF | BMFBOVESPA:BOVA11 | iShares Ibovespa Fundo de Índice | Referência (BENCHMARK) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 00_A BROAD_MARKET_ETF | BMFBOVESPA:SMAL11 | iShares BM&FBOVESPA Small Cap | Proxy de amplitude (BREADTH_PROXY) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 10_D ENTERPRISE_SOFTWARE | BMFBOVESPA:TOTS3 | Totvs | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 10_F INTERNET_AND_ADTECH | BMFBOVESPA:MGLU3 | Magazine Luiza | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 15_A AGRIBUSINESS | BMFBOVESPA:JBSS3 | JBS | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 15_A AGRIBUSINESS | BMFBOVESPA:SLCE3 | SLC Agrícola | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 20_B TELECOM | BMFBOVESPA:VIVT3 | Telefônica Brasil | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 30_A DISCRETIONARY_LEADERS | BMFBOVESPA:LREN3 | Lojas Renner | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 30_B STAPLES | BMFBOVESPA:ABEV3 | Ambev | Âncora (ANCHOR) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 30_B STAPLES | BMFBOVESPA:ASAI3 | Sendas Distribuidora | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 30_B STAPLES | BMFBOVESPA:PCAR3 | Companhia Brasileira de Distribuição | Satélite beta (BETA_SATELLITE) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 30_C RESTAURANTS_AND_TRAVEL | BMFBOVESPA:CVCB3 | CVC Brasil | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 30_C RESTAURANTS_AND_TRAVEL | BMFBOVESPA:AZUL4 | Azul | Sensor de liquidez (LIQUIDITY_SENSOR) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 40_A MONEY_CENTER_BANKS | BMFBOVESPA:ITUB4 | Itaú Unibanco | Âncora (ANCHOR) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 40_A MONEY_CENTER_BANKS | BMFBOVESPA:BBDC4 | Banco Bradesco | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | BMFBOVESPA:B3SA3 | B3 Brasil Bolsa Balcão | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 40_D INSURANCE | BMFBOVESPA:BBSE3 | BB Seguridade | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 50_A PHARMA | BMFBOVESPA:HYPE3 | Hypera | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 50_C MANAGED_CARE | BMFBOVESPA:RDOR3 | Rede D'Or São Luiz | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 60_A AEROSPACE_AND_DEFENSE | BMFBOVESPA:EMBR3 | Embraer | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 60_B MACHINERY_AND_RAIL | BMFBOVESPA:WEGE3 | WEG | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 60_C TRANSPORT_AND_LOGISTICS | BMFBOVESPA:RAIL3 | Rumo | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 70_A INTEGRATED_ENERGY | BMFBOVESPA:PETR4 | Petróleo Brasileiro PN | Âncora (ANCHOR) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 70_B OILFIELD_AND_MIDSTREAM | BMFBOVESPA:UGPA3 | Ultrapar Participações | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 70_C EXPLORATION_AND_PRODUCTION | BMFBOVESPA:PRIO3 | PRIO | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_A MATERIALS | BMFBOVESPA:SUZB3 | Suzano | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_A MATERIALS | BMFBOVESPA:BRKM5 | Braskem | Satélite beta (BETA_SATELLITE) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_B UTILITIES | BMFBOVESPA:ELET3 | Centrais Elétricas Brasileiras | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_B UTILITIES | BMFBOVESPA:CMIG4 | Cemig | Satélite beta (BETA_SATELLITE) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_C METALS_AND_MINING | BMFBOVESPA:VALE3 | Vale | Âncora (ANCHOR) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_C METALS_AND_MINING | BMFBOVESPA:GGBR4 | Gerdau | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_C METALS_AND_MINING | BMFBOVESPA:CMIN3 | CSN Mineração | Líder de qualidade (QUALITY_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_C METALS_AND_MINING | BMFBOVESPA:CSNA3 | Companhia Siderúrgica Nacional | Satélite beta (BETA_SATELLITE) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 80_C METALS_AND_MINING | BMFBOVESPA:USIM5 | Usiminas | Sensor de liquidez (LIQUIDITY_SENSOR) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
| 90_A REITS | BMFBOVESPA:MULT3 | Multiplan Empreendimentos Imobiliários | Líder do tema (THEME_LEADER) |  | https://www.b3.com.br/en_us/market-data-and-indices/data-services/market-data/historical-data/equities/ |
