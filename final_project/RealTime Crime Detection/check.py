import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Yashukk03@"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Criminals")



mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)


