import mysql.connector

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)

cursor = db.cursor()

sql="INSERT INTO products (Name,Price,imageURL,Description) VALUES (%s,%s,%s,%s)"
# value=("telefon 5",4000,"5.jpg","telefondur")
# cursor.execute(sql,value)    tek bir kayıt

values=[("telefon 9",4000,"6.jpg","telefondur"),
        ("telefon 10",5000,"7.jpg","telefondur"),
        ("telefon 11",6000,"8.jpg","telefondur")
        ]

cursor.executemany(sql,values)


try:
    db.commit()
    print(cursor.rowcount ,"kayıt edildi")
    print(f"son eklenen product id : {cursor.lastrowid}")
except mysql.connector.Error as err:
    print("hata:",err)
finally:
    cursor.close()
    db.close()
    print("bağlantı kapatıldı")