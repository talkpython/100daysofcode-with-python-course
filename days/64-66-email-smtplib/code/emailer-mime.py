#!python3
#emailer.py is a simple script for sending emails using smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from_addr = 'pybitesblog@gmail.com'
to_addr = 'pybitesblog@gmail.com'
bcc = ['pybitesblog@gmail.com', 'myemail@gmail.com', 'email@gmail.com']

msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = 'New Releases and Sales on Steam'

body = """New Releases and Sales on Steam
    
Click the links below to check them out!
   
"""

msg.attach(MIMEText(body, 'plain'))

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login(' pybitesblog@gmail.com ', ' <application id> ')

text = msg.as_string()

smtp_server.sendmail(from_addr, [to_addr] + bcc, text)

smtp_server.quit()

print('Email sent successfully')
