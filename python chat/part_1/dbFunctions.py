import pymysql


class DbFunctions:

    def __init__(self):
        self.cursor = None
        self.connection = None

    def connectDb(self):
        # database connection
        self.connection = pymysql.connect(
            host="localhost", user="root", passwd="", database="school")
        self.cursor = self.connection.cursor()

    def createTables(self):

        # Query for creating table
        table = """CREATE TABLE Chat_History(
        ID INT(20) PRIMARY KEY AUTO_INCREMENT)"""

        query = "SHOW TABLES LIKE 'Chat_History'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if not result:
            self.cursor.execute(table)

        # closeConnection()

    def addNewCol(self, clientName):
        self.connectDb()
        query = "ALTER TABLE Chat_History ADD COLUMN " + \
            clientName+" varchar(500);"
        # query = "ALTER TABLE Chat_History ADD "+clientName+" varchar(500);"

        self.cursor.execute(query)
        # connection.commit()
        self.closeConnection()

    def insertMessage(self, clientName, msg):
        self.connectDb()
        query = "INSERT INTO Chat_History SET "+clientName+" = '" + msg+"' ;"

        # executing the quires
        self.cursor.execute(query)
        # commiting the connection then closing it.
        self.connection.commit()
        self.closeConnection()

    def closeConnection(self):
        self.connection.close()
