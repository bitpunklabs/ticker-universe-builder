> Erzeugt von `python examples/build_examples.py` aus `examples/seeds/de.tsv`.
> Dies ist das `.md`-Artefakt eines Builds, eingecheckt, damit es ohne Ausführung lesbar ist.
> Jeder Kennzahlenwert darin ist illustrativ — siehe [README.md](../README.md).

# DE Ticker-Universum

- Tiefe: Schlank
- Fakten zum Stand: 2026-09-17
- Version: `5d81fc4fb461`
- Titel: 45
- Themen: 25
- Größtes Thema: 30_E · 4 · 9% · gewichteter Anteil 4
- TradingView-Einträge: 70 / 1000
- Abgelehnte oder nicht ausgewählte Kandidaten: 29
- Prüfung: BESTANDEN

## Rollenverteilung

| Rolle | Anzahl |
|---|---:|
| Anker (ANCHOR) | 7 |
| Benchmark (BENCHMARK) | 1 |
| Beta-Satellit (BETA_SATELLITE) | 5 |
| Breiten-Proxy (BREADTH_PROXY) | 1 |
| Liquiditätssensor (LIQUIDITY_SENSOR) | 2 |
| Qualitätsführer (QUALITY_LEADER) | 5 |
| Themenführer (THEME_LEADER) | 24 |

## Themenabdeckung

| Code | Gruppe | Thema | Stufe | Anzahl |
|---|---|---|---:|---:|
| 00_A | Marktindizes | BROAD_MARKET_ETF | 1 | 2 |
| 00_B | Marktindizes | EQUAL_WEIGHT_AND_BREADTH | 2 | 0 |
| 00_C | Marktindizes | VOLATILITY_AND_HEDGES | 3 | 0 |
| 10_B | Technologie | SEMICONDUCTORS | 1 | 1 |
| 10_C | Technologie | SEMICAP_EQUIPMENT | 1 | 1 |
| 10_D | Technologie | ENTERPRISE_SOFTWARE | 1 | 3 |
| 10_E | Technologie | CYBERSECURITY | 1 | 1 |
| 10_F | Technologie | INTERNET_AND_ADTECH | 1 | 2 |
| 10_G | Technologie | IT_SERVICES_AND_CONSULTING | 2 | 0 |
| 20_A | Kommunikation | STREAMING_AND_MEDIA | 1 | 1 |
| 20_B | Kommunikation | TELECOM | 1 | 1 |
| 20_C | Kommunikation | GAMING_AND_INTERACTIVE | 3 | 0 |
| 20_D | Kommunikation | ADVERTISING_AND_MARKETING | 3 | 0 |
| 30_A | Konsum | DISCRETIONARY_LEADERS | 1 | 2 |
| 30_B | Konsum | STAPLES | 1 | 1 |
| 30_C | Konsum | RESTAURANTS_AND_TRAVEL | 1 | 2 |
| 30_D | Konsum | APPAREL_AND_LUXURY | 2 | 0 |
| 30_E | Konsum | AUTOS_AND_MOBILITY | 1 | 4 |
| 40_A | Finanzwerte | MONEY_CENTER_BANKS | 1 | 1 |
| 40_B | Finanzwerte | PAYMENTS | 3 | 0 |
| 40_C | Finanzwerte | ASSET_MANAGERS_AND_EXCHANGES | 1 | 1 |
| 40_D | Finanzwerte | INSURANCE | 1 | 2 |
| 40_E | Finanzwerte | REGIONAL_BANKS | 2 | 0 |
| 50_A | Gesundheit | PHARMA | 1 | 2 |
| 50_B | Gesundheit | MEDTECH_AND_DEVICES | 1 | 1 |
| 50_D | Gesundheit | BIOTECH | 2 | 0 |
| 50_E | Gesundheit | LIFE_SCIENCE_TOOLS | 2 | 0 |
| 50_F | Gesundheit | HEALTHCARE_DISTRIBUTION | 3 | 0 |
| 60_A | Industrie | AEROSPACE_AND_DEFENSE | 1 | 1 |
| 60_B | Industrie | MACHINERY_AND_RAIL | 1 | 2 |
| 60_C | Industrie | TRANSPORT_AND_LOGISTICS | 1 | 1 |
| 60_D | Industrie | ELECTRICAL_EQUIPMENT | 1 | 3 |
| 60_E | Industrie | ENGINEERING_AND_CONSTRUCTION | 3 | 0 |
| 60_F | Industrie | DISTRIBUTION_AND_SUPPLY | 3 | 0 |
| 80_A | Rohstoffe und Versorger | MATERIALS | 1 | 3 |
| 80_B | Rohstoffe und Versorger | UTILITIES | 1 | 2 |
| 80_C | Rohstoffe und Versorger | METALS_AND_MINING | 2 | 0 |
| 80_D | Rohstoffe und Versorger | CHEMICALS | 1 | 3 |
| 80_E | Rohstoffe und Versorger | WATER_AND_WASTE | 3 | 0 |
| 90_A | Immobilien | REITS | 1 | 2 |
| 90_C | Immobilien | REAL_ESTATE_SERVICES | 3 | 0 |

