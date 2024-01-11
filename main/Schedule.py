import datetime
import json
import sys
from Solver import *
from AutoScheduleParm import *
from ScheduleCourse import *
import numpy

def getDateList(startDate,endDate):
    startDate = datetime.datetime.strptime(startDate, '%Y-%m-%d')
    endDate = datetime.datetime.strptime(endDate, '%Y-%m-%d')
    list = []
    now = startDate
    while True:
        list.append(now)
        temp = endDate - now
        if temp.days <= 0:
            break
        now = now + datetime.timedelta(days=1)
    num = round(len(list) / 7)
    list = numpy.array(list).reshape(num,7)
    return list

def getTime(date,step,list):
    ans = []
    temp = []
    bt = 8
    if date.weekday() == 5 or date.weekday() == 6:
        bt = 9
    for i in range(len(list)):
        if len(temp) == 0 and list[i] == 1:
            temp.append(i)
            temp.append(i)
        elif len(temp) == 2 and list[i] == 1:
            temp[1] = i
        if len(temp) == 2 and (list[i] == 0 or i == len(list) - 1):

            st = datetime.timedelta(minutes=(60 * bt +step*temp[0])) + date
            ed = datetime.timedelta(minutes=(60 * bt + step*(temp[1] + 1))) + date
            duration = step * (temp[1] - temp[0] + 1)
            ans.append([st.strftime('%H:%M:%S'), ed.strftime('%H:%M:%S'), duration])
            temp = []
    return ans

if __name__ == '__main__':
    autoScheduleParm = AutoScheduleParm(sys.argv[1], sys.argv[2], sys.argv[3])
    # autoScheduleParm = AutoScheduleParm(1,'2023-04-03','2023-05-07')
    dateList = getDateList(autoScheduleParm.startDate,autoScheduleParm.endDate)
    y = 0
    for i in range(len(dateList)):
        solver = Solver(7, 20, 0, 15)
        y = solver.solver()
        for j in range(len(y)):
            for k in range(len(y[j])):
                list = getTime(dateList[i][j],60,y[j][k])
                for l in list:
                    scheduleCourse = ScheduleCourse(autoScheduleParm.roomId,(int(autoScheduleParm.roomId) - 1) * 20 + k,str(dateList[i][j].date()),l[0],l[1],l[2])
                    print(json.dumps(scheduleCourse.__dict__))



