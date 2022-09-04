from calendar import week
from multiprocessing import connection
import smtplib
import datetime as dt
import random
from email_via_python import send_email,hour,minute


# DONE obtain current day of week
# DONE check to see if day of week = Target Day
# DONE open quotes.txt and get LIST of quotes
# TODO send email with random quote 

now = dt.datetime.now()
day = now.weekday()
day_dict = {'Monday': 0, 'Tuesday': 1, 'Wednesday': 2, 'Thursday': 3, 'Friday': 4, 'Saturday': 5, 'Sunday': 6}
target_day = "Saturday"

with open("quotes.txt") as file:
    raw = file.read()
    quote_list = raw.splitlines()
    # print(quote_list)

def send_quote():
    random_quote = random.choice(quote_list)
    send_email(f"Subject:Motivational Quote {hour}:{minute} \n\n{random_quote}")

if day == day_dict[target_day]:
    send_quote()
