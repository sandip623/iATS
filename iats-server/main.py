"""
import mysql.connector

# Replace these values with your MySQL database credentials
host = 'localhost'
user = 'root'
password = '21168250'
database = 'iatsdb'

# Connect to the MySQL database server
try:
    connection = mysql.connector.connect(
        host=host,
        user=user,
        password=password,
        database=database
    )
    print("Connected to the MySQL database server")
except mysql.connector.Error as e:
    print(f"Error connecting to MySQL database: {e}")

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Example: Execute a SELECT query
try:
    cursor.execute("SELECT * FROM temp_table")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except mysql.connector.Error as e:
    print(f"Error executing SQL query: {e}")

# Close the cursor and connection
cursor.close()
connection.close()
"""

import requests

response = requests.get("https://myjobs.indeed.com/applied")
print(response.status_code)