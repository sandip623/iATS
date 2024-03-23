import mysql.connector
from mysqlconfig import DBCONFIG

class MySqlCls:
    def __init__(self, host : str, username : str, password : str, database : str):
        self.host = host
        self.username = username
        self.password = password 
        self.database = database
        self.connection = None
        self.cursor = None
    
    def connect(self) -> None:
        try:
            self.connection = mysql.connector.connect(
                host=self.host, 
                user=self.username,
                password=self.password,
                database=self.database
            )
            print(f"Connected to the MySQL database: {self.database}")
            self.cursor = self.connection.cursor()
        except mysql.connector.Error as e:
            print(f"Error connecting to MySQL database: {e}")

    def disconnect(self) -> None:
        try:
            if (self.cursor and self.connection):
                self.cursor.close()
                self.connection.close()
                print(f"Disconnected from database: {self.database}")
            else:
                print("mysqlcls.disconnect(): nothing to close...")
        except mysql.connector.Error as e:
            print(f"Error at mysqlcls.disconnect(): {e}")

    def getDummyTable(self) -> None:
        """Query to get the """
        try:
            self.connect()
            if (self.connection and self.cursor):
                self.cursor.execute("SELECT * FROM dummytable")
                rows = self.cursor.fetchall()
                for row in rows:
                    print(row)
                self.disconnect()
            else:
                print(f"mysqlcls.getDummyTable() connection or cursor not set...")
        except mysql.connector.Error as e:
            print(f"mysqlcls.getDummyTable() produced error: {e}")

    

myinstance = MySqlCls(DBCONFIG['host'], DBCONFIG['username'], DBCONFIG['password'], DBCONFIG['database'])
myinstance.getDummyTable()