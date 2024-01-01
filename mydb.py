# Install Mysql on your computer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python


import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Pass@123' 
)

# prepare cusrson object
cursorObject = dataBase.cursor()

# create a database

cursorObject.execute('CREATE DATABASE dcrm_db')

print('Database created!')