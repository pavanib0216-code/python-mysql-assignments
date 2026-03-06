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

    cursor = conn.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS laptop (
        Id INT NOT NULL,
        Name VARCHAR(250) NOT NULL,
        Price FLOAT NOT NULL,
        Purchase_date DATE NOT NULL
    )
    """

    cursor.execute(create_table_query)
    print("Table is created")

except Error as e:
    print("Failed to create table:", e)

finally:
    if conn is not None and conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed") 