import os
from secrets import SID
from twilio.rest import Client
import secrets

TWILIO_PHONE = "+19855895764"
TARGET_PHONE = "+14348254811"

account_sid = secrets.SID
auth_token = secrets.AUTH

# Print your credentials and check they are correct 
# print(account_sid)
# print(auth_token)

# temporarily, hardcode the credentials that you got form your console
temp_account_sid = secrets.SID
temp_auth_token = secrets.AUTH

print(f"Temp SID: {temp_account_sid}")
print(f"Temp AUTH: {temp_auth_token}")

client = Client(temp_account_sid, temp_auth_token)


message = client.messages.create(
                              body='Hi there',
                              from_=TWILIO_PHONE,
                              to=TARGET_PHONE
                          )

print(message.sid)