import yfinance as yf
import pandas as pd
import json
import requests
import matplotlib.pyplot as plt



#Using the Ticker module we can create an object that will allow us to access functions to extract data.
apple = yf.Ticker("AAPL")


url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/apple.json"

response = requests.get(url)
with open("apple.json", "wb") as f:
    f.write(response.content)
    #FILE DOWNLOADED    

#Using the attribute info we can extract information about the stock as a Python dictionary.
with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    print(apple_info['country'])


#With the history() method we can get the share price of the stock over a certain period of time. Using the period parameter we can set how far back from the present to get data. The options for period are 1 day (1d), 5d, 1 month (1mo) , 3mo, 6mo, 1 year (1y), 2y, 5y, 10y, ytd, and max.
apple_share_price_data = apple.history(period="max")
print(apple_share_price_data.head())

#We can reset the index of the DataFrame with the reset_index function. We also set the inplace paramter to True so the change takes place to the DataFrame itself.
apple_share_price_data.reset_index(inplace=True)
print(apple_share_price_data.head())

#We can plot the Open price against the Date:
apple_share_price_data.plot(x="Date", y="Open")
plt.show()

#Dividends are the distribution of a companys profits to shareholders. In this case they are defined as an amount of money returned per share an investor owns. Using the variable dividends we can get a dataframe of the data. The period of the data is given by the period defined in the 'history` function.
apple_dividends = apple.dividends
print(apple_dividends.head())

apple.dividends.plot(x='Date',y='Dividends')
plt.show()

#Using the Ticker module we can create an object that will allow us to access functions to extract data.
amd= yf.Ticker("AMD")


url2 = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/data/amd.json"
response = requests.get(url2)
with open("amd.json", "wb") as f:
    f.write(response.content)
    #FILE DOWNLOADED    

#Using the attribute info we can extract information about the stock as a Python dictionary.
with open('amd.json') as json_file:
    amd_info = json.load(json_file)
    print(amd_info['country'])
    print(amd_info['sector'])

amd_share_price_data = amd.history(period='max')
print(amd_share_price_data.head())