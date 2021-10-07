# Packages

import pandas_datareader as web
import pandas as pd
import datetime as dt
import numpy as np
import matplotlib.pyplot as plt

# Reading the data

start = dt.datetime(2015, 1, 1)
end = dt.datetime(2021, 6, 30)
ticker = "AAPL"
source = "yahoo"

prices = web.DataReader(ticker, source, start, end)  # Time series data

df = prices["Adj Close"]


# Calculating the day-to-day stock returns
returns = df.pct_change()

# Extracting the last price
last_price = df[-1]
# print(last_price)

# Simulation

n = 10 ** 3
t = 252  # number of days in the future we want to simulate the price (there are 252 trading days in a year)

simulation_df = pd.DataFrame()  # Creating an empty dataframe to initialize
for i in range(1, n, 1):
    count = 0
    daily_std = returns.std()  # Stock volatility

    price_series = []

    price = last_price * (1 + np.random.normal(0, daily_std))
    price_series.append(price)

    for j in range(1, t, 1):
        if count == t - 1:
            break
        price = price_series[count] * (1 + np.random.normal(0, daily_std))
        price_series.append(price)
        count = count + 1

    simulation_df[i] = price_series


# Plot

fig = plt.figure()
plt.plot(simulation_df)
plt.xlabel("Trading days")
plt.ylabel("Simulated Price")
plt.title("Simulated prices for: " + ticker)
# plt.grid()
plt.axhline(y=last_price, color="b", linestyle="-")
plt.show()








