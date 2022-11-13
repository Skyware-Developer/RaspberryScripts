
import os
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


def send_email(message, photoB64):
    # Define email sender and receiver
    email_sender = 'SENDER EMAIL'
    email_password = "PASSWORD"
    email_receiver =  'RECEPIENT EMAIL'
    with open('filename', 'rb') as f:
        img_data = f.read()

    # Set the subject and body of the email
    subject = 'Email SENT from Python'
    body = message

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    image = MIMEImage(img_data, name=os.path.basename("filename"))
    em.attach(image)
    em.set_content(body)

    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = email_sender
    msg['To'] = email_receiver

    text = MIMEText(message)
    msg.attach(text)
    image = MIMEImage(img_data, name=os.path.basename("filename"))
    msg.attach(image)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, msg.as_string())

if __name__ == '__main__':
    send_email("Hola Mundo", 1234)