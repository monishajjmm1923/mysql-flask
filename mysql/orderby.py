import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="mydatabase"
)

mycursor = mydb.cursor()

#sql = "SELECT * FROM customers ORDER BY name"
sql = "SELECT * FROM customers ORDER BY name DESC"  #Sort the result reverse alphabetically by name

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
