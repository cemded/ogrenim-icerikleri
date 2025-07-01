import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)

cursor=db.cursor()

def sqlupdate(idProducts,Name,Price):
    sql="UPDATE products SET Name=%s,Price=%s*1.2 WHERE idProducts=%s"
    params=(Name,Price,idProducts)
    cursor.execute(sql,params)
    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt güncellendi.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()
sqlupdate(2,"telefon 2 updated",2000)