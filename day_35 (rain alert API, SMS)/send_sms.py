import os
from twilio.rest import Client

# TWILIO_ACCOUNT_SID = ""
# TWILIO_AUTH_TOKEN = ""
TWILIO_PHONE = "+19855895764"
TARGET_PHONE = "+14348254811"

account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Test text from Twilio",
                     from_= TWILIO_PHONE,
                     to= TARGET_PHONE
                 )

print(message.sid)