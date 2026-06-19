import pymysql

try:
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="Deepikahari@05"
    )

    print("Connected Successfully")
    conn.close()

except Exception as e:
    print("Error:", e)