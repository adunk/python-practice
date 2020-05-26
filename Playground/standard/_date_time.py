from datetime import datetime, timedelta
import calendar

now = datetime.now()
print(now)
print(now.date())
print(now.year)
print(now.month)
print(now.hour)
print(now.minute)
print(now.second)
print(now.time())
# date() and time() are methods as they combine several attributes

# Change the formatting of a time display. These change how days are formatted
print(now.strftime('%a (short) %A (long) %d (day of the month)'))
print(now.strftime('%b (short) %B (long) %m (number of the month)'))
print(now.strftime('%A %B %d'))
print(now.strftime('%A %B %d %H:%M:%S %p'))
print(now.strftime('%A %B %d %H:%M:%S %p, %Y'))

# Creating future and past date objects
future = now + timedelta(days=2)
past = now - timedelta(weeks=3)
print(future.date())
print(past.date())

if future > past:
    print('Comparision of date objects works')

cal = calendar.month(2001, 10)
print(cal)
cal2 = calendar.weekday(2001, 10, 11)
# Index of the day of the week starting with 0 for Monday
# This prints 3 (Thursday)
print(cal2)

print(calendar.isleap(1999))
print(calendar.isleap(2000))