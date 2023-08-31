import smtplib
from email.message import EmailMessage

email = EmailMessage()

email['from'] = 'Lokudu James Simon'
email['to'] = 'james0954858998@gmail.com'
email['subject'] = 'You won a free Macbook'

email.set_content('I am a Python Master!')

with smtplib.SMTP(host ='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('jameslokudu24@gmail.com', 'P@mel@@2o2o!!')
    smtp.send_message(email)
    print('all good boss!')