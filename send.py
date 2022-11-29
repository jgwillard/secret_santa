#!/usr/bin/env python3

import smtplib
import sys
import os

from email.message import EmailMessage

textfile  = sys.argv[1]

user = os.environ.get('USER')
password = os.environ.get('PASSWORD')

with open(textfile) as fp:
    # Create a text/plain message
    msg = EmailMessage()
    msg.set_content(fp.read())

msg['Subject'] = f'The contents of {textfile}'
msg['From'] = f'{user}@gmail.com'
msg['To'] = f'{user}@gmail.com'

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.ehlo()
        server.login(user, password)
        server.send_message(msg)
