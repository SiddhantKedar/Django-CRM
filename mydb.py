#pip install my sql
# pip install mysql-conectior
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'password123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE SMA")

print("All done!")