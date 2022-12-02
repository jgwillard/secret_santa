import smtplib
import os

from email.message import EmailMessage

def send_email(fr, to, subject, content, user, password):
    msg = EmailMessage()
    msg.set_content(content)
    msg['From'] = fr
    msg['To'] = to
    msg['Subject'] = subject

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.ehlo()
            server.login(user, password)
            server.send_message(msg)
