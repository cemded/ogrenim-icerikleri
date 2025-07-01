import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)

cursor=db.cursor()

# sql="SELECT COUNT(*) FROM products"
# sql="SELECT AVG(Price) FROM products"
# sql="SELECT SUM(Price) FROM products"
# sql="SELECT MIN(Price) FROM products"
# sql="SELECT MAX(Price) FROM products"
# sql="SELECT Name,Price FROM products WHERE Price=(SELECT MAX(Price) FROM products)"
#sql="SELECT Name,Price FROM products ORDER BY Price"  #ORDER BY Price DESC azalan


def selectbyprice(Price):
    sql="SELECT Name,Price From products WHERE Price=%s"
    params=(Price,)
    cursor.execute(sql,params)


    try:
        result=cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()    

        print(result)
        
selectbyprice(4000)