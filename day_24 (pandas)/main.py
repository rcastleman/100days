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
# print(data)

data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# print(temp_list)
# average = sum(temp_list)/len(temp_list)
# print(average)
# max = data["temp"].max()

# print(data.day)

def convert_CtoF(temp):
    return temp * 9/5 + 32

monday = data[data.day == "Monday"]
monday_temp = monday.temp
# print(convert_CtoF(monday_temp))

# print(convert_CtoF(data.temp == monday))

# print(monday.condition)

# print(data[data.temp == max])

# create a dataframe from scratch

data_dict = {
    "students" : ["Amy","James","Angela"],
    "scores" : [76,56,65]
}

new =pd.DataFrame(data_dict)
# print(new)

new.to_csv("new_data.csv")

