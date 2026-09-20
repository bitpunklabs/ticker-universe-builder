> `python examples/build_examples.py` 가 `examples/seeds/kr.tsv` 로부터 생성.
> build 가 써내는 `.md` 산출물이며, 아무것도 실행하지 않고 읽을 수 있도록 저장소에 넣었다.
> 지표 값은 모두 예시일 뿐이다 — [README.md](../README.md) 참고.

# KR 종목 유니버스

- 깊이: 간이
- 사실 기준일: 2026-09-17
- 버전: `4e7765bf007c`
- 종목 수: 55
- 테마 수: 35
- 최대 테마: 00_A · 3 · 5% · 가중 기준 1
- TradingView 항목 수: 90 / 1000
- 탈락하거나 제외된 후보: 37
- 검증: 통과

## 역할 분포

| 역할 | 개수 |
|---|---:|
| 앵커 (ANCHOR) | 5 |
| 벤치마크 (BENCHMARK) | 2 |
| 베타 위성 (BETA_SATELLITE) | 7 |
| 시장 폭 대리 (BREADTH_PROXY) | 1 |
| 유동성 관측 (LIQUIDITY_SENSOR) | 1 |
| 신규 상장 (NEW_LISTING) | 1 |
| 우량 주도주 (QUALITY_LEADER) | 4 |
| 테마 주도주 (THEME_LEADER) | 34 |

## 테마 커버리지

| 코드 | 대분류 | 테마 | 단계 | 개수 |
|---|---|---|---:|---:|
| 00_A | 시장 벤치마크 | BROAD_MARKET_ETF | 1 | 3 |
| 00_B | 시장 벤치마크 | EQUAL_WEIGHT_AND_BREADTH | 2 | 0 |
| 00_C | 시장 벤치마크 | VOLATILITY_AND_HEDGES | 3 | 0 |
| 10_A | 테크놀로지 | MEGACAP_PLATFORMS | 1 | 1 |
| 10_B | 테크놀로지 | SEMICONDUCTORS | 1 | 3 |
| 10_C | 테크놀로지 | SEMICAP_EQUIPMENT | 1 | 1 |
| 10_D | 테크놀로지 | ENTERPRISE_SOFTWARE | 1 | 1 |
| 10_E | 테크놀로지 | CYBERSECURITY | 1 | 1 |
| 10_F | 테크놀로지 | INTERNET_AND_ADTECH | 1 | 2 |
| 10_H | 테크놀로지 | HARDWARE_AND_NETWORKING | 3 | 0 |
| 11_A | AI 인프라 | AI_COMPUTE | 1 | 1 |
| 11_B | AI 인프라 | DATA_CENTER_AND_POWER | 1 | 2 |
| 20_A | 커뮤니케이션 | STREAMING_AND_MEDIA | 1 | 1 |
| 20_B | 커뮤니케이션 | TELECOM | 1 | 1 |
| 20_C | 커뮤니케이션 | GAMING_AND_INTERACTIVE | 1 | 2 |
| 20_D | 커뮤니케이션 | ADVERTISING_AND_MARKETING | 3 | 0 |
| 20_E | 커뮤니케이션 | ENTERTAINMENT_AND_MUSIC | 1 | 2 |
| 30_A | 소비재 | DISCRETIONARY_LEADERS | 1 | 2 |
| 30_B | 소비재 | STAPLES | 1 | 1 |
| 30_C | 소비재 | RESTAURANTS_AND_TRAVEL | 1 | 1 |
| 30_D | 소비재 | APPAREL_AND_LUXURY | 2 | 0 |
| 30_E | 소비재 | AUTOS_AND_MOBILITY | 1 | 3 |
| 35_A | 조선·중공업 | SHIPBUILDING | 1 | 1 |
| 35_B | 조선·중공업 | DEFENSE_AND_HEAVY | 2 | 0 |
| 40_A | 금융 | MONEY_CENTER_BANKS | 1 | 2 |
| 40_B | 금융 | PAYMENTS | 1 | 1 |
| 40_C | 금융 | ASSET_MANAGERS_AND_EXCHANGES | 1 | 1 |
| 40_D | 금융 | INSURANCE | 1 | 1 |
| 40_E | 금융 | REGIONAL_BANKS | 2 | 0 |
| 40_F | 금융 | FINTECH_LENDERS | 3 | 0 |
| 50_A | 헬스케어 | PHARMA | 1 | 2 |
| 50_B | 헬스케어 | MEDTECH_AND_DEVICES | 1 | 1 |
| 50_C | 헬스케어 | MANAGED_CARE | 3 | 0 |
| 50_D | 헬스케어 | BIOTECH | 1 | 2 |
| 50_E | 헬스케어 | LIFE_SCIENCE_TOOLS | 2 | 0 |
| 50_F | 헬스케어 | HEALTHCARE_DISTRIBUTION | 3 | 0 |
| 60_A | 산업재 | AEROSPACE_AND_DEFENSE | 1 | 1 |
| 60_B | 산업재 | MACHINERY_AND_RAIL | 1 | 2 |
| 60_C | 산업재 | TRANSPORT_AND_LOGISTICS | 1 | 3 |
| 60_D | 산업재 | ELECTRICAL_EQUIPMENT | 2 | 0 |
| 60_E | 산업재 | ENGINEERING_AND_CONSTRUCTION | 3 | 0 |
| 60_F | 산업재 | DISTRIBUTION_AND_SUPPLY | 3 | 0 |
| 70_A | 에너지 | INTEGRATED_ENERGY | 1 | 1 |
| 70_B | 에너지 | OILFIELD_AND_MIDSTREAM | 1 | 1 |
| 70_C | 에너지 | EXPLORATION_AND_PRODUCTION | 2 | 0 |
| 80_A | 소재·유틸리티 | MATERIALS | 1 | 2 |
| 80_B | 소재·유틸리티 | UTILITIES | 1 | 1 |
| 80_C | 소재·유틸리티 | METALS_AND_MINING | 2 | 0 |
| 80_D | 소재·유틸리티 | CHEMICALS | 1 | 2 |
| 80_E | 소재·유틸리티 | WATER_AND_WASTE | 3 | 0 |
| 80_F | 소재·유틸리티 | BATTERY_CHAIN | 1 | 2 |
| 90_A | 부동산 | REITS | 1 | 1 |

