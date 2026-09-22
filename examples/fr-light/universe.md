> Généré par `python examples/build_examples.py`, à partir de
> `examples/seeds/fr.tsv`. Voici l'artefact `.md` qu'un build produit, versionné pour
> être lu sans rien exécuter.
> Toutes les valeurs de métriques y sont illustratives — voir [README.md](../README.md).

# Univers de titres FR

- Profondeur : Léger
- Faits arrêtés au : 2026-09-17
- Version : `80aa66787f2e`
- Titres : 45
- Thèmes : 28
- Stabilité : 1.00 · 45 / 45 · ±1%
- Thème le plus large : 30_D · 4 · 9% · part pondérée 4
- Entrées TradingView : 73 / 1000
- Candidats écartés ou non retenus : 19
- Validation : CONFORME

## Répartition des rôles

| Rôle | Nombre |
|---|---:|
| Ancrage (ANCHOR) | 8 |
| Référence (BENCHMARK) | 1 |
| Satellite bêta (BETA_SATELLITE) | 6 |
| Indicateur de largeur (BREADTH_PROXY) | 1 |
| Capteur de liquidité (LIQUIDITY_SENSOR) | 2 |
| Chef de file qualité (QUALITY_LEADER) | 2 |
| Chef de file thématique (THEME_LEADER) | 25 |

## Couverture thématique

| Code | Groupe | Thème | Niveau | Nombre |
|---|---|---|---:|---:|
| 00_A | Indices de marché | BROAD_MARKET_ETF | 1 | 2 |
| 00_B | Indices de marché | EQUAL_WEIGHT_AND_BREADTH | 2 | 0 |
| 00_C | Indices de marché | VOLATILITY_AND_HEDGES | 3 | 0 |
| 10_B | Technologie | SEMICONDUCTORS | 1 | 1 |
| 10_C | Technologie | SEMICAP_EQUIPMENT | 1 | 1 |
| 10_D | Technologie | ENTERPRISE_SOFTWARE | 1 | 2 |
| 10_E | Technologie | CYBERSECURITY | 3 | 0 |
| 10_F | Technologie | INTERNET_AND_ADTECH | 1 | 1 |
| 10_G | Technologie | IT_SERVICES_AND_CONSULTING | 2 | 0 |
| 11_B | Infrastructure IA | DATA_CENTER_AND_POWER | 1 | 1 |
| 20_A | Communication | STREAMING_AND_MEDIA | 1 | 2 |
| 20_B | Communication | TELECOM | 1 | 1 |
| 20_C | Communication | GAMING_AND_INTERACTIVE | 3 | 0 |
| 20_D | Communication | ADVERTISING_AND_MARKETING | 3 | 0 |
| 30_A | Consommation | DISCRETIONARY_LEADERS | 1 | 1 |
| 30_B | Consommation | STAPLES | 1 | 2 |
| 30_C | Consommation | RESTAURANTS_AND_TRAVEL | 1 | 2 |
| 30_D | Consommation | APPAREL_AND_LUXURY | 1 | 4 |
| 30_E | Consommation | AUTOS_AND_MOBILITY | 1 | 3 |
| 40_A | Finance | MONEY_CENTER_BANKS | 1 | 2 |
| 40_B | Finance | PAYMENTS | 1 | 1 |
| 40_C | Finance | ASSET_MANAGERS_AND_EXCHANGES | 1 | 1 |
| 40_D | Finance | INSURANCE | 1 | 2 |
| 40_E | Finance | REGIONAL_BANKS | 2 | 0 |
| 50_A | Santé | PHARMA | 1 | 1 |
| 50_B | Santé | MEDTECH_AND_DEVICES | 1 | 1 |
| 50_D | Santé | BIOTECH | 2 | 0 |
| 50_E | Santé | LIFE_SCIENCE_TOOLS | 2 | 0 |
| 50_F | Santé | HEALTHCARE_DISTRIBUTION | 3 | 0 |
| 60_A | Industrie | AEROSPACE_AND_DEFENSE | 1 | 3 |
| 60_B | Industrie | MACHINERY_AND_RAIL | 1 | 1 |
| 60_C | Industrie | TRANSPORT_AND_LOGISTICS | 1 | 1 |
| 60_D | Industrie | ELECTRICAL_EQUIPMENT | 2 | 0 |
| 60_E | Industrie | ENGINEERING_AND_CONSTRUCTION | 1 | 1 |
| 60_F | Industrie | DISTRIBUTION_AND_SUPPLY | 3 | 0 |
| 70_A | Énergie | INTEGRATED_ENERGY | 1 | 1 |
| 70_B | Énergie | OILFIELD_AND_MIDSTREAM | 1 | 2 |
| 70_C | Énergie | EXPLORATION_AND_PRODUCTION | 2 | 0 |
| 80_A | Matériaux et services publics | MATERIALS | 1 | 2 |
| 80_B | Matériaux et services publics | UTILITIES | 1 | 1 |
| 80_C | Matériaux et services publics | METALS_AND_MINING | 2 | 0 |
| 80_D | Matériaux et services publics | CHEMICALS | 3 | 0 |
| 80_E | Matériaux et services publics | WATER_AND_WASTE | 3 | 0 |
| 90_A | Immobilier | REITS | 1 | 2 |
| 90_C | Immobilier | REAL_ESTATE_SERVICES | 3 | 0 |

