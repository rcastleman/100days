import requests
import secrets


nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

query = input("What exercise did you do?")

headers = {
    "x_app_id":secrets.APP_ID,
    "x_app_key":secrets.APP_KEY,
    "x-remote-user-id":0}

parameters = {
    "x-user-jwt":x_app_id,
    "query": query
    }

response = requests.post(url=nutritionix_endpoint,params=parameters)
print(response.text)
