import pandas as pd

# Load the Excel file
file_path = '/content/BRENT_TUFE_DATA.xlsx'  # Update with your file path if needed
df = pd.read_excel(file_path)

# Display column names and first few rows
print("Column Names:\n", df.columns)
print("\nFirst 5 Rows:\n", df.head())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

import matplotlib.pyplot as plt

# Convert 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Brent price in TRY dynamically
df['BRENT_PRICE_TRY'] = df['BRENT PRICE (USD)'] * (df['USDTRY'] / 10000)

# Check the transformed data
print("\nTransformed Data (First 5 Rows):\n", df[['Date', 'BRENT PRICE (USD)', 'USDTRY', 'BRENT_PRICE_TRY']].head())

# Correlation between Brent Price (TRY) and TUFE
correlation_try = df['BRENT_PRICE_TRY'].corr(df['TUFE'])
print(f"\nCorrelation between TRY-based Brent Price and TUFE: {correlation_try}")

# Plot Brent Price (TRY) and TUFE over time
plt.figure(figsize=(12, 6))
plt.plot(df['Date'], df['BRENT_PRICE_TRY'], label='Brent Price (TRY)', color='green')
plt.plot(df['Date'], df['TUFE'], label='CPI (TUFE)', color='orange')
plt.title('Brent Price (TRY) and CPI (TUFE) Over Time')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()

from statsmodels.tsa.stattools import adfuller

# ADF Test for BRENT_PRICE_TRY
adf_brent_try = adfuller(df['BRENT_PRICE_TRY'])
print("\nADF Test for BRENT_PRICE_TRY")
print(f"ADF Statistic: {adf_brent_try[0]}")
print(f"p-value: {adf_brent_try[1]}")
print(f"Critical Values: {adf_brent_try[4]}")

# ADF Test for TUFE
adf_tufe = adfuller(df['TUFE'])
print("\nADF Test for TUFE")
print(f"ADF Statistic: {adf_tufe[0]}")
print(f"p-value: {adf_tufe[1]}")
print(f"Critical Values: {adf_tufe[4]}")

from statsmodels.tsa.stattools import adfuller

# Dynamically calculate Brent Price in TRY
brent_try_dynamic = data['BRENT PRICE (USD)'] * (data['USDTRY'] / 10000)

# ADF Test for Brent Price in TRY (Dynamic Calculation)
adf_brent_try = adfuller(brent_try_dynamic)
print("ADF Test for Brent Price (TRY):")
print(f"ADF Statistic: {adf_brent_try[0]}")
print(f"p-value: {adf_brent_try[1]}")
print(f"Critical Values: {adf_brent_try[4]}")

# ADF Test for TUFE
adf_tufe = adfuller(data['TUFE'])
print("\nADF Test for TUFE:")
print(f"ADF Statistic: {adf_tufe[0]}")
print(f"p-value: {adf_tufe[1]}")
print(f"Critical Values: {adf_tufe[4]}")

# Differencing Brent Price in TRY dynamically
brent_try_diff_dynamic = brent_try_dynamic.diff().dropna()

# ADF Test for Differenced Brent Price in TRY
adf_brent_try_diff = adfuller(brent_try_diff_dynamic)
print("\nADF Test for Differenced Brent Price (TRY):")
print(f"ADF Statistic: {adf_brent_try_diff[0]}")
print(f"p-value: {adf_brent_try_diff[1]}")
print(f"Critical Values: {adf_brent_try_diff[4]}")

# Differencing TUFE dynamically
tufe_diff_dynamic = data['TUFE'].diff().dropna()

# ADF Test for Differenced TUFE
adf_tufe_diff = adfuller(tufe_diff_dynamic)
print("\nADF Test for Differenced TUFE:")
print(f"ADF Statistic: {adf_tufe_diff[0]}")
print(f"p-value: {adf_tufe_diff[1]}")
print(f"Critical Values: {adf_tufe_diff[4]}")

# Differencing the series twice for Brent Price (TRY)
brent_try_diff2 = brent_try_dynamic.diff().diff().dropna()
adf_brent_try_diff2 = adfuller(brent_try_diff2)
print("\nADF Test for Second Differenced Brent Price (TRY):")
print(f"ADF Statistic: {adf_brent_try_diff2[0]}")
print(f"p-value: {adf_brent_try_diff2[1]}")
print(f"Critical Values: {adf_brent_try_diff2[4]}")

# Differencing the series twice for TUFE
tufe_diff2 = data['TUFE'].diff().diff().dropna()
adf_tufe_diff2 = adfuller(tufe_diff2)
print("\nADF Test for Second Differenced TUFE:")
print(f"ADF Statistic: {adf_tufe_diff2[0]}")
print(f"p-value: {adf_tufe_diff2[1]}")
print(f"Critical Values: {adf_tufe_diff2[4]}")

from statsmodels.tsa.stattools import grangercausalitytests

# Preparing data for Granger causality test
data_granger = pd.DataFrame({
    'Brent_Price_TRY_Diff2': brent_try_dynamic.diff().diff().dropna(),
    'TUFE_Diff2': data['TUFE'].diff().diff().dropna()
}).dropna()

# Granger causality test with lags from 1 to 4
print("Granger Causality Test Results")
grangercausalitytests(data_granger, maxlag=4, verbose=True)

import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt
import logging

# Suppress cmdstanpy logs
logging.getLogger('cmdstanpy').setLevel(logging.ERROR)

# Load the data
file_path = 'BRENT_TUFE_DATA.xlsx'
data = pd.read_excel(file_path)

# Prepare the data
data['Date'] = pd.to_datetime(data['Date'])
data.sort_values(by='Date', inplace=True)
data['Brent_Price_Try'] = data['BRENT PRICE (USD)'] * (data['USDTRY'] / 10000)

# Prepare data for Prophet
df_brent = data[['Date', 'Brent_Price_Try']].rename(columns={'Date': 'ds', 'Brent_Price_Try': 'y'})
df_tufe = data[['Date', 'TUFE']].rename(columns={'Date': 'ds', 'TUFE': 'y'})

# Prophet model for Brent Price
model_brent = Prophet(weekly_seasonality=False, daily_seasonality=False)
model_brent.fit(df_brent)
future_brent = model_brent.make_future_dataframe(periods=12, freq='ME')
forecast_brent = model_brent.predict(future_brent)

# Visualize Brent Price predictions
plt.figure(figsize=(10, 6))
model_brent.plot(forecast_brent)
plt.title('Brent Price (TRY) Forecast')
plt.xlabel('Date')
plt.ylabel('Price (TRY)')
plt.grid()
plt.show()

# Prophet model for TUFE
model_tufe = Prophet(weekly_seasonality=False, daily_seasonality=False)
model_tufe.fit(df_tufe)
future_tufe = model_tufe.make_future_dataframe(periods=12, freq='ME')
forecast_tufe = model_tufe.predict(future_tufe)

# Visualize TUFE predictions
plt.figure(figsize=(10, 6))
model_tufe.plot(forecast_tufe)
plt.title('CPI (TUFE) Forecast')
plt.xlabel('Date')
plt.ylabel('TUFE')
plt.grid()
plt.show()
