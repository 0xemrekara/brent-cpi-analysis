# Brent Price (TRY) and CPI (TUFE) Analysis

## Overview

This project performs an analysis of the relationship between Brent oil prices (converted to TRY) and the Turkish Consumer Price Index (TUFE) using time series forecasting models. The primary tools used for this analysis are **Prophet**, **ADF Tests**, and **Granger Causality Tests**.

The analysis aims to provide insights into how Brent oil prices and CPI interact over time and to forecast future trends for both variables.

---

## Data

The data used in this project is from the **BRENT_TUFE_DATA.xlsx** file. This file contains historical data for:

- **BRENT PRICE (USD)**: The price of Brent crude oil in USD.
- **USDTRY**: The exchange rate between USD and Turkish Lira (TRY).
- **TUFE**: The Turkish Consumer Price Index (CPI).
- **Date**: Timestamps for each observation.
---

## Libraries Used

The following libraries are required to run the project:

- `pandas`: For data manipulation and analysis.
- `matplotlib.pyplot`: For visualizing data.
- `statsmodels`: For performing statistical tests like ADF and Granger Causality.
- `prophet`: For time series forecasting.
- `seaborn`: For creating correlation heatmaps.

---

## Steps in the Analysis

### 1. **Data Loading and Preparation**
- Loaded the `BRENT_TUFE_DATA.xlsx` file.
- Converted the **Date** column to datetime format.
- Calculated **Brent Price (TRY)** dynamically.

### 2. **Correlation Analysis**
- Correlation between **Brent Price (TRY)** and **TUFE**.

### 3. **Stationarity Check**
- Used Augmented Dickey-Fuller (ADF) test to check for stationarity.
- Applied first and second differencing to achieve stationarity.

### 4. **Granger Causality Test**
- Examined the causal relationship between Brent Price (TRY) and TUFE.

### 5. **Forecasting**
- Used Prophet to forecast **Brent Price (TRY)** and **TUFE** for the next 12 months.
- Visualized forecast results with confidence intervals.

---

## Outputs

### 1. Correlation
- Displays the correlation coefficient between Brent Price (TRY) and TUFE.

### 2. ADF Test Results
- Determines if the series is stationary. Outputs for both raw and differenced data.

### 3. Granger Causality
- Tests whether changes in Brent Price (TRY) can predict TUFE (or vice versa).

### 4. Forecasts
- 12-month forecasts for both Brent Price (TRY) and TUFE, with confidence intervals.

### 5. Visualizations
- Time series plots for Brent Price (TRY) and TUFE.
- Stationarity visualizations with differencing.
- Forecast plots.
