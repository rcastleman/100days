from pickle import FALSE, TRUE
from selectors import SelectorKey
from subprocess import call
import secrets

from datetime import date, timedelta

import requests
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient


#-------------- global variables ---------------------#

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla"

#trigger (%) above which news is retrieved
TRIGGER = 5

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

TWILIO_PHONE = "+19855895764"
TARGET_PHONE = "+14348254811"

#----------------- hints -----------------------------#

# Use https://www.alphavantage.co/documentation/#daily

#  https://newsapi.org/ 
# STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

# demo API call
# https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo

#-------------------- API parameters --------------------#

account_sid = secrets.SID
auth_token = secrets.AUTH

stock_parameters = {"function": "TIME_SERIES_DAILY",
"symbol":"TSLA",
"apikey":secrets.ALPHA_KEY}

news_parameters = {"q":COMPANY_NAME,
"apiKey":secrets.NEWS_KEY,
"searchIn":"title",
"from":"2022-09-10",
"to":date.today(),
}

#-------------------- helper functions --------------------#

def send_notification():

    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Hi there',
        from_=TWILIO_PHONE,
        to=TARGET_PHONE
                          )
    print(message.sid)

#-------------------- main loop ----------------------------#

# today_date = date.today()
# yesterday_date = today_date - timedelta(days = 1)

# dummy hard-coded data for testing
today_date = "2022-09-09"
yesterday_date = "2022-09-08"
today = 150
yesterday = 125

# notify = FALSE

# while not notify:

# response = requests.get(STOCK_ENDPOINT,params=stock_parameters)
# response.raise_for_status()
# data = response.json()
# today = data["Time Series (Daily)"][today_date]["4. close"]
# yesterday = data["Time Series (Daily)"][yesterday_date]["4. close"]
ratio = 100*(abs(float(today)/float(yesterday))-1)
limit = 3
if ratio > TRIGGER:
    news_response = requests.get(NEWS_ENDPOINT,params=news_parameters)
    news_response.raise_for_status()
    news_data = news_response.json()
    articles = news_data["articles"][0:limit]
    # formatted_articles = [f"Headline: {article['title']}.\nDescription: {article['description']}" for article in articles]
    formatted_articles = [f"Headline: {article['title']}." for article in articles]
    # print(formatted_articles)

    account_sid = secrets.SID
    auth_token = secrets.AUTH
    client = Client(account_sid, auth_token)

    for article in formatted_articles:

        message = client.messages \
            .create(
                body=article,
                from_=TWILIO_PHONE,
                to=TARGET_PHONE
            )
    print(message.status)
