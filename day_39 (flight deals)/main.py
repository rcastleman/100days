from datetime import *
from data_manager import DataManager
data_manager = DataManager()
sheet_data = data_manager.get_destination_data()

if sheet_data[0]["iataCode"] == "":
    from flight_search import FlightSearch
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    print(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

origin_city = "LON"
start_trip = date.today() + timedelta(days=1)
end_trip = start_trip + timedelta(days = 180)

for destination in sheet_data():
    flight = flight_search.check_flights(
        origin_city,
        destination["iataCode"],
        from_time = start_trip,
        to_time = end_trip
    )

