import mysql.connector

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
            """Create USERS table - nb; SHA3-256 hash value are of 256 bits (32 bytes) => 64 hexademical characters => hence, fixed length to 64 for hash store"""
            create_users_query = """CREATE TABLE IF NOT EXISTS users (
                                    userid INT AUTO_INCREMENT, 
                                    username VARCHAR(50) NOT NULL, 
                                    email VARCHAR(50) NOT NULL, 
                                    pwd VARCHAR(50) NOT NULL,
                                    pwd_hash CHAR(64) NOT NULL, 
                                    pwd_salt CHAR(32) NOT NULL,
                                    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                                    deleted INT DEFAULT 0, 
                                    PRIMARY KEY (userid));"""
            self.cursor.execute(create_users_query)            
            """Create COMPANY table"""
            create_applications_query = """CREATE TABLE IF NOT EXISTS applications (
                                           appid INT AUTO_INCREMENT, 
                                           userid INT, 
                                           job_title VARCHAR(50), 
                                           company_name VARCHAR(50), 
                                           application_date DATE, 
                                           application_status VARCHAR(50),
                                           PRIMARY KEY  (appid), 
                                           FOREIGN KEY (userid) REFERENCES users(userid));"""
            self.cursor.execute(create_applications_query)
            self.connection.commit()
            print("mysqlcls.createAllTables()'s created tables and commited changes...")
        except mysql.connector.Error as e:
            print(f"Error at mysqlcls.createAllTables(): {e}") 
        finally:
            if (self.connection or self.cursor):
                self.disconnect()