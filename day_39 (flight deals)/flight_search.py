import code
import os
import requests
from dotenv import load_dotenv
load_dotenv()

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
KIWI_TOKEN = os.environ.get("KWIW_USERID")
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")

class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{KIWI_ENDPOINT}/locations/query"
        headers = {"apikey": KIWI_API_KEY}
        query = {"term": city_name, "location_types": "city"}
        response = requests.get(url=location_endpoint, headers=headers, params=query)
        # print(response.json())
        results = response.json()["locations"]
        code = results[0]["code"]
        return code