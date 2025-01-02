# Results and Key Findings

## Overview

This document summarizes the results obtained from analyzing Brent Price and CPI (TUFE) data. The analysis highlights the differences between USD-based and TRY-based calculations and emphasizes the stronger insights gained from TRY-based metrics.

---

## 1. Correlation Analysis

### USD-Based Correlation
- **Correlation Coefficient (Brent Price USD vs TUFE)**: Weak or no meaningful correlation detected.
  - **Reason**: The USD-based analysis may not capture the effects of exchange rate fluctuations on CPI.

### TRY-Based Correlation
- **Correlation Coefficient (Brent Price TRY vs TUFE)**: `0.967`
  - Indicates a **strong positive relationship** between Brent oil prices in TRY and CPI (TUFE).
  - Highlights the significant impact of exchange rate-adjusted oil prices on inflation.

---

## 2. Stationarity Tests (TRY-Based)

### Brent Price (TRY)
- **ADF Statistic**: `-2.579`
- **p-value**: `0.097`
- **Critical Values**: `{'1%': -3.460, '5%': -2.874, '10%': -2.573}`
- Result: The series is **not stationary** at the 5% significance level. Differencing was applied.

### CPI (TUFE)
- **ADF Statistic**: `-0.103`
- **p-value**: `0.949`
- **Critical Values**: `{'1%': -3.460, '5%': -2.874, '10%': -2.573}`
- Result: The series is **not stationary**. Double differencing was applied for stationarity.

---

## 3. Granger Causality Test (TRY-Based)

- **Lag 1**: No causality detected (p-value > 0.05).
- **Lag 2**: No causality detected (p-value > 0.05).
- **Lag 3**: No causality detected (p-value > 0.05).
- **Lag 4**: **Causality detected** (p-value < 0.05).
  - Implication: Lagged changes in Brent Price (TRY) may influence CPI (TUFE).

---

## 4. Forecast Results

### Brent Price (TRY) Forecast (Next 12 Months)
| Date       | Predicted Price (TRY) | Lower Bound | Upper Bound |
|------------|------------------------|-------------|-------------|
| 2024-12-31 | 2926.51               | 2773.33     | 3059.64     |
| 2025-01-31 | 3019.97               | 2873.17     | 3174.72     |
| 2025-02-28 | 3002.85               | 2846.99     | 3146.00     |
| ...        | ...                   | ...         | ...         |

### CPI (TUFE) Forecast (Next 12 Months)
| Date       | Predicted CPI (TUFE) | Lower Bound | Upper Bound |
|------------|----------------------|-------------|-------------|
| 2024-12-31 | 2382.08             | 2263.55     | 2493.67     |
| 2025-01-31 | 2446.82             | 2330.39     | 2556.73     |
| 2025-02-28 | 2381.15             | 2271.68     | 2501.38     |
| ...        | ...                 | ...         | ...         |

---

## 5. Key Insights

1. **USD vs TRY Analysis**:
   - USD-based metrics fail to uncover meaningful insights due to the exclusion of exchange rate effects.
   - TRY-based calculations provide a clearer picture of the relationship between Brent Price and CPI.

2. **Strong Correlation**:
   - A strong positive correlation exists between Brent Price (TRY) and CPI (TUFE).

3. **Causality**:
   - Evidence of lagged causality at 4 lags suggests predictive relationships.

4. **Forecasting**:
   - Both Brent Price (TRY) and CPI (TUFE) demonstrate upward trends, reflecting macroeconomic impacts.

---

## Recommendations

1. Expand the dataset to include daily or weekly data for higher granularity.
2. Investigate additional variables (e.g., monetary policies, global oil prices) to refine the analysis.
3. Compare TRY-based findings with real-world economic events to validate insights.

---

## Author

- **Name**: Emre Kara
- **Email**: [karaemre@proton.me](mailto:karaemre@proton.me)
- **GitHub**: [0xemrekara](https://github.com/0xemrekara)
