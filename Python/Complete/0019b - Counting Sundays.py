'''
You are given the following information, 
but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September, April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.

A leap year occurs on any year evenly divisible by 4, 
but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the 
twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''
from datetime import timedelta, date

start = date(1900, 1, 1)
day_count = int(1e5)
monday_count = 0
for day in (start + timedelta(n) for n in range(day_count)):
	if day.year == 2001: break
	elif day.year > 1900:
		if day.weekday() is 6 and day.day is 1:
			monday_count += 1
print(monday_count)