import mysql.connector
from mysqlconfig import DBCONFIG

class MySqlCls:
    """Class used to set the DB Context"""
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
        """Disconnect method to be called upon completion of each connection query"""
        try:
            if (self.cursor and self.connection):
                self.cursor.close()
                self.connection.close()
                print(f"Disconnected from database: {self.database}")
            else:
                print("mysqlcls.disconnect(): nothing to close...")
        except mysql.connector.Error as e:
            print(f"Error at mysqlcls.disconnect(): {e}")

    def createAllTables(self) -> None:
        """Create all tables necessary if not exist in the db..."""
        try:
            if (self.connection == None or self.cursor == None):
                self.connect()
            """Create USERS table"""
            self.cursor.execute("CREATE TABLE IF NOT EXISTS users (userid INT AUTO_INCREMENT, username VARCHAR(50), email VARCHAR(50), password VARCHAR(50), deleted INT DEFAULT 0, "
                                "PRIMARY KEY (userid));")            
            """Create COMPANY table"""
            self.cursor.execute("CREATE TABLE IF NOT EXISTS applications (appid INT AUTO_INCREMENT, userid INT, job_title VARCHAR(50), company_name VARCHAR(50), "
                                " application_date DATE, application_status VARCHAR(50),"
                                " PRIMARY KEY  (appid), FOREIGN KEY (userid) REFERENCES users(userid));")
            self.connection.commit()
            print("mysqlcls.createAllTables()'s created tables and commited changes...")
        except mysql.connector.Error as e:
            print(f"Error at mysqlcls.createAllTables(): {e}") 
        finally:
            if (self.connection or self.cursor):
                self.disconnect()
 
    def countUser(self, email : str):
        """Query to count the number of users with matching email / for checking if user already exists"""
        try:
            if (self.connection == None or self.cursor == None):
                self.connect()
            self.cursor
        except mysql.connect.Error as e:
            print(f"Error at ") 

    def selectUser(self, email : str):
        """Query to get matching user record(s) from the users table"""
        try:
            if (self.connection == None or self.cursor == None):
                self.connect()
            self.cursor.execute(f"SELECT * FROM users WHERE users.email = {email};")
            rows = self.cursor.fetchall()
            if rows:
                print(len(rows))
                return rows
            print(rows)
            return None
        except mysql.connector.Error as e:
            print(f"Error at mysqlcls.selectUser(): {e}")
            return None 
        finally:
            if (self.connection or self.cursor):
                self.disconnect()
    

myinstance = MySqlCls(DBCONFIG['host'], DBCONFIG['username'], DBCONFIG['password'], DBCONFIG['database'])
#myinstance.createAllTables()
myinstance.selectUser("'foobar@email.com'")