#!python3
#emailer.py is a simple script for sending emails using smtplib

import smtplib

from_addr = 'pybitesblog@gmail.com'
to_addr = 'pybitesblog@gmail.com'

body = """New Releases and Sales on Steam
    
Click the links below to check them out!
   
"""

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)

smtp_server.ehlo()

smtp_server.starttls()

smtp_server.login(' pybitesblog@gmail.com ', ' <application id> ')

smtp_server.sendmail(from_addr, to_addr, body)

smtp_server.quit()

print('Email sent successfully')
