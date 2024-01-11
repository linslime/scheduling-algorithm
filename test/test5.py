import datetime

now = datetime.datetime.strptime("2023-04-03", '%Y-%m-%d')
print(now)
delta = datetime.timedelta(hours=3)
n_days = now + delta
print(n_days.strftime('%H:%M:%S'))