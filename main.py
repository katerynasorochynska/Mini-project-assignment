import yfinance as yf
data = yf.download(tickers='GOOGL', period='2y', interval='1d')
# print(type(data))

import pandas as pd
data['SMA']=data['Close'].rolling(20).mean()
data['LMA']=data['Close'].rolling(50).mean()
print(data.head(51))


