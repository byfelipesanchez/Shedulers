
import requests
import bs4
from bs4 import BeautifulSoup
import gspread

gc = gspread.service_account(filename='creds.json')



sh = gc.open('webscraper').sheet1

sh.append_row('first', 'second')
# def parsePrice():
#     r = requests.get('https://br.financas.yahoo.com/quote/KLBN4.SA?p=KLBN4.SA&.tsrc=fin-srch')
#     soup = bs4.BeautifulSoup(r.text, 'lxml')
#     price = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
#     return price
#
# while True:
#     print('the current price is: ' + str(parsePrice()))