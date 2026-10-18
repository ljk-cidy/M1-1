"""Independent checks of generated values and report artifacts."""
from pathlib import Path
import json
import math
import re
import pandas as pd

root = Path(__file__).resolve().parent
source = pd.read_csv(root / 'data/samsung_2023_2024.csv', parse_dates=['Date']).set_index('Date')
metrics = pd.read_csv(root / 'data/analysis_metrics.csv', parse_dates=['Date']).set_index('Date')
pd.testing.assert_series_equal(source.Close, metrics.Close)
assert len(source) == 489
assert math.isclose(metrics.MA20.iloc[19], sum(source.Close.iloc[:20])/20)
returns = [100*(b/a-1) for a,b in zip(source.Close, source.Close.iloc[1:])]
assert math.isclose(metrics.Volatility_20D_pct.iloc[20], pd.Series(returns[:20]).std(), rel_tol=1e-10)
monthly = pd.read_csv(root / 'data/monthly_returns.csv', index_col=0)
assert pd.isna(monthly.iloc[0,0])
apr = source.loc['2024-04'].Close.iloc[-1]
mar = source.loc['2024-03'].Close.iloc[-1]
assert math.isclose(monthly.loc['2024-04-30'].iloc[0], (apr/mar-1)*100)
report = (root / 'REPORT.md').read_text(encoding='utf-8')
for image in re.findall(r'!\[[^\]]*\]\(([^)]+)\)', report):
    assert (root / image).read_bytes().startswith(b'\x89PNG\r\n\x1a\n')
notebook = json.loads((root / 'analysis.ipynb').read_text(encoding='utf-8'))
for cell in notebook['cells']:
    if cell['cell_type'] == 'code':
        compile(''.join(cell['source']), 'analysis.ipynb', 'exec')
print('PASS: source preserved; moving mean, volatility, month-end returns, PNG links and notebook code checked.')
