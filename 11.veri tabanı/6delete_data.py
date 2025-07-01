import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)

cursor=db.cursor()

def deletebyid(idProducts):
    sql="DELETE FROM products Where idProducts=%s"
    params=(idProducts,)
    cursor.execute(sql,params)
    try:
        db.commit()
        print(f"{cursor.rowcount} tane kayıt silindi.")
    except mysql.connector.Error as err:
        print(err)
    finally:
        db.close()
        cursor.close()
deletebyid(10)