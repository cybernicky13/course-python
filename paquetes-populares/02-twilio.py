import os
from twilio.rest import Client

sid = os.environ.get("TWILIO_SID")
token = os.environ.get("TWILIO_TOKEN")
numero = os.environ.get("TWILIO_N")

cliente = Client(sid,token)
mensaje = cliente.messages.create(
    body="Hola mundos!",
    from_=numero,
    to="+133366678077"
)