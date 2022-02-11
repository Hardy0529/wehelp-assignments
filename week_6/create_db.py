import mysql.connector

# 創建連線
connection = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="12345678",
    database="website")

cursor = connection.cursor()


# cursor.execute("SELECT * FROM `member`;")
cursor.execute("SELECT * FROM `member`  WHERE `username` = 'test';")

records = cursor.fetchall()
for r in records:
    print(r[2])


cursor.close()
connection.close()
