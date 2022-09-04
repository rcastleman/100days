from calendar import week
from multiprocessing import connection
import smtplib
import datetime as dt
import random
import pandas as pd

# TODO obtain current day of week
# TODO check to see if day of week = Target Day
# TODO open quotes.txt and get LIST of quotes
# TODO send email with random quote 

now = dt.datetime.now()
day = now.weekday()

day_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}

target_day = "Saturday"

def send_email():
    print("sending an email!")

if day == day_dict[target_day]:
    send_email()