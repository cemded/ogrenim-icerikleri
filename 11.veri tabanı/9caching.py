import mysql.connector
from cachetools import cached,TTLCache

db= mysql.connector.connect(
    host="localhost",
    user="root",
    password="Cem133cem",
    database="shopdb" #üzerinde çalışıcagımız database
)


@cached(cache=TTLCache(maxsize=30,ttl=60))
def listproductsbyname(name):
    cursor=db.cursor()
    sql="SELECT p.name,c.name FROM products p INNER JOIN category c ON p.categoryid=c.id WHERE c.name=%s"
    params=(name,)
    cursor.execute(sql,params)
    try:
         return cursor.fetchall()
    except mysql.connector.Error as err:
        print(err)
print(listproductsbyname("Phone"))


# from cachetools import cached, TTLCache
# import mysql.connector

# @cached(cache=TTLCache(maxsize=30, ttl=60))
# def listproductsbyname(name):
#     try:
#         with mysql.connector.connect(
#             host="localhost",
#             user="root",
#             password="Cem133cem",
#             database="shopdb"
#         ) as db:
#             with db.cursor() as cursor:
#                 sql = "SELECT p.name, c.name FROM products p INNER JOIN category c ON p.categoryid=c.id WHERE c.name=%s"
#                 params = (name,)
#                 cursor.execute(sql, params)
#                 return cursor.fetchall()
#     except mysql.connector.Error as err:
#         print(err)
