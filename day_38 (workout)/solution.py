import requests
import secrets 

GENDER = "male"
WEIGHT_KG = 70.0
HEIGHT_CM = 168.0
AGE = 50

APP_ID = secrets.APP_ID
API_KEY = secrets.API_KEY

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

parameters = {
    "query": "ran 10 km",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()
print(result)