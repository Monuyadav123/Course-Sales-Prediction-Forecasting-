import pandas as pd
from prophet import Prophet

def forecast_sales(data_path="data/intellipaat_sales.csv", periods=1):
    # Load dataset
    df = pd.read_csv(data_path, parse_dates=["date"])
    df = df.rename(columns={"date": "ds", "sales": "y"})

    # Prophet Model
    model = Prophet()
    model.fit(df)
    future = model.make_future_dataframe(periods=periods, freq='M')
    forecast = model.predict(future)

    return forecast.tail(periods)[["ds", "yhat"]]
