from unittest import result


class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass

sheet_data = [{'city': 'Berlin', 'iataCode': '', 'lowestPrice': 42, 'id': 2}, {'city': 'Cape Town', 'iataCode': '', 'lowestPrice': 378, 'id': 3}, {'city': 'Istanbul', 'iataCode': '', 'lowestPrice': 95, 'id': 4}, {'city': 'Kuala Lumpur', 'iataCode': '', 'lowestPrice': 414, 'id': 5}, {'city': 'New York', 'iataCode': '', 'lowestPrice': 240, 'id': 6}, {'city': 'Paris', 'iataCode': '', 'lowestPrice': 54, 'id': 7}, {'city': 'San Francisco', 'iataCode': '', 'lowestPrice': 260, 'id': 8}, {'city': 'Sydney', 'iataCode': '', 'lowestPrice': 551, 'id': 9}, {'city': 'Tokyo', 'iataCode': '', 'lowestPrice': 485, 'id': 10}]


def process_cities(data):
    output_list = []
    for record in data:
        record = {k:"TESTING" for k,v in record.items() if v == ""}
        output_list.append(record)
    return output_list

print(process_cities(sheet_data))