import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    pass

sheet_endpoint = "https://api.sheety.co/d1adb73803921977f6bd07bf9871e281/flightDealsRc/prices"

response = requests.get(sheet_endpoint)
response.raise_for_status()
data = response.json()
sheet_data = data["prices"]
print(sheet_data)