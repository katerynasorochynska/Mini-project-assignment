import yfinance as yf
data = yf.download(tickers='GOOGL', period='2y', interval='1d')
# print(type(data))

import pandas as pd
data['SMA']=data['Close'].rolling(20).mean()
data['LMA']=data['Close'].rolling(50).mean()
print(data.head(51))

data.columns = data.columns.get_level_values(0)
decisions = []

for i, row in data.iterrows():
    if pd.isna(row["SMA"]) or pd.isna(row["LMA"]):
        decisions.append('Утримуємось')
    elif row['SMA'] > row['LMA']:
        decisions.append('Купуємо')
    else:
        decisions.append('Продаємо')

data['Рішення'] = decisions
print(data)
