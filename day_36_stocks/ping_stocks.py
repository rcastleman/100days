from secrets import ALPHA_KEY
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"

parameters = {"function": "TIME_SERIES_DAILY",
"symbol":"TSLA",
"apikey":ALPHA_KEY}

today_date = "2022-09-09"
yesterday_date = "2022-09-08"

response = requests.get(STOCK_ENDPOINT,params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

today = data["Time Series (Daily)"][today_date]["4. close"]
yesterday = data["Time Series (Daily)"][yesterday_date]["4. close"]

print (today,yesterday)
