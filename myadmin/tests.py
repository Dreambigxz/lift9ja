from datetime import datetime
import datetime

# datetime(year, month, day, hour, minute, second)

today = datetime.datetime.today()
a = datetime.datetime(today.year, today.month, today.day, today.hour, today.minute, today.second)
b = datetime.datetime(2021, 9, 17, 23, 48, 17)


# returns a timedelta object
c = a - b
minutes = c.total_seconds() / 60
print('Total difference in minutes: ', minutes)

# returns the difference of the time of the day
minutes = c.seconds / 60
print('Difference in minutes: ', minutes)

emails = ['yusufaiza64@gmail.com', 'gregoryilori02@gmail.com', 'donyemordi@gmail.com']

for email in emails:
    print(email)
    if 'donyemordi@gmail.com' in email:
        print(True)


print('image-7.mp4')