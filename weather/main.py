from dataclasses import dataclass
from email.contentmanager import raw_data_manager
import pandas as pd

with open("weather_data.csv") as file:
    raw_data = file.readlines()
    clean_data = []
    for e in raw_data:
        e = e.replace("\n","")
        clean_data.append(e)
    
print(clean_data[1:])