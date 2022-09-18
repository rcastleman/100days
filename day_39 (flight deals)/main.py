#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from math import lgamma
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from pprint import pprint


#------------------ KIWI API CALL -------------------------#

KIWI_ENDPOINT = "https://api.tequila.kiwi.com/v2/search"

from_city = "LGA"
to_city = "MIA"
depart_date = "29/10/2022"
return_date = "07/11/2022"

kiwi_params = {
    "fly_from":from_city,
    "fly_to": to_city,
    "dateFrom": depart_date,
    "dateTo": return_date,
    }

# old_sheet_data = "[{'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 2}, {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 3}, {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 4}, {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 5}, {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 6}, {'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 7}, {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 8}, {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 9}, {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 10}]"

sheet_data = [{'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 2}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 3}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 4}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 5}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 6}, {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 7}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 8}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 9}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 10}]


#--------------------- SHEETLY API CALL ----------------------#

sheet_endpoint = "https://api.sheety.co/d1adb73803921977f6bd07bf9871e281/flightDealsRc/prices"

# response = requests.get(sheet_endpoint)
# response.raise_for_status()
# data = response.json()
# sheet_data = data["prices"]
# print(sheet_data)

# with open('sheet_data', 'w') as f:
#     f.write(str(sheet_data))