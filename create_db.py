import mysql.connector
import os

username = os.environ.get("root")
password = os.environ.get("toor")

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd = 'toor',
    database='our_users'
)

my_cursor = mydb.cursor()

# my_cursor.execute("CREATE DATABASE order_gegevens")

my_cursor.execute('show databases')
for db in my_cursor:
    print(db)