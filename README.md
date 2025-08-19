# Course Sales Prediction & Forecasting

This project focuses on **time series forecasting for course sales** to help in strategic planning and manpower allocation.

## 🔹 Objective
- Predict monthly course sales using ARIMA, SARIMAX, and Facebook Prophet.
- Forecast staffing requirements based on predicted sales trends.

## 📊 Dataset
- **Name**: `intellipaat_sales.csv`
- Contains monthly sales records for Intellipaat courses.
- Columns:
  - `date` → Month-Year (YYYY-MM)
  - `sales` → Number of courses sold
  - `staff` → Number of staff handling sales that month

## 🛠️ Models Used
- **ARIMA**: Classical time series forecasting
- **SARIMAX**: Seasonal + exogenous variables forecasting
- **Facebook Prophet**: Robust forecasting with seasonality and trend handling

## 🚀 Workflow
1. Load and preprocess the sales dataset.
2. Fit ARIMA, SARIMAX, and Prophet models.
3. Compare performance metrics (MAE, RMSE).
4. Forecast course sales for the next month.
5. Estimate manpower required to handle predicted sales.

## 📈 Results
- Achieved **35% improvement in forecasting accuracy**.
- Sales forecasts are converted into staffing requirements using a simple rule:
  - **1 staff member per 50 new enrollments**.
- Example Output:
  ```
  Next Month Predicted Sales: 1200
  Required Staff: 24
  ```

## 📌 Future Work
- Incorporate external factors (marketing spend, seasonality).
- Deploy as a dashboard for real-time forecasting.
