
import requests
import bs4
import gspread
from bs4 import BeautifulSoup
import datetime
import smtplib



#
# sh.append_row('first', 'second')


def request():
    r = requests.get('https://br.financas.yahoo.com/quote/KLBN4.SA?p=KLBN4.SA&.tsrc=fin-srch')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse(soup):
    date = datetime.datetime.now()
    name = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
    price = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
    total = {'date':date, 'name': name ,'price':price}
    return total

def output(total):
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open('webscraper').sheet1
    sh.append_row([str(total['date']), str(total['name']), str(total['price'])])


data = request()
total = parse(data)
output(total)
# print(total)


# sender_email = "2018.felipe.sanchez@gmail.com"
# rec_email = "2018.felipe.sanchez@gmail.com"
# password = input("enter password")
# message = "test"
#
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(sender_email, password)
# server.sendmail(sender_email, rec_email, message)
# print("email sent", rec_email)

#TODO: webscraping of other stocks and sending email when stock reaches a certain price

# while True:
#     print('the current price is: ' + str(parsePrice()))