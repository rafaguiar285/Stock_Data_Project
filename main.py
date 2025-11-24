import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt

import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


# The make_graph function has been modified to use Matplotlib for static graphs. Earlier, it used Plotly to generate interactive dashboards, which caused issues when uploading the notebook in the MARK assignment submission.
def make_graph(stock_data, revenue_data, stock):
    stock_data_specific = stock_data[stock_data.Date <= '2021-06-14']
    revenue_data_specific = revenue_data[revenue_data.Date <= '2021-04-30']

    fig, axes = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

    # Stock price
    axes[0].plot(pd.to_datetime(stock_data_specific.Date), stock_data_specific.Close.astype("float"), label="Share Price", color="blue")
    axes[0].set_ylabel("Price ($US)")
    axes[0].set_title(f"{stock} - Historical Share Price")

    # Revenue
    axes[1].plot(pd.to_datetime(revenue_data_specific.Date), revenue_data_specific.Revenue.astype("float"), label="Revenue", color="green")
    axes[1].set_ylabel("Revenue ($US Millions)")
    axes[1].set_xlabel("Date")
    axes[1].set_title(f"{stock} - Historical Revenue")

    plt.tight_layout()
    plt.show()

#Extract data on to create a ticker object
#TESLA
tesla = yf.Ticker('TSLA')

#Extract stock information and save it in a dataframe
tesla_data = tesla.history(period='max')
#Reset the index
tesla_data.reset_index(inplace=True)
#Display the five first rows
print(tesla_data.head())


#GAME STOP
gameStop = yf.Ticker('GME')

#Extract stock information and save it in a dataframe
gme_data = gameStop.history(period='max')
#Reset the Index
gme_data.reset_index(inplace=True)
#Display the five first rows
print(tesla_data.head())


from Webscraping_Extract_Revenue_Data import tesla_revenue, gameStopRevenue

#PLOT THE GRAPHS
make_graph(tesla_data, tesla_revenue, 'Tesla')

make_graph(gme_data, gameStopRevenue, 'GameStop')