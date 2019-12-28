#Select the 5 first records in the "customers" table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

#mycursor.execute("SELECT * FROM customers LIMIT 5")
mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")#Start from position 3, and return 5 records

myresult = mycursor.fetchall()

for x in myresult:
  print(x)