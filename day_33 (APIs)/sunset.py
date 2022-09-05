from ast import FormattedValue
import requests
from datetime import datetime

MY_LAT = 40.753270
MY_LNG = -73.971660

parameters = {"lat":MY_LAT,
"lng": MY_LNG,"formatted":0}

response = requests.get(url = "https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data  = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

#split out the TIME then the HOUR from the time
print(sunrise.split("T")[1].split(":")[0])

# time_now = datetime.now()
# print(time_now)