## Comment les mesures ont été produites

| Mesure | Base | Méthode | Fenêtre |
|---|---|---|---|
| beta_stability | mesuré (measured) | concordance de l'estimation du bêta entre les deux moitiés de la fenêtre | 180d |
| beta_strength | mesuré (measured) | valeur absolue du bêta OLS contre EURONEXT:CAC ; un bêta de 2,0 vaut 100 | 180d |
| heat | jugé (judged) | saut de volume confirmé par les données de marché, jamais une séance isolée | — |
| independence | mesuré (measured) | 100 moins le R² de la régression des rendements quotidiens sur EURONEXT:CAC | 180d |
| liquidity | mesuré (measured) | percentile en coupe transversale du volume quotidien moyen | 30d |
| quality | mixte (blended) | ancienneté de cotation et percentile de taille, complétés par un jugement de durabilité | — |

Pour 36 composants sur 45, quality combine 50% de règle et 50% de jugement. La moitié réglée lit l'ancienneté de cotation, le percentile de taille et les signaux défavorables ; la moitié jugée est ce qu'aucune statistique ne couvre.

## Pourquoi des candidats n'ont pas été retenus

| Motif | Nombre |
|---|---:|
| places déjà attribuées (not_selected_under_budget) | 17 |
| type d'instrument exclu (excluded_instrument_type) | 1 |
| redondant avec un composant (redundant_with_member) | 1 |

## Composants

