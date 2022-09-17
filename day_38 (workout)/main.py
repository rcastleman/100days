import requests
import secrets
from datetime import date, datetime
import os
from dotenv import load_dotenv
load_dotenv()

# link to Google sheet 
#https://docs.google.com/spreadsheets/d/10lshz6OBryHn1apsJtU2BVXYkb8hO30nseEjtX_ehXQ/edit#gid=0

GENDER = "male"
WEIGHT_KG = 66.7
HEIGHT_CM = 173.0
AGE = 59

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheet_endpoint = "https://api.sheety.co/d1adb73803921977f6bd07bf9871e281/100DaysMyWorkouts/workouts"

text = input("What exercise did you do? ")

headers = {
    "x-app-id":secrets.APP_ID,
    "x-app-key":secrets.API_KEY}

parameters = {
 "query":text,
 "gender":GENDER,
 "weight_kg":WEIGHT_KG,
 "height_cm":HEIGHT_CM,
 "age":AGE
}

response = requests.post(
    url=exercise_endpoint,
    json=parameters,
    headers=headers)
result = response.json()
print(result)

# To create a new row in your sheet, perform a POST request to the endpoint, with your row contents as a JSON payload in the request body.

bearer_headers = {"Authorization": f"Bearer {secrets.TOKEN}"}

today_date = datetime.now().strftime("%m/%d/%Y")
now_time = datetime.now().strftime("%H:%M")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(sheet_endpoint, json=sheet_inputs,headers=bearer_headers)

    print(sheet_response.text)