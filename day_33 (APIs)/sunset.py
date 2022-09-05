import requests

MY_LAT = 40.753270
MY_LNG = -73.971660

parameters = {"lat":MY_LAT,
"lng": MY_LNG}

response = requests.get(url = "https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
# data  = response.json()
# print(data)
