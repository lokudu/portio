from twilio.rest import Client

account_sid = 'AC8dd21018b8594cbba9a7433901978873'
auth_token = '42072161b5a232d790e7a3f883b97e9e'
client = Client(account_sid, auth_token)

message = client.messages.create(
    messaging_service_sid='MG39e7260215ab4ba7cbdc38079f29b8c0',
  body='How are you doing James, hope your presentation went well yesterday. Just wising you success',
  to='+211925507769'
)

print(message.sid)