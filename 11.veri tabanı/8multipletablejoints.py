import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)

cursor = db.cursor()

#sql="SELECT * FROM products"

def listproductsbyname(name):
    sql="SELECT p.name,c.name FROM products p INNER JOIN category c ON p.categoryid=c.id WHERE c.name=%s"
    params=(name,)
    cursor.execute(sql,params)
    try:
        result=cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()
        print(result)
listproductsbyname("Phone")