## 지표를 산출한 방법

| 지표 | 근거 | 방법 | 기간 |
|---|---|---|---|
| beta_stability | 실측 (measured) | 구간을 전반과 후반으로 나눴을 때 베타 추정치의 일치 정도 | 180d |
| beta_strength | 실측 (measured) | KRX:069500 대비 OLS 베타의 절댓값. 베타 2.0을 100으로 본다 | 180d |
| heat | 판단 (judged) | 거래대금 급증. 거래소 데이터로 확인된 것만 인정하며 하루 변동은 제외 | — |
| independence | 실측 (measured) | 일간 수익률을 KRX:069500에 회귀한 결정계수를 100에서 뺀 값 | 180d |
| liquidity | 실측 (measured) | 30일 일평균 거래대금의 횡단면 백분위 | 30d |
| quality | 규칙과 판단 혼합 (blended) | 상장 기간과 규모 백분위에 사업 지속성 판단을 더한 값 | — |

전체 55종목 중 45종목에서 quality는 규칙 50%과 판단 50%의 조합입니다. 규칙 쪽은 상장 기간, 규모 분위, 부정적 지정을 읽고, 판단 쪽은 어떤 통계로도 덮이지 않는 부분입니다.

## 후보가 들어가지 못한 이유

| 사유 | 개수 |
|---|---:|
| 정원이 모두 찼음 (not_selected_under_budget) | 35 |
| 동일 자산 중복 (duplicate_asset) | 1 |
| 제외 대상 상품 유형 (excluded_instrument_type) | 1 |

## 구성 종목

