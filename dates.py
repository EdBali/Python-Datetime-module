import datetime
import pytz
#-----------------SUMMARRY OF DATETIME module------------
#-------------The datetime module has 4 classes:
# datetime.date ---(year,month,date)
# datetime.time ---(hour,minute,second,microsecond)
# datetime.datetime ---(year,month,date,hour,minute,second,microsecond)
# datetime.timedelta ---this deals with duration in days,month,years,hour,minute,second,microsecond


#printing the current date
today = datetime.date.today()
print(today)

#printing my birthday
birthday = datetime.date(2000,12,18)
print(birthday)

#calculating number of days since birth
days_since_birth = (today - birthday).days
print(days_since_birth)

#Adding and subtracting days using timedelta
ten_days = datetime.timedelta(days = 10)
print(today + ten_days)

#How to get specifc day,month,weekday
print(datetime.date.today().month)
# print(datetime.date.today().day)
# print(datetime.date.today().weekday)


#Adding 10hours to current time
ten_hours = datetime.timedelta(hours = 10)
print(datetime.datetime.now() + ten_hours)


#Working with time zones..You have to pip install "pytz" module, then import it
datetime_day =  datetime.datetime.now(tz = pytz.UTC)
datetime_pacific = datetime_day.astimezone(pytz.timezone('US/Pacific'))
print(datetime_pacific)

#Printing list of available timezones
# for tz in pytz.all_timezones:
#     print(tz)

#String Formatting Dates
print(datetime_pacific.strftime('%B %d, %Y'))

#Turning a normal String date to a datetime object
datetime_object = datetime.datetime.strptime('March 09, 2010','%B %d, %Y')
print(datetime_object)


#NB: look for "MAYA" for easier manipulation of dates