## Wie die Kennzahlen entstanden sind

| Kennzahl | Grundlage | Methode | Zeitfenster |
|---|---|---|---|
| beta_stability | gemessen (measured) | Übereinstimmung der Beta-Schätzung über beide Hälften des Zeitraums | 180d |
| beta_strength | gemessen (measured) | Betrag des OLS-Betas gegen XETR:EXS1; Beta 2,0 entspricht 100 | 180d |
| heat | eingeschätzt (judged) | Umsatzsprung, gegen Börsendaten bestätigt, niemals eine Eintagesbewegung | — |
| independence | gemessen (measured) | 100 minus das Bestimmtheitsmaß der Tagesrenditen auf XETR:EXS1 | 180d |
| liquidity | gemessen (measured) | Querschnittsperzentil des durchschnittlichen Tagesumsatzes | 30d |
| quality | gemischt (blended) | Börsenalter und Größenperzentil, ergänzt um ein Urteil zur Beständigkeit | — |

Bei 37 von 45 Mitgliedern setzt sich quality zu 50% aus Regeln und zu 50% aus Einschätzung zusammen. Die Regelhälfte liest Börsenalter, Größenperzentil und Negativmerkmale; die Einschätzungshälfte ist das, was keine Statistik abdeckt.

## Warum Kandidaten nicht aufgenommen wurden

| Begründung | Anzahl |
|---|---:|
| Plätze bereits vergeben (not_selected_under_budget) | 27 |
| ausgeschlossene Instrumentenart (excluded_instrument_type) | 1 |
| redundant zu einem Mitglied (redundant_with_member) | 1 |

## Mitglieder

