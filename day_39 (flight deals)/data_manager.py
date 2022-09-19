import requests

sheety_endpoint = "https://api.sheety.co/d1adb73803921977f6bd07bf9871e281/flightDealsRc/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(sheet_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

