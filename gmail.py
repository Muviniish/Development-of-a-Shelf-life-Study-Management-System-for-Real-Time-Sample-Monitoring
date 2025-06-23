import smtplib
from email.mime.text import MIMEText


def main(email,test_date):
    sender_email = "muviniish15@gmail.com"
    password = "hugasegmsfvbfknn"
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    receiver_email = email

    subject = "Reminder: Your Product Test Date is Approaching"
    body = f"This is a reminder that your product is scheduled for testing on {test_date}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email:", e)