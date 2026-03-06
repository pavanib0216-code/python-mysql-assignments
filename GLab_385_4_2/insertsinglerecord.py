import mysql.connector as mydbconnection
from mysql.connector import Error

conn = None

try:
    conn = mydbconnection.connect(
        host='localhost',
        database='usersdb',
        user='pavani',
        password='Pavani@123',
        port='3306'
    )

    mySql_insert_query = """
    INSERT INTO laptop (Id, Name, Price, Purchase_date)
    VALUES (15, 'Lenovo ThinkPad P71', 6459, '2019-08-14')
    """

    cursor = conn.cursor()
    cursor.execute(mySql_insert_query)

    conn.commit()

    print(cursor.rowcount, "Record inserted successfully into Laptop table")

except Error as e:
    print("Failed to insert record into Laptop table", e)

finally:
    if conn is not None and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")