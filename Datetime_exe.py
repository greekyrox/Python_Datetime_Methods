import datetime
import pytz


#DATE (mostly naive)
tday=datetime.date.today()
d=datetime.timedelta(days=10,hours=10)
new_date=tday+d
print(new_date)
print(new_date.day) # .day prints only day
print()# this was an example of time delta

bday=datetime.date(2019,11,6)
td=bday-tday
print(td.total_seconds()) #total_seconds is used for converting anything to seconds
# you'll get time delta if yo add or substract a date from another date
print()

#TIME
t=datetime.time(23,59,59,9999)
print(t)
print(t.hour)
print()

#DATETIME
dt=datetime.datetime(2019,7,25,12,4,59)
tdelta=datetime.timedelta(hours=12)#adding a time delta in the datetime

dt=dt+tdelta
print(dt)
print(dt.minute)
print(dt.year)

print()
print(datetime.datetime.today()) #no option to pass tz info
print(datetime.datetime.now()) #has an option to pass tz info
print(datetime.datetime.utcnow()) #gives equvalent utc  time