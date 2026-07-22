import yfinance as yf
data = yf.download(tickers='GOOGL', period='2y', interval='1d')
# print(type(data))

import pandas as pd
data['SMA']=data['Close'].rolling(20).mean()
data['LMA']=data['Close'].rolling(50).mean()
#print(data.head(51))

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

profit_loss = []
prev_close_price = None
prev_decision = "Купуємо"
entry_dates = []
entry_prices = []
exit_dates = []
exit_prices = []

for i, row in data.iterrows():
    if prev_close_price is not None and prev_decision == "Купуємо":
        profit_loss.append(row["Close"] - prev_close_price)
    else:
        profit_loss.append(0)

    if row['Рішення'] == 'Купуємо' and prev_decision != 'Купуємо':
        entry_dates.append(i)
        entry_prices.append(row['Close'])
    elif row['Рішення'] == 'Продаємо' and prev_decision == 'Купуємо':
        exit_dates.append(i)
        exit_prices.append(row['Close'])

    prev_close_price = row["Close"]
    prev_decision = row["Рішення"]

data["profit_loss"] = profit_loss
print(f"Загальний прибуток/збиток: {sum(profit_loss):.2f}")