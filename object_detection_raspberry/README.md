from email.mime.image import MIMEImage
import os
import smtplib
import ssl
from email.message import EmailMessage
from email.mime import image

def send_email(message, photoB64):
    # Define email sender and receiver
    email_sender = 'skyware.inc@gmail.com'
    email_password = os.environ.get("PASSWORD")
    email_receiver = 'cristianxapata@gmail.com'
    with open('intruder.png', 'rb') as f:
        img_data = f.read()

    # Set the subject and body of the email
    subject = 'Email SENT from Python'
    body = message

    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    image = MIMEImage(img_data, name=os.path.basename("intruder.png"))
    em.attach(image)
    em.set_content(body)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())

if __name__ == '__main__':
    send_email("Hola Mundo", 1234)