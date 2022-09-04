from multiprocessing import connection
import smtplib

my_email = "rc.code.test@gmail.com"
my_password = "DEpicHErON"

connection = smtplib.SMTP("smtp.gmail.com")

#encrypts connection
connection.starttls()
connection.login(user = my_email,password = my_password)
connection.sendmail(from_addr = my_email,to_addrs = "rcastleman@gmail.com")
