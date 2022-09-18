#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

# TODO Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with International Air Transport Association (IATA) codes for each city. Most of the cities in the sheet include multiple airports, you want the city code (not the airport code see here).




# TODO Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all the cities in the Google Sheet.

# TODO If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number with the Twilio API.

# TODO The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates. e.g.


from math import lgamma
import requests
import os
from dotenv import load_dotenv
load_dotenv()
from pprint import pprint
