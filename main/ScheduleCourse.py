class ScheduleCourse(object):
    def __init__(self,roomId,teacherId,dateTime,beginTime,endTime,duration):
        self.roomId = roomId
        self.teacherId = teacherId
        self.dateTime = dateTime
        self.beginTime = beginTime
        self.endTime = endTime
        self.duration = duration
