import requests
from bs4 import BeautifulSoup

URL = 'https://www.google.com/search?client=firefox-b-d&q=petr4f+acao'

headers = {"Users-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

print(soup.prettify())

title = soup.find('div', class_ = 'D(ib) Fz(18px)').text

print(title.strip())