#
import requests
import bs4
import gspread
from bs4 import BeautifulSoup
import datetime
import smtplib, ssl
from subprocess import call
import time


def send_email():
    port = 465

    sender, password = '######', '######'

    recieve = '2018.felipe.sanchez@gmail.com'

    message = '''
    Subject: Testing Python Email

    Message via Python!

    Felipe

    '''

    context = ssl.create_default_context()

    print("starting to send")
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)as server:
        server.login(sender, password)
        server.sendmail(sender, recieve, message)

    print("email sent!")

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
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request()
total = parse(data)
output(total)
print(total)


def request1():
    r = requests.get('https://finance.yahoo.com/quote/TRPL4.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse1(soup):
        date = datetime.datetime.now()
        name1 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price1 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name1 ,'price':price1, }
        return total


def output1(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request1()
total = parse1(data)
output1(total)
print(total)
 

def request2():
    r = requests.get('https://br.financas.yahoo.com/quote/GGBR4.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse2(soup):
        date = datetime.datetime.now()
        name2 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price2 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name2 ,'price':price2, }
        return total


def output2(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request2()
total = parse2(data)
output2(total)
print(total)

def request3():
    r = requests.get('https://finance.yahoo.com/quote/EMBR3.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse3(soup):
        date = datetime.datetime.now()
        name3 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price3 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name3 ,'price':price3, }
        return total


def output3(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request3()
total = parse3(data)
output3(total)
print(total)


def request4():
    r = requests.get('https://finance.yahoo.com/quote/vvar3.sa/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse4(soup):
        date = datetime.datetime.now()
        name4 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price4 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name4 ,'price':price4, }
        return total


def output4(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request4()
total = parse4(data)
output4(total)
print(total)


def request5():
    r = requests.get('https://br.financas.yahoo.com/quote/petr4.sa/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse5(soup):
        date = datetime.datetime.now()
        name5 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price5 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name5 ,'price':price5, }
        return total


def output5(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request5()
total = parse5(data)
output5(total)
print(total)

def request6():
    r = requests.get('https://finance.yahoo.com/quote/USIM3.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse6(soup):
        date = datetime.datetime.now()
        name6 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price6 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name6 ,'price':price6, }
        return total


def output6(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request6()
total = parse6(data)
output6(total)
print(total)

def request7():
    r = requests.get('https://finance.yahoo.com/quote/CSNA3.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse7(soup):
        date = datetime.datetime.now()
        name7 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price7 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name7 ,'price':price7, }
        return total


def output7(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request7()
total = parse7(data)
output7(total)
print(total)

def request8():
    r = requests.get('https://finance.yahoo.com/quote/ITSA4.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse8(soup):
        date = datetime.datetime.now()
        name8 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price8 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name8 ,'price':price8, }
        return total

def output8(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request8()
total = parse8(data)
output8(total)
print(total)


def request9():
    r = requests.get('https://br.financas.yahoo.com/quote/BBAS3.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse9(soup):
        date = datetime.datetime.now()
        name9 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price9 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name9 ,'price':price9, }
        return total

def output9(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request9()
total = parse9(data)
output9(total)
print(total)

def request10():
    r = requests.get('https://br.financas.yahoo.com/quote/VALE3.SA/')
    soup = bs4.BeautifulSoup(r.text, 'lxml')
    return soup


def parse10(soup):
        date = datetime.datetime.now()
        name10 = soup.find('h1', class_ = 'D(ib) Fz(18px)').text.strip()
        price10 = soup.find_all('div', {'class':"My(6px) Pos(r) smartphone_Mt(6px)"})[0].find('span').text
        total = {'date':date, 'name': name10 ,'price':price10, }
        return total

def output10(total):
        gc = gspread.service_account(filename='creds.json')
        sh = gc.open('Stocks').sheet1
        sh.append_row([str(total['date']), str(total['name']), str(total['price'])])

data = request10()
total = parse10(data)
output10(total)
print(total)

##

lines = ("-","-", "-")
gc = gspread.service_account(filename='creds.json')
sh = gc.open('Stocks').sheet1
sh.append_row(lines)
print(lines)
 