| 테마 | 티커 | 이름 | 역할 | 사유 | 출처 |
|---|---|---|---|---|---|
| 00_A BROAD_MARKET_ETF | KRX:102110 | TIGER 200 | 벤치마크 (BENCHMARK) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 00_A BROAD_MARKET_ETF | KRX:069500 | KODEX 200 | 벤치마크 (BENCHMARK) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 00_A BROAD_MARKET_ETF | KRX:229200 | KODEX 코스닥150 | 시장 폭 대리 (BREADTH_PROXY) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_A MEGACAP_PLATFORMS | KRX:035420 | NAVER | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_B SEMICONDUCTORS | KRX:005930 | 삼성전자 | 앵커 (ANCHOR) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_B SEMICONDUCTORS | KRX:000660 | SK하이닉스 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_B SEMICONDUCTORS | KRX:000990 | DB하이텍 | 우량 주도주 (QUALITY_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_C SEMICAP_EQUIPMENT | KRX:042700 | 한미반도체 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_D ENTERPRISE_SOFTWARE | KRX:012510 | 더존비즈온 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_E CYBERSECURITY | KRX:053800 | 안랩 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_F INTERNET_AND_ADTECH | KRX:035720 | 카카오 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 10_F INTERNET_AND_ADTECH | KRX:089600 | 나스미디어 | 우량 주도주 (QUALITY_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 11_A AI_COMPUTE | KRX:007660 | 이수페타시스 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 11_B DATA_CENTER_AND_POWER | KRX:034020 | 두산에너빌리티 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 11_B DATA_CENTER_AND_POWER | KRX:298040 | 효성중공업 | 우량 주도주 (QUALITY_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 20_A STREAMING_AND_MEDIA | KRX:035760 | CJ ENM | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 20_B TELECOM | KRX:017670 | SK텔레콤 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 20_C GAMING_AND_INTERACTIVE | KRX:259960 | 크래프톤 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 20_C GAMING_AND_INTERACTIVE | KRX:263750 | 펄어비스 | 베타 위성 (BETA_SATELLITE) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 20_E ENTERTAINMENT_AND_MUSIC | KRX:352820 | 하이브 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 20_E ENTERTAINMENT_AND_MUSIC | KRX:122870 | 와이지엔터테인먼트 | 베타 위성 (BETA_SATELLITE) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 30_A DISCRETIONARY_LEADERS | KRX:090430 | 아모레퍼시픽 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 30_A DISCRETIONARY_LEADERS | KRX:004170 | 신세계 | 우량 주도주 (QUALITY_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 30_B STAPLES | KRX:051900 | LG생활건강 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 30_C RESTAURANTS_AND_TRAVEL | KRX:008770 | 호텔신라 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 30_E AUTOS_AND_MOBILITY | KRX:005380 | 현대차 | 앵커 (ANCHOR) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 30_E AUTOS_AND_MOBILITY | KRX:000270 | 기아 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 30_E AUTOS_AND_MOBILITY | KRX:018880 | 한온시스템 | 베타 위성 (BETA_SATELLITE) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 35_A SHIPBUILDING | KRX:009540 | HD한국조선해양 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 40_A MONEY_CENTER_BANKS | KRX:105560 | KB금융 | 앵커 (ANCHOR) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 40_A MONEY_CENTER_BANKS | KRX:055550 | 신한지주 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 40_B PAYMENTS | KRX:377300 | 카카오페이 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 40_C ASSET_MANAGERS_AND_EXCHANGES | KRX:006800 | 미래에셋증권 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 40_D INSURANCE | KRX:032830 | 삼성생명 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 50_A PHARMA | KRX:000100 | 유한양행 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 50_A PHARMA | KRX:069620 | 대웅제약 | 베타 위성 (BETA_SATELLITE) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 50_B MEDTECH_AND_DEVICES | KRX:328130 | 루닛 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 50_D BIOTECH | KRX:207940 | 삼성바이오로직스 | 앵커 (ANCHOR) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 50_D BIOTECH | KRX:068270 | 셀트리온 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 60_A AEROSPACE_AND_DEFENSE | KRX:012450 | 한화에어로스페이스 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 60_B MACHINERY_AND_RAIL | KRX:241560 | 두산밥캣 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 60_B MACHINERY_AND_RAIL | KRX:454910 | 두산로보틱스 | 신규 상장 (NEW_LISTING) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 60_C TRANSPORT_AND_LOGISTICS | KRX:000120 | CJ대한통운 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 60_C TRANSPORT_AND_LOGISTICS | KRX:028670 | 팬오션 | 베타 위성 (BETA_SATELLITE) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 60_C TRANSPORT_AND_LOGISTICS | KRX:011200 | HMM | 유동성 관측 (LIQUIDITY_SENSOR) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 70_A INTEGRATED_ENERGY | KRX:010950 | S-Oil | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 70_B OILFIELD_AND_MIDSTREAM | KRX:036460 | 한국가스공사 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 80_A MATERIALS | KRX:005490 | POSCO홀딩스 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 80_A MATERIALS | KRX:004020 | 현대제철 | 베타 위성 (BETA_SATELLITE) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 80_B UTILITIES | KRX:015760 | 한국전력 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 80_D CHEMICALS | KRX:051910 | LG화학 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 80_D CHEMICALS | KRX:011170 | 롯데케미칼 | 베타 위성 (BETA_SATELLITE) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 80_F BATTERY_CHAIN | KRX:373220 | LG에너지솔루션 | 앵커 (ANCHOR) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 80_F BATTERY_CHAIN | KRX:006400 | 삼성SDI | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
| 90_A REITS | KRX:330590 | 롯데리츠 | 테마 주도주 (THEME_LEADER) |  | https://data.krx.co.kr/contents/MDC/MDI/mdiLoader/index.cmd?menuId=MDC0201 |
