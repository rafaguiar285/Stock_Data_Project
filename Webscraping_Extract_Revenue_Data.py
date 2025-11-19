import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import warnings
# Ignore all warnings
warnings.filterwarnings("ignore", category=FutureWarning)


#TESLA

url = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/revenue.htm'
html_data = requests.get(url).text

soup = BeautifulSoup(html_data,'html.parser')

#Create An empty data frame
tesla_revenue = pd.DataFrame(columns=['Date','Revenue'])

#Find the relevant table
for row in soup.find_all("tbody")[1].find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    tesla_revenue = pd.concat([tesla_revenue, pd.DataFrame({"Date":[date], "Revenue":[revenue]})], ignore_index=True)

#Remove the comma and dollar sign from the Revenue column.
tesla_revenue["Revenue"] = tesla_revenue['Revenue'].str.replace(',|\$',"",regex=True)

#Remove an null or empty strings in the Revenue column.
tesla_revenue.dropna(inplace=True)
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

#Print the five last rows
print(tesla_revenue.tail())


#GAME STOP

url2 = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/stock.html'
html_data2 = requests.get(url2).text

soup2 = BeautifulSoup(html_data2,'html.parser')

#Create An empty data frame
gameStopRevenue = pd.DataFrame(columns=['Date','Revenue'])

#Find the relevant table
for row in soup2.find_all("tbody")[1].find_all('tr'):
    col = row.find_all("td")
    date = col[0].text
    revenue = col[1].text
    gameStopRevenue = pd.concat([gameStopRevenue, pd.DataFrame({"Date":[date], "Revenue":[revenue]})], ignore_index=True)

#Remove the comma and dollar sign from the Revenue column.
gameStopRevenue["Revenue"] = gameStopRevenue['Revenue'].str.replace(',|\$',"",regex=True)

#Remove an null or empty strings in the Revenue column.
gameStopRevenue.dropna(inplace=True)
gameStopRevenue = gameStopRevenue[gameStopRevenue['Revenue'] != ""]

#Print the five last rows
print(gameStopRevenue.tail())