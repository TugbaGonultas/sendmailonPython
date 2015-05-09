__author__ = 'tugba'



import smtplib
from_= 'tgbgonultas@gmail.com'
to_='denemepython@gmail.com'
mesaj="ben"
try:

    server=smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('tgbgonultas','yvwtuqmlcrdvzhsp')
    server.sendmail(from_,to_,mesaj)

finally:
    server.quit()



