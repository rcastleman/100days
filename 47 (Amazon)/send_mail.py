import smtplib
import datetime as dt

gmail_email = "rc.code.test@gmail.com"
gmail_password =  "xxfgumnxsleullfm"
gmail_SMTP = "smtp.gmail.com"
send_to = "rcastleman@gmail.com"

now = dt.datetime.now()
hour = now.hour
minute = now.minute

email_body = f"Subject:test at {hour}:{minute} \n\nTest email body ...  "


def send_email(body):
    server = smtplib.SMTP()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_email, gmail_password)
    server.sendmail(gmail_email,send_to,f"Subject:Happy Birthday!\n\n{body}")
    server.quit()

