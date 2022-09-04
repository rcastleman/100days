import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
weekday = now.weekday()
# print(year)
# print(month)
# print(weekday)

date_of_birth = dt.datetime(year = 1995,month=12,day=15)
print(date_of_birth)