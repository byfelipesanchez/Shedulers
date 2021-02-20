#!/usr/bin/env python
# coding: utf-8

import datetime
import locale
from urllib.request import urlopen
from bs4 import BeautifulSoup

import smtplib
from email.mime.multipart import MIMEMultipart

web_charset = "utf-8"
mail_charset = "ISO-2022-JP"

targeturl = 'https://br.financas.yahoo.com/quote/KLBN4.SA?p=KLBN4.SA&.tsrc=fin-srch' # Target URL for scraping
targetclass = ('h1', {'class':'D(ib) Fz(18px)'}) # Target element for scraping

from_address = "senderemailfs@gmail.com" # Sender address (Gmail address)
from_password = "FelipeSanchezsSenderEmail" # Sender server password (Gmail password)
to_address   = "2018.felipe.sanchez@gmail.com" # Recipient address

statusOK = u"Found / "
statusNG = u"Not Found"

def scraping(url):
	try:
		html = urllib2.urlopen(url).read()
		soup = BeautifulSoup(html)
		target = soup.find(targetclass).renderContents()
		if len(target) == 0:
			return statusNG
		else:
			return statusOK + target.decode(web_charset)
	except:
		return statusNG

def create_message(from_addr, to_addr, subject, body, encoding):
	msg = MIMEText(body, 'plain', encoding)
	msg['From'] = from_addr
	msg['To'] = to_addr
	msg['Subject'] = Header(subject, encoding)
	msg["Date"] = formatdate(localtime=True)
	return msg

def sendmail(subject, text):
	msg = create_message(from_address, to_address, subject, text, mail_charset)
	s = smtplib.SMTP('smtp.gmail.com', 587)
	s.ehlo()
	s.starttls()
	s.ehlo()
	s.login(from_address, from_password)
	s.sendmail(from_address, to_address, msg.as_string())
	s.close()

if __name__ == "__main__":
	d = datetime.datetime.today()
	time = d.strftime("%Y-%m-%d %H:%M:%S")
	mailsubject = u"Page Scraping // " + time
	mailmessage = scraping(targeturl)
	sendmail(mailsubject, mailmessage)