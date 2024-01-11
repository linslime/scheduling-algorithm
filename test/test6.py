import datetime
import numpy as np

def getDateList(startDate,endDate):
    startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
    endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    list = []
    now = startDate
    while True:
        print(now)
        list.append(now)
        temp = endDate - now
        if temp.days <= 0:
            break
        now = now + datetime.timedelta(days=1)
    num = round(len(list) / 7)
    list = np.array(list).reshape(num,7)
    return list

dateList = getDateList('2023-04-03','2023-05-07')
print(dateList[0][0])