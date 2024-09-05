
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(subject, body, to_email, password, from_email):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the server and send the email
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

def send_multiple_emails(subject, body, to_email, password, from_email, num_times):
    for i in range(num_times):
        unique_subject = f"{subject} - {i+1}"
        print(f'Sending email {i+1} of {num_times}')
        send_email(unique_subject, body, to_email, password, from_email)

# Example usage
from_email = 'enter your email here'
password = 'go to your google account and search app passwords. create one and put it here.'
to_email = 'the email you want to spam'
subject = 'subject'
body = 'text'
num_times = 20  # Number of times to send the email

send_multiple_emails(subject, body, to_email, password, from_email, num_times)
