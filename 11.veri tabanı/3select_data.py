import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)

cursor=db.cursor()
#sql="SELECT * FROM products" #bu bütün listeyi alır ayrıntılı seçmek istersen burada eleme yapabilirsin

sql="SELECT idProducts,Name FROM products"

cursor.execute(sql)

#product=cursor.fetchall()

product=cursor.fetchone()

# for x in product:
#     print(x[0],x[1]) 

print(product)