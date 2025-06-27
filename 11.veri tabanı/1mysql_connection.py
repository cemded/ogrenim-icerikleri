import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)

cursor = db.cursor()
# cursor.execute("CREATE DATABASE cemdb") data base oluşturur
# cursor.execute("show databases")

cursor.execute("SHOW TABLES")
for x in cursor:
    print(x)