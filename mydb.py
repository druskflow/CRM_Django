# install Mysql on your computer
# pip install mysql
# pip install mysql-connector

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',

)

#  prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE dcrm")

print("All Done!")