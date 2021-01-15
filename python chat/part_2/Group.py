
from dbUtils import DbConnection


class Group:

    def __init__(self):
        self.ID = ""
        self.groupName = ""
        self.numberOfStudents = 0
        self.performanceLevel = ""
        self.status = ""

        self.db = DbConnection()

    def getID(self):
        return self.ID

    def setGroupName(self, name):
        self.groupName = name

    def getGroupName(self):
        return self.groupName

    def setNumberOfStudents(self, students):
        self.numberOfStudents = students

    def getNumberOfStudents(self):
        return self.numberOfStudents

    def setPerformanceLevel(self, perf):
        self.performanceLevel = perf

    def getPerformanceLevel(self):
        return self.performanceLevel

    def setStatus(self, st):
        self.status = st

    def getStatus(self):
        return self.status

    def createNewGroup(self, name, numStudents, perLevel, status):
        self.db.createNewGroup(name, numStudents, perLevel, status)

    def updateGroupDetails(self, groupName):
        self.db.updateGroupDetails(groupName)

    def deletGroup(self, groupName):
        self.db.deletGroup(groupName)
