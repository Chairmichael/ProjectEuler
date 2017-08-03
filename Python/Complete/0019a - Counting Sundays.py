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

# [day, month(1-12), year(1900-2000), dayOfWeek(0-6)]
time = [ ]
day_of_week = 1
for year in range(1900, 2001):
	for month in range(1, 13):
		for day in range(1, 32):
			time.append([day, month, year, day_of_week])
			day_of_week += 1
			if day_of_week > 6: day_of_week = 0
			if month in [4, 6, 9, 11] and day is 30:
				break
			if month is 2 and day is 28:
				if year % 4 is 0 and year % 400 is not 0:
					time.append([day+1, month, year, day_of_week])
					day_of_week += 1
					if day_of_week > 6: day_of_week = 0
					break
				else:
					break
sundays = 0
for day in time:
	if day[3] is 0 and day[2] > 1900 and day[0] is 1:
		sundays += 1
print(sundays)
### has a fucking off-by-one error; ans=171