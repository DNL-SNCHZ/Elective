import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, message):
    from_address = 'youremail@example.com'  # Your email address
    password = 'youpassword'  # Your email account password or App Password

    # Create the email message
    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = to_address

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
         server.login(from_address, password)
         server.sendmail(from_address, to_address, msg.as_string())

# Example Usage
send_email('yourrecipientemail@example.com', 'Elective Test Email', 'This is a test email sent using Python.')


# to run type "py email_automation.py" and the email message will be sent to recipient email
