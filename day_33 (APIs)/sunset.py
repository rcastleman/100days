from ast import FormattedValue
from pickle import TRUE
import requests
from datetime import datetime
from email_engine import send_email
import time

MY_LAT = 40.753270
MY_LNG = -73.971660

# MY_LAT = 10.0
# MY_LNG = -59.0

#------------------- ISS API -------------------- #
response = requests.get(url = "http://api.open-notify.org/iss-now.json")
data  = response.json()

position = data['iss_position']['longitude']
iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

print(f"ISS lat: {iss_latitude}")
print(f"ISS lng: {iss_longitude}")
print(f"My Lat: {MY_LAT}")
print(f"My Lng: {MY_LNG}")

#------------- Sunrise / Sunset  API -------------- #

def is_night(): 
    parameters = {"lat":MY_LAT,
    "lng": MY_LNG,
    "formatted":0}

    response = requests.get(url = "https://api.sunrise-sunset.org/json",params=parameters)
    response.raise_for_status()
    data  = response.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    print(f"sunrise: {sunrise}")
    print(f"sunset: {sunset}")
    print(f"time now: {time_now}")

    if time_now >= sunset or time_now <= sunrise:
        return True

#-------------- ISS PROXIMITY TEST --------------------#

def is_overhead():
    if abs(iss_latitude - MY_LAT) < 5 and abs(iss_longitude - MY_LNG) < 5:
        return True

#--------------------- SEND EMAIL --------------------#

while True:
    time.sleep(60)
    if is_night and is_overhead:
        subject = "ISS overhead!"
        body = "The ISS is passing overhead.  Go outside and take a look!"
        send_email(subject=subject,body=body)
