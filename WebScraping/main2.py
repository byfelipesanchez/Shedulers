
import requests
import bs4
import gspread
from bs4 import BeautifulSoup
import datetime
import smtplib, ssl
from subprocess import call


# def send_email():
#     port = 465

#     sender, password = 'senderemailfs@gmail.com', 'FelipeSanchezsSenderEmail'

#     recieve = '2018.felipe.sanchez@gmail.com'

#     message = '''\
#     Subject: Testing Python Email

#     Message via Python!

#     Felipe

#     '''

#     context = ssl.create_default_context()

#     print("starting to send")
#     with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)as server:
#         server.login(sender, password)
#         server.sendmail(sender, recieve, message)

#     print("email sent!")

def request():
    r = requests.get('https://finance.yahoo.com/quote/TRPL4.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse(soup):
        date = datetime.datetime.now()
        name1 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name1 ,'price':price, }
        return total


def output(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request()
total = parse(data)
output(total)
print(total)





