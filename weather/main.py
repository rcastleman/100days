import csv
import pandas as pd
from dataclasses import dataclass

# with open("weather_data.csv") as file:
#     raw_data = file.readlines()
#     clean_data = []
#     for e in raw_data:
#         e = e.replace("\n","")
#         clean_data.append(e)
# print(clean_data[1:])


with open ("weather_data.csv") as data_file:
    data = csv.reader(data_file)  
# print(data)
#create list of temperatures where values are integers
    # temperatures = []
    # for row in data:
    #     if row[1] != "temp":
    #         temperatures.append(int(row[1]))
    # print(temperatures)

data = pd.read_csv("weather_data.csv")
print(data['temp'])