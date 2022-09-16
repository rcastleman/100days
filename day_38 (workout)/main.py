import requests
import secrets

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

# query = input("What exercise did you do?")

headers = {
    "x_app_id":secrets.APP_ID,
    "x_app_key":secrets.API_KEY,
    "x-remote-user-id":"0"}

parameters = {
 "query":"ran 3 miles",
 "gender":"female",
 "weight_kg":72.5,
 "height_cm":167.64,
 "age":30
}

response = requests.post(
    url=nutritionix_endpoint,
    params=parameters,
    headers=headers)
print(response.text)
