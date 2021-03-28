import datetime, calendar
year: int = int(input('Input year: '))
month: int = 1
day: int = 1
i = 1
data = datetime.date(year, month, day)
if calendar.isleap(year):
    print('Leap year')
    n = 366
else:
    print('Normal year')
    n = 365

while i <= n:
    if (calendar.weekday(data.year, data.month, data.day)) == 0:
        print(data, 'is Monday')
        i += 1
        data += datetime.timedelta(days=1)
    else:
        i += 1
        data += datetime.timedelta(days=1)
