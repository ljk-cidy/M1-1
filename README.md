# 삼성전자 시계열 분석 — M1-1

2023~2024년의 저장 가격 489개로 추세·월별 수익률·변동성을 분석합니다. [분석 리포트](REPORT.md)에서 결과와 한계를 확인할 수 있습니다.

## 실행 방법

Python 3.10 이상, 저장소 루트에서 실행합니다.

```sh
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
python analysis.py
```

또는 `jupyter notebook analysis.ipynb`를 열고 위에서 아래로 실행합니다. 인터넷 없이 기존 CSV를 사용합니다. 실행하면 REPORT.md, 그림 4개, 파생 CSV 3개를 갱신하며 원본 CSV는 보존합니다.

## 미션 대응

- REPORT.md: 질문 3개, 정제·이상치 기준, 수치 근거가 있는 인사이트 3개, 관찰/가설 구분, 결론·한계, AI 사용 로그
- analysis.py / analysis.ipynb: 이동평균·변화율·변동성 및 보너스 STL 분해
- images/: 리포트에 포함되는 시각화 4개
- data/samsung_2023_2024.csv: 기존 Yahoo Finance 수집 표본
- data/analysis_metrics.csv, monthly_returns.csv, flagged_returns.csv: 검증용 파생 자료

수집 시각·가격 조정 설정·데이터 라이선스의 불확실성은 리포트에 명시했습니다. 대시보드는 구현하지 않았습니다.

검증: `python verify_analysis.py`로 이동평균·변동성·월말 변화율과 이미지 링크를 점검합니다. 실제 실행 버전은 REPORT.md의 AI 사용 로그에 기록됩니다.
