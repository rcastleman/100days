from multiprocessing import connection
import smtplib
import datetime as dt


gmail_email = "rc.code.test@gmail.com"
gmail_password =  "xxfgumnxsleullfm"
gmail_SMTP = "smtp.gmail.com"
send_to = "rcastleman@gmail.com"

now = dt.datetime.now()
hour = now.hour
minute = now.minute

generic_subject = "Subject line"
generic_body = "Body of the email"

def send_email(subject,body):
    server = smtplib.SMTP()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_email, gmail_password)
    server.sendmail(gmail_email,send_to,f"Subject: {subject}\n\n{body}")
    server.quit()

# send_email(generic_subject,generic_body)