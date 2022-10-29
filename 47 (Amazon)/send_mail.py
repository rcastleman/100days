import smtplib
import datetime as dt

gmail_email = "rc.code.test@gmail.com"
gmail_password =  "xxfgumnxsleullfm"
gmail_SMTP = "smtp.gmail.com"
send_to = "rcastleman@gmail.com"

now = dt.datetime.now()
hour = now.hour
minute = now.minute

body = f"Subject:test at {hour}:{minute} \n\nTEXT IN THE BODY HERE"

def send_email(body):
    server = smtplib.SMTP()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_email, gmail_password)
    server.sendmail(gmail_email,send_to,body)
    server.quit()

# send_email(body)