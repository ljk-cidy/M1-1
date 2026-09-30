# 📈 삼성전자(005930.KS) 주가 시계열 분석 및 트렌드 인사이트 보고서

본 프로젝트는 2023년부터 2024년까지의 삼성전자 주가 데이터를 바탕으로 시계열 패턴(추세, 월별 수익률, 단기 변동성, 시계열 분해)을 분석하고, 데이터 기반의 의사결정 인사이트를 도출한 연구 및 실습 보고서입니다.

---

## 📁 1. 프로젝트 폴더 구조 (Project Directory)

```text
M1-1/
├── data/
│   └── samsung_2023_2024.csv       # Yahoo Finance 수집 원본 데이터
├── images/
│   ├── 01_price_ma_trend.png       # 종가 및 이동평균선(20일/60일) 추이
│   ├── 02_monthly_returns.png      # 월별 수익률(MoM) 바 차트
│   ├── 03_volatility_trend.png     # 20일 이동 표준편차 변동성 추이
│   └── 04_stl_decomposition.png    # 시계열 분해 (Trend/Seasonal/Resid)
├── venv/                           # 독립 가상환경 폴더
├── analysis.ipynb                  # 데이터 수집, 정제, 분석 및 시각화 코드 (Jupyter)
├── REPORT.md                       # 상세 분석 리포트
├── README.md                       # 프로젝트 종합 보고서 (본 문서)
└── requirements.txt                # 파이썬 의존성 패키지 목록
```

---

## 🎯 2. 주요 분석 질문 (Key Questions)

1. **[추세]** 2023~2024년 삼성전자 주가는 지속적인 상승 흐름이었는가, 박스권 형태였는가?
2. **[계절성]** 월별 수익률(MoM) 분석 시 특정 분기나 월에 상승/하락 패턴이 반복되는가?
3. **[변동성]** 단기 변동성(20일 이동 표준편차)이 급증한 시점은 주가의 전환점(고점/저점)과 일치하는가?

---

## 📊 3. 데이터 및 시계열 분석 기법

| 항목 | 내용 |
|------|------|
| 데이터 출처 | Yahoo Finance (005930.KS) |
| 수집 기간 | 2023년 1월 1일 ~ 2024년 12월 31일 (약 490여 개 거래일 데이터 포인트) |
| 전처리 | 주말 및 공휴일 결측치는 전일 종가 대체 방식(`ffill`) 적용 |

**적용 기법**

- **이동평균 (Moving Average):** 20일(단기) 및 60일(중기) 이동평균선을 통한 추세 및 골든/데드크로스 포착
- **수익률 및 변동률:** 일일 수익률 및 월별(MoM) 수익률 집계
- **이동 변동성 (Rolling Volatility):** 20일 이동 표준편차를 이용한 단기 리스크 측정
- **시계열 분해 (Additive Decomposition):** 추세(Trend), 계절성(Seasonal), 잔차(Resid) 요인 분리

---

## 🖼️ 4. 시각화 및 주요 인사이트 (Key Insights)

### 4-1. 주가 추이 및 이동평균선 분석

![종가 및 이동평균선 추이](images/01_price_ma_trend.png)

- **관찰 (Fact):** 2023년 상반기 20일 이동평균선이 60일 이동평균선을 상향 돌파(골든크로스)하며 70,000원 선을 회복했으나, 2024년 하반기 역배열로 전환되며 하락세를 기록함.
- **해석 (Why):** 2023년 AI 반도체 기대감에 따른 자금 유입 이후, 2024년 하반기 메모리 공급 과잉 우려 및 실적 변동으로 투자 심리가 위축됨.

### 4-2. 월별 수익률 추이 (MoM)

![월별 수익률](images/02_monthly_returns.png)

- **관찰 (Fact):** 3~5월 구간은 대체로 양의 수익률을 유지했으나, 8~10월 구간에 큰 폭의 음의 수익률(-5% 이상)이 집중됨.
- **해석 (Why):** 글로벌 금리 정책 불확실성 및 3분기 실적 발표 시즌의 리스크가 반영되었을 가능성.

### 4-3. 20일 이동 변동성 추이

![20일 이동 변동성](images/03_volatility_trend.png)

- **관찰 (Fact):** 20일 이동 표준편차가 2.5% 이상으로 급증한 시점이 주가의 주요 고점 및 저점 형성 시기와 일치함.
- **해석 (Why):** 시장 주도 세력의 매물 소화 및 변동성 확대 과정에서 시장 참여자들의 과도한 반응이 발생함.

### 4-4. 시계열 분해 (Trend / Seasonal / Residual)

![시계열 분해](images/04_stl_decomposition.png)

- **관찰 (Fact):** 주가 데이터를 추세, 계절성, 잔차 요소로 분해하여 노이즈를 제거한 장기 우상향/우하향 추세 단계를 명확히 확인.

---

## 🛠️ 5. 개발 환경 및 재현 가이드 (Setup & Execution)

### 필수 환경

- Python 3.10 이상
- Git 및 VS Code

### 가상환경 세팅 및 의존성 설치

**1) 저장소 클론 (또는 폴더 이동)**

```bash
git clone https://github.com/ljk-cidy/M1-1.git
cd M1-1
```

**2) 가상환경 생성 및 활성화**

```bash
python -m venv venv
```

```bash
# Windows (CMD / PowerShell)
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

**3) 의존성 패키지 설치**

```bash
pip install -r requirements.txt
```

### 코드 실행 및 결과 생성

VS Code에서 `analysis.ipynb` 파일(Jupyter Notebook)을 열고 커널을 `venv`로 지정한 뒤 전체 셀을 실행하면, `data/` 및 `images/` 폴더에 데이터 파일과 시각화 그래프가 자동 저장됩니다.

---

## 🤖 6. AI 활용 기록 (AI Transparency Log)

- **사용 목적:** Python 시각화 코드 버그 수정(`seasonal_decompose` 예외 처리) 및 마크다운 문서 구조화
- **검증 방법:** Jupyter Notebook 셀 단위 실행을 통해 이미지 생성 여부 및 Pandas DataFrame 수치 직접 비교 검증 완료

---

## 🔗 7. 관련 링크

- 상세 분석 리포트: [REPORT.md](./REPORT.md)
- GitHub 저장소: <https://github.com/ljk-cidy/M1-1>