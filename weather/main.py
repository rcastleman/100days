import csv

# with open("weather_data.csv") as file:
#     raw_data = file.readlines()
#     clean_data = []
#     for e in raw_data:
#         e = e.replace("\n","")
#         clean_data.append(e)
# print(clean_data[1:])


with open("weather_data.csv") as data_file:
    #creates a CSV data object
    data = csv.reader(data_file)
    for row in data:
        print(row)
