import sys
import json

class hello(object):  # 创建Circle类
   def __init__(self,id,name):  # 约定成俗这里应该使用r，它与self.r中的r同名
       self.id = id
       self.name = name

def dict2hello(d):
    return hello(d['id'],d['name'])

class AutoScheduleParm(object):
    def __init__(self,roomId,startDate,endDate):
        self.roomId = roomId
        self.startDate = startDate
        self.endDate = endDate

def dict2AutoScheduleParm(d):
    return AutoScheduleParm(d['roomId'], d['startDate'], d['endDate'])

if __name__ == '__main__':
    # h1 = hello("id1","name1")
    # h2 = hello("id2","name2")
    # for i in sys.argv:
    #     print(type(i))
    # str = json.dumps(h1.__dict__)
    # sss = sys.argv[1]
    # print(sys.argv[1])
    # hh = json.loads(str, object_hook=dict2hello)
    # hh = json.loads(sys.argv[1], object_hook=dict2AutoScheduleParm)
    # hh.roomId = 3
    # print(sss)
    # asp = AutoScheduleParm(1,'2023-04-03','2023-05-08')
    # aspStr = json.dumps(asp.__dict__)
    # print(aspStr)
    # asp2 = json.loads(aspStr, object_hook=dict2AutoScheduleParm)
    # print(asp2.__dict__)
    # id = asp2.roomId
    list = "{\"endDate\":\"2023-05-08\",\"roomId\":1,\"startDate\":\"2023-04-03\"}"
    asp2 = json.loads(list, object_hook=dict2AutoScheduleParm)
    print(asp2.__dict__)
    # print(sys.argv[1],type(sys.argv[1]))

    # for i in range(1,len(sys.argv)):
    print(sys.argv[1])




