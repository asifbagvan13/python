import matplotlib.pyplot as plt
import datetime
import pandas as pd
import yfinance as yf
#yahooo finance link : https://finance.yahoo.com/markets/stocks/most-active/ can find indian stocks aswell


    

def plot(ts,st, ed):
    data = yf.download(tickers= ts, start=st, end=ed)
    plt.figure(figsize=(10, 6))
    plt.plot(data['Close'], label= ts)
    plt.title(ts)
    plt.xlabel('date')
    plt.ylabel('price')
    plt.legend()
    plt.show()
    

st = input("enter start date in year YY-MM-DD: ")    
ed = input("enter end date in year YY-MM-DD: ")    
ts = input("enter ticker name according to yahoo finance: ")
plot(ts.upper(),st, ed)