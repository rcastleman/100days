from calendar import week
from multiprocessing import connection
import smtplib
import datetime as dt
import random
from socket import TCP_NODELAY
from email_via_python import send_email,hour,minute
import csv
import pandas as pd

# TODO Check if today matches a birthday in the birthdays.csv
# HINT 1: Create a tuple from today's month and day using datetime. e.g.
# today = (today_month, today_day)
# HINT 2: Use pandas to read the birthdays.csv
# HINT 3: Use dictionary comprehension to create a dictionary from birthday.csv that is formated like this:
# birthdays_dict = {
#     (birthday_month, birthday_day): data_row
# }
#Dictionary comprehension template for pandas DataFrame looks like this:
# new_dict = {new_key: new_value for (index, data_row) in data.iterrows()}
#e.g. if the birthdays.csv looked like this:
# name,email,year,month,day
# Angela,angela@email.com,1995,12,24
#Then the birthdays_dict should look like this:
# birthdays_dict = {
#     (12, 24): Angela,angela@email.com,1995,12,24
# }
#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# TODO If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT 1: Think about the relative file path to open each letter. 
# HINT 2: Use the random module to get a number between 1-3 to pick a randome letter.
# HINT 3: Use the replace() method to replace [NAME] with the actual name. https://www.w3schools.com/python/ref_string_replace.asp

# TODO Send the letter generated in step 3 to that person's email address.
# HINT 1: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
# HINT 2: Remember to call .starttls()
# HINT 3: Remember to login to your email service with email/password. Make sure your security setting is set to allow less secure apps.
# HINT 4: The message should have the Subject: Happy Birthday then after \n\n The Message Body.

now = dt.datetime.now()
day = now.day
month = now.month
today = (month,day)
# print(f"Month: {month} Day: {day}")
# print(target)

data = pd.read_csv("birthdays.csv")
new_dict = {data_row["month"]:data_row["day"] for (index, data_row) in data.iterrows()}



def send_card():
    random_card = random.choice(["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"])
    return random_card
    # print(random_card)

def test_isBirthday(month,day):
    # if data.loc[data['month']] == month and data.loc[data['day']] == day:
    if data.loc[(df['month'] == month) & (data['day'] == day)]:
        # send_card()
        print(f"Sending a card to {data.loc[data['name']]}")

# test_isBirthday(month,day)


