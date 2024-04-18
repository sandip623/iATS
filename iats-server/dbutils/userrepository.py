import mysql.connector 
from .mysqlcls import MySqlCls
from .mysqlconfig import DBCONFIG

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
            query = f"SELECT * FROM users WHERE users.email = '{email}';"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            if rows:
                return rows
            return None
        except mysql.connector.Error as e:
            print(f"Error at mysqlcls.getUser(): {e}")
            return e 
        finally:
            if (self.connection or self.cursor):
                self.disconnect()

    def countUser(self, email : str) -> int:
        """Query to return total number of matching user from the users table"""
        try:
            if (self.connection == None or self.cursor == None):
                self.connect()
            #self.cursor = self.connection.cursor()
            query = f"SELECT COUNT(*) FROM users WHERE users.email = '{email}';"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            if rows:
                """Unpack the list of tuple to get the return value"""
                [(value,)] = rows 
                return value
        except mysql.connector.Error as e:
            print(f"Error at UserRepository.countUser(): {e}") 
            return e
        finally:
            if (self.connection or self.cursor):
                self.disconnect()

    def createUser(self, userdata : tuple) -> str:
        """Query used when registering a new user in the application"""
        try:
            if (self.connection == None or self.cursor == None):
                self.connect()
            #self.cursor = self.connection.cursor()
            query = f"""INSERT INTO users(username, email, pwd, pwd_hash, pwd_salt) 
                        VALUES ('{userdata.username}', '{userdata.email}', '{userdata.pwd}', '{userdata.pwd_hash}', '{userdata.pwd_salt}');"""
            self.cursor.execute(query)
            self.connection.commit()
            print("createUser() committed successfully")
            return "createUser() called successfully..."
        except mysql.connector.Error as e:
            print(f"Error at UserRepository.countUser(): {e}") 
            return e
        finally:
            if (self.connection or self.cursor):
                self.disconnect()
    
#myinstance = UserRepository(DBCONFIG['host'], DBCONFIG['username'], DBCONFIG['password'], DBCONFIG['database'])
#myinstance.countUser("foobar@email.com")