import requests

sheety_endpoint = "https://api.sheety.co/d1adb73803921977f6bd07bf9871e281/flightDealsRc/prices"

class DataManager:

    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=sheety_endpoint)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data
            )
            print(response.text)
