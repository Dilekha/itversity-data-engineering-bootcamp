import mysql.connector as mc
from mysql.connector import errorcode as ec

user = "retail_user"
password = "itversity909090"
host = "34.94.114.182"
db = "retail"

connection = mc.connect(user=user,
                        password=password,
                        host=host,
                        database=db
                       )
orders_cursor = connection.cursor()
query = """SELECT * FROM orders LIMIT 10"""
orders_cursor.execute(query)

for order in orders_cursor:
    print(order)

connection.close()
