from operator import truediv
from xmlrpc.client import FastMarshaller
import requests
import os
from twilio.rest import Client

TWILIO_ACCOUNT_SID = "ACdfb774e0c104504eb9da3842343bbff7"
TWILIO_AUTH_TOKEN = "a89fe5de4e42c89804e406aeb27f7807"
TWILIO_PHONE = "+19855895764"
TARGET_PHONE = "+14348254811"

# https://home.openweathermap.org/api_keys

API_KEY = "8f21e2683deb718640c8241bb5e63746"
one_call_API = "52b9cd8ce0541eaea09c5c01dbbf4609"
four_days_API = "b299b8818c68292f1fa725c78a75a35e"
NYC_LAT = 40.753270
NYC_LNG = -73.971660
TEST_LAT = 44.866623
TEST_LNG = 13.849579
COUNT = 8

five_day = f"https://api.openweathermap.org/data/2.5/forecast?lat={TEST_LAT}&lon={TEST_LNG}&appid={API_KEY}&units=imperial&cnt={COUNT}"

# current_wx = f"https://api.openweathermap.org/data/2.5/weather?lat={NYC_LAT}&lon={NYC_LNG}&appid={API_KEY}&units=imperial"

# one_call_wx = f"https://api.openweathermap.org/data/3.0/onecall?lat={NYC_LAT}&lon={NYC_LNG}&appid={API_KEY}&units=imperial"

# four_days = f"https://pro.openweathermap.org/data/2.5/forecast/hourly?lat={NYC_LAT}&lon={NYC_LNG}&appid={four_days_API}"


response = requests.get(url = five_day)
data  = response.json()

condition_list = []
for element in range(COUNT):
    id = data["list"][element]["weather"][0]["id"]
    condition_list.append(id)

# print(condition_list)
# for element in range(3):
#     id = data["list"][element]["weather"][0]["id"]
#     temp = data["list"][element]["main"]["temp"]
#     print(f"The weather condition ID is {id} and the temp is {temp}")

will_rain = False

for e in condition_list:
    if e <=700:
        will_rain = True

if will_rain:
    account_sid = TWILIO_ACCOUNT_SID
    auth_token = TWILIO_AUTH_TOKEN
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
            body="Bring an umbrella!",
            from_=TWILIO_PHONE,
            to=TARGET_PHONE
        )

    print(message.status)
