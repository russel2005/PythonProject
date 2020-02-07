import datetime
import pytz

today = datetime.date.today()
print(today)

birthday = datetime.date(2016, 2, 26)
print(birthday)

days_since_birth = (today - birthday).days
print(days_since_birth)

#10 days added from current date
tdelta = datetime.timedelta(days=10)
print(today + tdelta)

print(today.day)

#Monday = 0 sunday = 6
print(today.weekday())


print(datetime.time(7, 2, 20, 15))
#datetime.date (Y, M, D)
#datetime.time (h, m, s, ms)
#datetime.datetime (Y, M, D, h, m, s, ms)


#10 hours added current time
hour_delta = datetime.timedelta(hours=10)
print(datetime.datetime.now() + hour_delta)


#use pytz
datetime_today = datetime.datetime.now(tz=pytz.UTC)
datetime_pacific = datetime_today.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)

'''
for tz in pytz.all_timezones:
    print(tz)
'''

#string formatting with dates
#2020-02-03 -> February 3, 2020

print(datetime_today.strftime('%B %d, %Y'))

datetime_thing = datetime.datetime.strptime('February 03, 2020', '%B %d, %Y')
print(datetime_thing)
print(repr(datetime_thing))

