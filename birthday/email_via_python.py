from multiprocessing import connection
import smtplib
import datetime as dt

yahoo_email = "rc.code@yahoo.com"
yahoo_password = "NunCOmpGRA"
yahoo_SMTP = "smtp.mail.yahoo.com"
gmail_email = "rc.code.test@gmail.com"
# gmail_password = "DEpicHErON"
gmail_password =  "xxfgumnxsleullfm"
gmail_SMTP = "smtp.gmail.com"
send_to = "rcastleman@gmail.com"

now = dt.datetime.now()
hour = now.hour
minute = now.minute

email_body = f"Subject:test at {hour}:{minute} \n\nTest email body ...  "

#angela's code doesn't work because 'less secure apps' are no longer supported by gmail or yahoo ... found code snippet here: https://stackoverflow.com/questions/57598232/timed-out-error-when-using-python-to-send-an-email

def send_email(body):
    server = smtplib.SMTP()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(gmail_email, gmail_password)
    server.sendmail(gmail_email,send_to,body)
    server.quit()

# send_email(email_body)