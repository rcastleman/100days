import requests
import secrets

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

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