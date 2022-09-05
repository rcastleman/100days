import requests

response = requests.get(url = "http://api.open-notify.org/iss-now.json")
data  = response.json()
# print(data)

position = data['iss_position']['longitude']
# print(position)
iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])

print(f"ISS lat: {iss_latitude}")
print(f"ISS lng: {iss_longitude}")
