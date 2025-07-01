import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)

cursor=db.cursor()

#sql="SELECT * FROM products WHERE Price=4000" #eğer içeride name kullanırsan ' tırnak kullanman gerek dışarıda " olduğu için

#sql="SELECT * FROM products WHERE name LIKE '%telefon%'"
#sql="SELECT * FROM products WHERE name LIKE '%telefon'" #telefon ile biten kayıtlar % başta olursa
#sql="SELECT * FROM products WHERE name LIKE 'telefon%'" #telefon ile başlayan kayıtlar % sonda olursa
#cursor.execute(sql)

# for x in product:
#     print(x)

def getproductbyprice(Price):
    sql="SELECT * FROM products WHERE Price=%s"
    params=(Price,)
    cursor.execute(sql,params)
    product=cursor.fetchall()
    print(product)

getproductbyprice(5000)

