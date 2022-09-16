# from email.message import _PayloadType
from site import execusercustomize
import requests
import secrets
from datetime import date, datetime

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_endpoint = "https://api.sheety.co/phill/myWebsite/emails"



GENDER = "male"
WEIGHT_KG = 66.7
HEIGHT_CM = 173.0
AGE = 59

headers = {
    "x-app-id":secrets.APP_ID,
    "x-app-key":secrets.API_KEY}

text = input("What exercise did you do? ")

parameters = {
 "query":text,
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE
}

response = requests.post(
    url=nutritionix_endpoint,
    json=parameters,
    headers=headers)
result = response.json()
print(result)


# To create a new row in your sheet, perform a POST request to the endpoint, with your row contents as a JSON payload in the request body.

# sheety_headers = {}

date = date.today()
time = datetime.now()
time_formatted = time.strftime("%H:%M")
exercise = result["exercises"][0]["name"]
duration = result["exercises"][0]["duration_min"]
calories = result["exercises"][0]["nf_calories"]

# print(f"Date: {date}\ntime: {time_formatted}\nexercise: {exercise}\ncalories: {calories}")

payload = {
    date,
    time,
    exercise,
    duration,
    calories
}

response = requests.post(sheety_endpoint,json=payload)
