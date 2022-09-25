import os
from datetime import *
import requests
from dotenv import load_dotenv

from flight_data import FlightData
load_dotenv()

KIWI_ENDPOINT = "https://tequila-api.kiwi.com"
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{KIWI_ENDPOINT}/locations/query"
        headers = {"apikey": KIWI_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        results = response.json()["locations"]
        code = results[0]["code"]
        return code

    def check_flights(self,origin_city_code,destination_city_code,from_time,to_time):
        headers = {"apikey": KIWI_API_KEY}
        query = {
            "fly_from":origin_city_code,
            "fly_to":destination_city_code,
            "date_from":from_time.strftime("%d/%m/%Y"),
            "date_to":to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from":7,
            "nights_in_dst_to":28,
            "flight_type":"round",
            "curr":"GBP"
            }
        
        response = requests.get(
            url=f"{KIWI_ENDPOINT}/v2/search",
            headers=headers,
            params=query
        )

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {destination_city_code}.")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0])

        print(f"{flight_data.destination_city}: GBP{flight_data.price}")
        return flight_data

# https://api.tequila.kiwi.com/v2/search?fly_from=LON&fly_to=BER&date_from=10%2F1%2F2022&date_to=11%2F1%2F22&nights_in_dst_from=5&nights_in_dst_to=7&max_fly_duration=5&flight_type=round&one_for_city=0&one_per_date=0&adults=1&children=0&selected_cabins=F&mix_with_cabins=M&adult_hold_bag=0&adult_hand_bag=0&child_hold_bag=0&child_hand_bag=0&only_working_days=false&only_weekends=false&partner_market=us&max_stopovers=2&max_sector_stopovers=2&vehicle_type=aircraft&limit=500

# The next step is to search for the flight prices from London (LON) to all the destinations in the Google Sheet. In this project, we're looking only for direct flights, that leave anytime between tomorrow and in 6 months (6x30days) time. We're also looking for round trips that return between 7 and 28 days in length. The currency of the price we get back should be in GBP.