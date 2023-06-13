# https://myaccount.google.com/u/1/lesssecureapps

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib 

path = Path("modulos-nativos/berserk-tatto-ideas.jpg")
mime_image =  MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "Denji"
mensaje["to"] = "ndarkslayer13@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo = MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()

    smtp.login("denji@chainsawman.com", "ilovemakima")
    smtp.send_message(mensaje)