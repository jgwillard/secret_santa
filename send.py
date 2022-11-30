import smtplib
import os

from email.message import EmailMessage

def send_email(to, fr, subject, content, user, password):
    msg = EmailMessage()
    msg.set_content(content)
    msg['Subject'] = subject
    msg['From'] = f'{fr}@gmail.com'
    msg['To'] = f'{to}@gmail.com'

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.ehlo()
            server.login(user, password)
            server.send_message(msg)