| Thème | Ticker | Nom | Rôle | Motif | Source |
|---|---|---|---|---|---|
| 00_A BROAD_MARKET_ETF | EURONEXT:CAC | Amundi CAC 40 UCITS ETF | Référence (BENCHMARK) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 00_A BROAD_MARKET_ETF | EURONEXT:CW8 | Amundi MSCI World UCITS ETF | Indicateur de largeur (BREADTH_PROXY) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 10_B SEMICONDUCTORS | EURONEXT:STMPA | STMicroelectronics | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 10_C SEMICAP_EQUIPMENT | EURONEXT:SOI | Soitec | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 10_D ENTERPRISE_SOFTWARE | EURONEXT:DSY | Dassault Systèmes | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 10_D ENTERPRISE_SOFTWARE | EURONEXT:ATO | Atos | Capteur de liquidité (LIQUIDITY_SENSOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 10_F INTERNET_AND_ADTECH | EURONEXT:PUB | Publicis Groupe | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 11_B DATA_CENTER_AND_POWER | EURONEXT:SU | Schneider Electric | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 20_A STREAMING_AND_MEDIA | EURONEXT:VIV | Vivendi | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 20_A STREAMING_AND_MEDIA | EURONEXT:TFI | TF1 | Satellite bêta (BETA_SATELLITE) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 20_B TELECOM | EURONEXT:ORA | Orange | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_A DISCRETIONARY_LEADERS | EURONEXT:FDJ | La Française des Jeux | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_B STAPLES | EURONEXT:OR | L'Oréal | Ancrage (ANCHOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_B STAPLES | EURONEXT:BN | Danone | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_C RESTAURANTS_AND_TRAVEL | EURONEXT:AC | Accor | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_C RESTAURANTS_AND_TRAVEL | EURONEXT:AF | Air France-KLM | Capteur de liquidité (LIQUIDITY_SENSOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_D APPAREL_AND_LUXURY | EURONEXT:MC | LVMH Moët Hennessy Louis Vuitton | Ancrage (ANCHOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_D APPAREL_AND_LUXURY | EURONEXT:RMS | Hermès International | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_D APPAREL_AND_LUXURY | EURONEXT:KER | Kering | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_D APPAREL_AND_LUXURY | EURONEXT:EL | EssilorLuxottica | Chef de file qualité (QUALITY_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_E AUTOS_AND_MOBILITY | EURONEXT:STLAP | Stellantis | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_E AUTOS_AND_MOBILITY | EURONEXT:RNO | Renault | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 30_E AUTOS_AND_MOBILITY | EURONEXT:FR | Valeo | Satellite bêta (BETA_SATELLITE) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 40_A MONEY_CENTER_BANKS | EURONEXT:BNP | BNP Paribas | Ancrage (ANCHOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 40_A MONEY_CENTER_BANKS | EURONEXT:GLE | Société Générale | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 40_B PAYMENTS | EURONEXT:WLN | Worldline | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | EURONEXT:ENX | Euronext | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 40_D INSURANCE | EURONEXT:CS | AXA | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 40_D INSURANCE | EURONEXT:SCR | SCOR | Satellite bêta (BETA_SATELLITE) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 50_A PHARMA | EURONEXT:SAN | Sanofi | Ancrage (ANCHOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 50_B MEDTECH_AND_DEVICES | EURONEXT:BIM | bioMérieux | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 60_A AEROSPACE_AND_DEFENSE | EURONEXT:AIR | Airbus | Ancrage (ANCHOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 60_A AEROSPACE_AND_DEFENSE | EURONEXT:SAF | Safran | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 60_A AEROSPACE_AND_DEFENSE | EURONEXT:HO | Thales | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 60_B MACHINERY_AND_RAIL | EURONEXT:ALO | Alstom | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 60_C TRANSPORT_AND_LOGISTICS | EURONEXT:GET | Getlink | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 60_E ENGINEERING_AND_CONSTRUCTION | EURONEXT:DG | Vinci | Ancrage (ANCHOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 70_A INTEGRATED_ENERGY | EURONEXT:TTE | TotalEnergies | Ancrage (ANCHOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 70_B OILFIELD_AND_MIDSTREAM | EURONEXT:TE | Technip Energies | Chef de file qualité (QUALITY_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 70_B OILFIELD_AND_MIDSTREAM | EURONEXT:VK | Vallourec | Satellite bêta (BETA_SATELLITE) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 80_A MATERIALS | EURONEXT:AI | Air Liquide | Ancrage (ANCHOR) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 80_A MATERIALS | EURONEXT:NK | Imerys | Satellite bêta (BETA_SATELLITE) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 80_B UTILITIES | EURONEXT:ENGI | Engie | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 90_A REITS | EURONEXT:URW | Unibail-Rodamco-Westfield | Chef de file thématique (THEME_LEADER) |  | https://live.euronext.com/en/markets/paris/equities/list |
| 90_A REITS | EURONEXT:COV | Covivio | Satellite bêta (BETA_SATELLITE) |  | https://live.euronext.com/en/markets/paris/equities/list |
