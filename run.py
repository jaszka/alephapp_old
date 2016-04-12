# coding=utf-8
import urllib
import urllib2
import cookielib
import re
import smtplib
import sys

#Podaj login:
login = ''
#Podaj hasło:
pass = ''
#Podaj maila:
mail = ''

#katalog Aleph
url = 'http://katalog.biblioteka.wroc.pl/F'

#dane do wysłania
values = {
    'func': 'bor-hold',
    'adm_library': 'MBP50',
    'bor_id': login,
    'bor_verification': pass,
    'bor_library': 'MBP50'
    }
data = urllib.urlencode(values)

cookies = cookielib.CookieJar()
opener = urllib2.build_opener(
  urllib2.HTTPRedirectHandler(),
  urllib2.HTTPHandler(debuglevel=0),
  urllib2.HTTPSHandler(debuglevel=0),
  urllib2.HTTPCookieProcessor(cookies))

response = opener.open(url, data)
the_page = response.read()

#Czy zamówienie jest juz dostępne?
matches = re.findall('Zarezerwowany.+\d', the_page)

if len(matches) > 0:
    
    TO = mail
    SUBJECT = 'Twoja zamówiona książka czeka na odbiór'
    TEXT = 'Drogi Czytelniku,' \
           '\nTwoje zamówienie jest gotowe do odbioru.' \
           '\nStatus: %s.' \
           '\nWejdź na http://katalog.biblioteka.wroc.pl/F i sprawdź jeśli mi nie ufasz:P' %matches
    sender = 'mty.python@o2.pl'
    passw = 'xxxx'

    mail = smtplib.SMTP('poczta.o2.pl', 587)

    mail.ehlo()
    mail.starttls()
    mail.ehlo
    mail.login(sender, passw)

    BODY = '\r\n'.join([
        'To: %s' % TO,
        'From: %s' % sender,
        'Subject: %s' % SUBJECT,
        '',
        TEXT
    ])

    mail.sendmail(sender, [TO], BODY)
    mail.close()

else:
    sys.exit()
