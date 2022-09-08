import os
from twilio.rest import Client

# TWILIO_ACCOUNT_SID = "ACdfb774e0c104504eb9da3842343bbff7"
# TWILIO_AUTH_TOKEN = "a89fe5de4e42c89804e406aeb27f7807"
TWILIO_PHONE = "+19855895764"
TARGET_PHONE = "+14348254811"

account_sid = "ACdfb774e0c104504eb9da3842343bbff7"
auth_token = "a89fe5de4e42c89804e406aeb27f7807"
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test text from Twilio",
                     from_= TWILIO_PHONE,
                     to= TARGET_PHONE
                 )

print(message.sid)