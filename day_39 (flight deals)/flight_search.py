from codecs import code_page_decode
from unittest import result
import os
from dotenv import load_dotenv
load_dotenv()

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"
KIWI_TOKEN = os.environ.get("KWIW_USERID")
KIWI_API_KEY = os.environ.get("KIWI_API_KEY")

class FlightSearch:

    def get_destination_code(self,city_name):
        code = "TESTING"
        return code

# from_city = "LGA"
# to_city = "MIA"
# depart_date = "29/10/2022"
# return_date = "07/11/2022"

# kiwi_params = {
#     "fly_from":from_city,
#     "fly_to": to_city,
#     "dateFrom": depart_date,
#     "dateTo": return_date,
#     }

# sheet_data = [{'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 2}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 3}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 4}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 5}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 6}, {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 7}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 8}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 9}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 10}]
