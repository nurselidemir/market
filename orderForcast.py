import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA

class SupplyOrderForecast:
    def __init__(self, data):
        """
        Initialize the forecasting model.
        :param data: A Pandas DataFrame with columns ['date', 'orders'].
        """
        self.data = data
        self.model = None

    def preprocess_data(self):
        """Preprocess the data by setting the date as index and handling missing values."""
        self.data['date'] = pd.to_datetime(self.data['date'])
        self.data.set_index('date', inplace=True)
        self.data = self.data.asfreq('D')  # Ensure daily frequency
        self.data.fillna(method='ffill', inplace=True)

    def train_model(self, order=(2,1,2)):
        """Train an ARIMA model on the supply order data."""
        self.model = ARIMA(self.data['orders'], order=order)
        self.model = self.model.fit()
        print("Model trained successfully.")

    def forecast(self, steps=30):
        """Forecast future supply orders."""
        forecast_values = self.model.forecast(steps=steps)
        forecast_dates = pd.date_range(start=self.data.index[-1], periods=steps+1, freq='D')[1:]
        forecast_df = pd.DataFrame({'date': forecast_dates, 'forecasted_orders': forecast_values})
        return forecast_df

    def plot_forecast(self, steps=30):
        """Plot historical and forecasted supply orders."""
        forecast_df = self.forecast(steps)
        plt.figure(figsize=(10, 5))
        plt.plot(self.data.index, self.data['orders'], label='Historical Orders')
        plt.plot(forecast_df['date'], forecast_df['forecasted_orders'], label='Forecasted Orders', linestyle='dashed')
        plt.legend()
        plt.xlabel('Date')
        plt.ylabel('Orders')
        plt.title('Supply Order Forecast')
        plt.show()

# Example usage:
# df = pd.read_csv('orders_data.csv')
# forecast_model = SupplyOrderForecast(df)
# forecast_model.preprocess_data()
# forecast_model.train_model()
# print(forecast_model.forecast())
# forecast_model.plot_forecast()
