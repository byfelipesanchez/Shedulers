import requests
import bs4
import gspread
from bs4 import BeautifulSoup
import datetime
import smtplib, ssl
from subprocess import call
import time


def request():
    r = requests.get('https://www.google.com/search?safe=active&client=firefox-b-d&sxsrf=ALeKk03rpVr9UF89A0Xo4p2mRaBrbSuJMg%3A1613780947389&ei=01cwYNOhF6PY5OUPpuu9-Aw&q=preco+do+euro+para+real&oq=preco+do+euro+para+real&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEMsBMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIGCAAQFhAeOgcIABBHELADULYOWIYXYNEYaAFwAngAgAHIAYgBlA2SAQYwLjEwLjGYAQCgAQGqAQdnd3Mtd2l6yAEIwAEB&sclient=gws-wiz&ved=0ahUKEwiT1_TAmvfuAhUjLLkGHaZ1D88Q4dUDCAw&uact=5')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse(soup):
        date = datetime.datetime.now()
        price = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name ,'price':price, }
        return total
    

def output(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request()
total = parse(data)
output(total)
print(total)