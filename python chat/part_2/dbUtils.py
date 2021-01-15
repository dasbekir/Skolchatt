
import pymysql


class DbConnection:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connectDb(self):
        # database connection
        self.connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="school")
        self.cursor = self.connection.cursor()

        if(self.cursor):
            self.createTables()

    def createTables(self):

        # Query for creating table
        classTable = """CREATE TABLE Classes(
        ID INT(20) PRIMARY KEY AUTO_INCREMENT,
        CLASS_NAME  CHAR(20) NOT NULL,
        START_TIME CHAR(30) NOT NULL,
        END_TIME  CHAR(30) NOT NULL,
        TEACHER_NAME CHAR(30),
        LOCATION CHAR(30))"""

        # Query for creating table
        groupTable = """CREATE TABLE Groups(
        ID INT(20) PRIMARY KEY AUTO_INCREMENT,
        GROUP_NAME  CHAR(20) NOT NULL,
        NUM_STUDENTS CHAR(30) NOT NULL,
        PERFORMANCE_LEVEL  CHAR(30) NOT NULL,
        STATUS CHAR(30) NOT NULL)"""

        query = "SHOW TABLES LIKE 'Classes'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if not result:
            self.cursor.execute(classTable)

        query = "SHOW TABLES LIKE 'Groups'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if not result:
            pass
            self.cursor.execute(groupTable)

    def createNewClass(self, name, sTime, eTime, tName, loc):
        self.connectDb()
        query = "INSERT INTO Classes(CLASS_NAME, START_TIME, END_TIME, TEACHER_NAME, LOCATION) VALUES('" + \
            name+"','"+sTime+"','"+eTime+"','"+tName+"','"+loc+"' );"

        # executing the quires
        self.cursor.execute(query)

        # commiting the connection then closing it.
        self.connection.commit()

        self.closeConnection()

    def updateClassDetails(self, className):

        self.connectDb()
        q = "SELECT * FROM Classes WHERE CLASS_NAME = '"+className+"' ;"
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

        print(len(result))
        while True:
            print("\n....Which column do you want to update?")
            print(
                "1. CLASS_NAME\n2. START_TIME\n3. END_TIME\n4. TEACHER_NAME\n5. LOCATION\n")
            opt = input("Choose One: ")
            val = input("Enter New Value: ")

            if opt == "1":
                updateSql = "UPDATE classes SET CLASS_NAME= '" + \
                    val+"'  WHERE CLASS_NAME = '"+className+"' ;"
            elif opt == "2":
                print("In Start time......................")
                updateSql = "UPDATE classes SET START_TIME= '" + \
                    val+"'  WHERE CLASS_NAME = '"+className+"' ;"
            elif opt == "3":
                updateSql = "UPDATE classes SET END_TIME= '" + \
                    val+"'  WHERE CLASS_NAME = '"+className+"' ;"
            elif opt == "4":
                updateSql = "UPDATE classes SET TEACHER_NAME= '" + \
                    val+"'  WHERE CLASS_NAME = '"+className+"' ;"
            elif opt == "5":
                updateSql = "UPDATE classes SET LOCATION= '" + \
                    val+"'  WHERE CLASS_NAME = '"+className+"' ;"

            # print(updateSql)
            res = self.cursor.execute(updateSql)
            print("\nrows Effected: ", res)
            if res != 0:
                print("Record Updated Successfully...\n")
                self.connection.commit()
            else:
                print("\nError updating record..\n")

            again = input("Do you want to update Another column(Y or N): ")
            print("\n")
            if again.upper() == "Y":
                continue
            else:
                break

        self.closeConnection()

    def deletClass(self, className):

        self.connectDb()
        deleteSql = "DELETE FROM classes WHERE CLASS_NAME = '"+className+"'; "
        res = self.cursor.execute(deleteSql)

        if res != 0:
            print("Record deleted successfully..")
            self.connection.commit()
        else:
            print("Sorry No rows deleted...")

        self.closeConnection()

    def createNewGroup(self, name, numStudents, perLevel, status):
        self.connectDb()
        query = "INSERT INTO Groups(GROUP_NAME, NUM_STUDENTS, PERFORMANCE_LEVEL, STATUS) VALUES('" + \
            name+"','"+numStudents+"','"+perLevel+"','"+status+"' );"

        # executing the quires
        self.cursor.execute(query)

        # commiting the connection then closing it.
        self.connection.commit()

        self.closeConnection()

    def updateGroupDetails(self, groupName):

        self.connectDb()
        q = "SELECT * FROM Groups WHERE GROUP_NAME = '"+groupName+"' ;"
        self.cursor.execute(q)
        result = self.cursor.fetchall()
        for row in result:
            print(row)

        print(len(result))
        while True:
            print("\n....Which column do you want to update?")
            print(
                "1. GROUP_NAME\n2. NUM_STUDENTS\n3. PERFORMANCE_LEVEL\n4. STATUS\n")
            opt = input("Choose One: ")
            val = input("Enter New Value: ")

            if opt == "1":
                updateSql = "UPDATE Groups SET GROUP_NAME= '" + \
                    val+"'  WHERE GROUP_NAME = '"+groupName+"' ;"
            elif opt == "2":
                print("In Start time......................")
                updateSql = "UPDATE Groups SET NUM_STUDENTS= '" + \
                    val+"'  WHERE GROUP_NAME = '"+groupName+"' ;"
            elif opt == "3":
                updateSql = "UPDATE Groups SET PERFORMANCE_LEVEL= '" + \
                    val+"'  WHERE GROUP_NAME = '"+groupName+"' ;"
            elif opt == "4":
                updateSql = "UPDATE Groups SET STATUS= '" + \
                    val+"'  WHERE GROUP_NAME = '"+groupName+"' ;"

            # print(updateSql)
            res = self.cursor.execute(updateSql)
            print("\nrows Effected: ", res)
            if res != 0:
                print("Record Updated Successfully...\n")
                self.connection.commit()
            else:
                print("\nError updating record..\n")

            again = input("Do you want to update Another column(Y or N): ")
            print("\n")
            if again.upper() == "Y":
                continue
            else:
                break

        self.closeConnection()

    def deletGroup(self, groupName):

        self.connectDb()
        deleteSql = "DELETE FROM Groups WHERE GROUP_NAME = '"+groupName+"'; "
        res = self.cursor.execute(deleteSql)

        if res != 0:
            print("Record deleted successfully..")
            self.connection.commit()
        else:
            print("Sorry No rows deleted...")

        self.closeConnection()

    def closeConnection(self):
        self.connection.close()
