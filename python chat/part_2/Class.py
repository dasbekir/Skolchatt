from dbUtils import DbConnection


class Class:

    def __init__(self):
        self.ID = ""
        self.className = ""
        self.startTime = ""
        self.endTime = ""
        self.teacherName = ""
        self.location = ""

        self.db = DbConnection()

    def getID(self):
        return self.ID

    def setClassName(self, name):
        self.className = name

    def getClassName(self):
        return self.className

    def setStartTime(self, sTime):
        self.startTime = sTime

    def getStartTime(self):
        return self.startTime

    def setEndTime(self, eTime):
        self.endTime = eTime

    def getEndTime(self):
        return self.endTime

    def setTeacher(self, tName):
        self.teacherName = tName

    def getTeacher(self):
        return self.teacherName

    def setLocation(self, location):
        self.location = location

    def getLocation(self):
        return self.location

    def createNewClass(self, name, sTime, eTime, tName, loc):
        self.db.createNewClass(name, sTime, eTime, tName, loc)

    def updateClassDetails(self, className):
        self.db.updateClassDetails(className)

    def deletClass(self, className):
        self.db.deletClass(className)
