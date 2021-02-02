#this code actually worked 
import mysql.connector
from mysql.connector import errorcode
from datetime import datetime
db =mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='sumpassword', # will enter real password when time to connect
    database='students'
    )

my_cursor = db.cursor()
my_cursor.execute("CREATE TABLE Test(name varchar(50)NOT NULL, created datetime NOT NULL, gender ENUM('M','F','O') NOT NULL, id inT PRIMARY KEY NOT NULL AUTO_INCREMENT)")
