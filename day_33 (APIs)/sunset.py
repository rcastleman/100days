from ast import FormattedValue
import requests
from datetime import datetime
from email_engine import send_email

#----------- ISS API --------------- #
response = requests.get(url = "http://api.open-notify.org/iss-now.json")
data  = response.json()

position = data['iss_position']['longitude']
iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

print(f"ISS lat: {iss_latitude}")
print(f"ISS lng: {iss_longitude}")

#----------- Sunrise / Sunset  API --------------- #

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

#if the ISS within 5 degrees of current lat or long
#send email saying "look up"

subject = "ISS overhead!"
body = "The ISS is passing overhead.  Go outside and take a look!"

def is_overhead():
    if abs(iss_latitude - MY_LAT) < 5 | abs(iss_longitude - MY_LNG) < 5:
        send_email(subject=subject,body=body)
