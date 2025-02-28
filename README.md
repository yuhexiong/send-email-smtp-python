# Send Email SMTP

Use smtplib to send email.  

## Overview

- Language: Python v3.12

## ENV

copy .env.example and rename as .env

```
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_ADDRESS=fromemail@gmail.com
EMAIL_PASSWORD=yourpassword
EMAIL_RECIPIENTS=toemail1@gmail.com,toemail2@gmail.com
EMAIL_SUBJECT="Test Email"
EMAIL_BODY="This is a test email."
```

## Run

### Run Local
```
python send-email-smtp.py
```

### Run In Docker
```
docker-compose up --build
```
