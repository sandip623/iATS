import mysql.connector 
from mysqlcls import MySqlCls
from mysqlconfig import DBCONFIG

class UserRepository(MySqlCls):
    """A repository class for managing user-related database operations..."""
    def __init__(self, host : str, username : str, password : str, database : str):
        """call the super method to invoke the constructor of the parent class -> i.e., pre-initialize database connection methods"""
        super().__init__(host, username, password, database) 

    def getUser(self, email : str):
        """Query to get matching user record(s) from the users table"""
        try:
            if (self.connection == None or self.cursor == None):
                self.connect()
            self.cursor.execute(f"SELECT * FROM users WHERE users.email = {email};")
            rows = self.cursor.fetchall()
            if rows:
                print(rows)
                return rows
            return None
        except mysql.connector.Error as e:
            print(f"Error at mysqlcls.getUser(): {e}")
            return None 
        finally:
            if (self.connection or self.cursor):
                self.disconnect()

myinstance = UserRepository(DBCONFIG['host'], DBCONFIG['username'], DBCONFIG['password'], DBCONFIG['database'])
myinstance.getUser("'foobar@email.com'")