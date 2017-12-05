import os

from twilio.rest import Client

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_phone = os.getenv('TWILIO_PHONE_NUM')
phone_num = os.getenv('MY_PHONE_NUM')

client = Client(account_sid, auth_token)

message = client.messages.create(
    from_=twilio_phone,
    to=phone_num,
    body="Python Text",
)

print(message.sid)
