import requests
from bs4 import BeautifulSoup

req = requests.get("https://ya.ru")

page = BeautifulSoup(req.text)
print(page.prettify())
