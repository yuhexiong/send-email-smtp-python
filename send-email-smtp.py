import os
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_email(subject, body, from_email, to_emails):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    
    try:
        with smtplib.SMTP(os.getenv('EMAIL_HOST'), int(os.getenv('EMAIL_PORT'))) as server:
            server.starttls()
            server.login(from_email, os.getenv('EMAIL_PASSWORD'))
            server.sendmail(from_email, to_emails, msg.as_string())
        print('Email sent successfully!')
    except Exception as e:
        print(f'Failed to send email: {e}')

if __name__ == '__main__':
    subject = os.getenv('EMAIL_SUBJECT')
    body = os.getenv('EMAIL_BODY')
    from_email = os.getenv('EMAIL_ADDRESS')
    to_emails = os.getenv('EMAIL_RECIPIENTS').split(',')

    send_email(subject, body, from_email, to_emails)
