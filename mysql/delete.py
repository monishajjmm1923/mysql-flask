#import mysql.connector

# host="localhost",
 # user="root",
  #passwd="",
  #database="mydatabase"
#)

#mycursor = mydb.cursor()

#sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

#mycursor.execute(sql)

#mydb.commit()

#print(mycursor.rowcount, "record(s) deleted")

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers1"

mycursor.execute(sql)