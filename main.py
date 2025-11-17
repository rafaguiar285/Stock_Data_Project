import yfinance as yf
import pandas as pd
import json



#Using the Ticker module we can create an object that will allow us to access functions to extract data.
apple = yf.Ticker("AAPL")


with open('apple.json') as json_file:
    apple_info = json.load(json_file)
    # Print the type of data variable    
    #print("Type:", type(apple_info))
print(apple_info)