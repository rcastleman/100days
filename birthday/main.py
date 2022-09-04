from calendar import week
from multiprocessing import connection
import smtplib
import datetime as dt
import random
from socket import TCP_NODELAY
from email_via_python import send_email
import csv
import pandas as pd

now = dt.datetime.now()
day = now.day
month = now.month
today = (month,day)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"],data_row["day"]):data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        new = contents.replace('[NAME]',birthday_person['name'])
    send_email(new)

