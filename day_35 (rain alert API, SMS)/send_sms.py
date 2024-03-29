import os
from secrets import SID
from twilio.rest import Client
import secrets

TWILIO_PHONE = "+19855895764"
TARGET_PHONE = "+14348254811"

account_sid = secrets.SID
auth_token = secrets.AUTH

# account_sid = secrets.TEST_SID
# auth_token = secrets.TEST_AUTH

client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test text from Twilio",
                     from_= TWILIO_PHONE,
                     to= TARGET_PHONE
                 )

print(message.sid)
