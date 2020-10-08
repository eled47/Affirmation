# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'AC6f2e1e50d879fdf510e86edcc16c9f3c'
auth_token = 'f5f0629ea6c74c891652a072e5d79f83'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+16087955604',
                     to='+14235809433'
                 )

print(message.sid)
