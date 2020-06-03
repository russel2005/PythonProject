"""
input receiver email address, subject line, message body
"""
import smtplib

SENDER_EMAIL ="touhidul2005@gmail.com"
SENDER_PASSWORD = 'russel50'


def send_email(receiver_email, subject, body):
    message = 'Subject: {}\n\n{}'.format(subject, body)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message)


send_email('russel2005@gmail.com', 'Notification', 'Everything is awesome!')
