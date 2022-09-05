from ast import FormattedValue
import requests
from datetime import datetime
from iss.py import iss_latitude,iss_longitude
from email_engine import send_email

MY_LAT = 40.753270
MY_LNG = -73.971660

parameters = {"lat":MY_LAT,
"lng": MY_LNG,"formatted":0}

response = requests.get(url = "https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data  = response.json()
#split out the TIME then the HOUR from the time
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(f"sunrise: {sunrise}")
print(f"sunset: {sunset}")
time_now = datetime.now()
print(f"local time: {time_now.hour}")

#is ISS within 5 degrees of current lat or long?

def is_overhead():
    pass

#send email saying "look up"