| Thema | Kürzel | Name | Rolle | Begründung | Beleg |
|---|---|---|---|---|---|
| 00_A BROAD_MARKET_ETF | XETR:EXS1 | iShares Core DAX UCITS ETF | Benchmark (BENCHMARK) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 00_A BROAD_MARKET_ETF | XETR:EXS3 | iShares MDAX UCITS ETF | Breiten-Proxy (BREADTH_PROXY) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 10_B SEMICONDUCTORS | XETR:IFX | Infineon Technologies | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 10_C SEMICAP_EQUIPMENT | XETR:AIXA | Aixtron | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 10_D ENTERPRISE_SOFTWARE | XETR:SAP | SAP | Anker (ANCHOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 10_D ENTERPRISE_SOFTWARE | XETR:NEM | Nemetschek | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 10_D ENTERPRISE_SOFTWARE | XETR:TMV | TeamViewer | Qualitätsführer (QUALITY_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 10_E CYBERSECURITY | XETR:YSN | secunet Security Networks | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 10_F INTERNET_AND_ADTECH | XETR:DHER | Delivery Hero | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 10_F INTERNET_AND_ADTECH | XETR:HFG | HelloFresh | Beta-Satellit (BETA_SATELLITE) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 20_A STREAMING_AND_MEDIA | XETR:PSM | ProSiebenSat.1 Media | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 20_B TELECOM | XETR:DTE | Deutsche Telekom | Anker (ANCHOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_A DISCRETIONARY_LEADERS | XETR:ADS | adidas | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_A DISCRETIONARY_LEADERS | XETR:PUM | Puma | Qualitätsführer (QUALITY_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_B STAPLES | XETR:BEI | Beiersdorf | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_C RESTAURANTS_AND_TRAVEL | XETR:TUI1 | TUI | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_C RESTAURANTS_AND_TRAVEL | XETR:LHA | Deutsche Lufthansa | Liquiditätssensor (LIQUIDITY_SENSOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_E AUTOS_AND_MOBILITY | XETR:MBG | Mercedes-Benz Group | Anker (ANCHOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_E AUTOS_AND_MOBILITY | XETR:BMW | Bayerische Motoren Werke | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_E AUTOS_AND_MOBILITY | XETR:VOW3 | Volkswagen Vorzüge | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 30_E AUTOS_AND_MOBILITY | XETR:CON | Continental | Qualitätsführer (QUALITY_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 40_A MONEY_CENTER_BANKS | XETR:DBK | Deutsche Bank | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | XETR:DB1 | Deutsche Börse | Anker (ANCHOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 40_D INSURANCE | XETR:ALV | Allianz | Anker (ANCHOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 40_D INSURANCE | XETR:MUV2 | Münchener Rückversicherung | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 50_A PHARMA | XETR:BAYN | Bayer | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 50_A PHARMA | XETR:MRK | Merck | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 50_B MEDTECH_AND_DEVICES | XETR:SHL | Siemens Healthineers | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 60_A AEROSPACE_AND_DEFENSE | XETR:RHM | Rheinmetall | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 60_B MACHINERY_AND_RAIL | XETR:KGX | Kion Group | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 60_B MACHINERY_AND_RAIL | XETR:KRN | Krones | Qualitätsführer (QUALITY_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 60_C TRANSPORT_AND_LOGISTICS | XETR:DHL | DHL Group | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 60_D ELECTRICAL_EQUIPMENT | XETR:SIE | Siemens | Anker (ANCHOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 60_D ELECTRICAL_EQUIPMENT | XETR:ENR | Siemens Energy | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 60_D ELECTRICAL_EQUIPMENT | XETR:NDX1 | Nordex | Beta-Satellit (BETA_SATELLITE) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 80_A MATERIALS | XETR:HEI | Heidelberg Materials | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 80_A MATERIALS | XETR:SZG | Salzgitter | Beta-Satellit (BETA_SATELLITE) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 80_A MATERIALS | XETR:TKA | thyssenkrupp | Liquiditätssensor (LIQUIDITY_SENSOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 80_B UTILITIES | XETR:RWE | RWE | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 80_B UTILITIES | XETR:EOAN | E.ON | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 80_D CHEMICALS | XETR:BAS | BASF | Anker (ANCHOR) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 80_D CHEMICALS | XETR:EVK | Evonik Industries | Qualitätsführer (QUALITY_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 80_D CHEMICALS | XETR:LXS | Lanxess | Beta-Satellit (BETA_SATELLITE) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 90_A REITS | XETR:VNA | Vonovia | Themenführer (THEME_LEADER) |  | https://www.xetra.com/xetra-en/instruments/instruments |
| 90_A REITS | XETR:TEG | TAG Immobilien | Beta-Satellit (BETA_SATELLITE) |  | https://www.xetra.com/xetra-en/instruments/instruments |
