import requests
from bs4 import BeautifulSoup

url = "https://stackoverflow.com/questions"
respuesta = requests.get(url)
texto = respuesta.text
soup = BeautifulSoup(texto,"html.parser")

soup.select("")