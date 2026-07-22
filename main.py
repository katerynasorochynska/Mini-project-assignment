import yfinance as yf
data = yf.download(tickers='GOOGL', period='2d', interval='1d')
print(data.head())
# print(type(data))
