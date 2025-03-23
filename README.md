# Brent Price (TRY) and CPI (TUFE) Analysis

Overview: This project performs an analysis of the relationship between Brent oil prices (converted to TRY) and the Turkish Consumer Price Index (TUFE) using time series econometrics and forecasting models. The focus is on uncovering meaningful relationships using Correlation Analysis, Augmented Dickey-Fuller (ADF) Tests for stationarity, Granger Causality Tests for directional influence, and Prophet Forecasting for 24-month projections. The study compares both USD-based and TRY-based Brent price calculations, highlighting the importance of exchange rate effects on CPI dynamics in Turkey.

Data: The data is stored in BRENT_TUFE_DATA.xlsx and contains: Date (monthly), BRENT PRICE (USD), USDTRY (exchange rate), and TUFE (CPI). TRY-based Brent prices are calculated as:  
BRENT_PRICE_TRY = BRENT PRICE (USD) * (USDTRY / 10000)

Libraries Used: pandas, matplotlib.pyplot, seaborn, statsmodels, prophet, and openpyxl.

Steps in the Analysis:
1. Data Loading and Preparation – Load the dataset, convert Date to datetime, set Date as index, and calculate Brent Price in TRY.
2. Correlation Analysis – Compare Brent Price (USD) vs. TUFE (weak correlation) and Brent Price (TRY) vs. TUFE (strong correlation, ~0.967).
3. Stationarity Check – Run ADF tests on raw, first-differenced, and second-differenced series; TUFE requires second differencing while Brent (TRY) requires first differencing.
4. Granger Causality Test – Conduct tests with lags 1–4; significant causality is detected at lag 4 (p < 0.05).
5. Forecasting – Use Prophet to forecast both TUFE and Brent Price (TRY) for 24 months (Jan 2025 – Dec 2026) with 80% confidence intervals.

Outputs:
- Correlation: USD-based Brent price shows no meaningful correlation with TUFE, while TRY-based Brent price shows a strong positive correlation (~0.967).
- ADF Tests: Both TUFE and Brent (TRY) are non-stationary initially; stationarity is achieved after appropriate differencing.
- Granger Causality: Lag 4 indicates that Brent Price (TRY) Granger-causes TUFE (p = 0.0434).
- Forecasts: Both series exhibit upward trends in the forecast period. Example predictions include:
   - **Brent Price (TRY):** 2025-01-31: 3019.97 (CI: 2873.17 – 3174.72), 2025-12-31: 3160.67 (CI: 2974.00 – 3377.18)
   - **TUFE:** 2025-01-31: 2446.82 (CI: 2330.39 – 2556.73), 2025-12-31: 2719.44 (CI: 2547.83 – 2883.27)
- Visualizations: Time series plots, stationarity checks (raw vs. differenced data), a correlation heatmap, a Granger causality p-value bar chart, and forecast plots are included in the analysis.

Author: Emre Kara | GitHub: [0xemrekara](https://github.com/0xemrekara) | Email: karaemre@proton.me
