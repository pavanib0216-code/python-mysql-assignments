import mysql.connector as dbconnect
from mysql.connector import Error


# 1️⃣ Define the function
def create_table(connection):
    cursor = connection.cursor()

    create_table_query = """
    CREATE TABLE IF NOT EXISTS tasks (
        task_id INT AUTO_INCREMENT,
        title VARCHAR(255) NOT NULL,
        start_date DATE,
        due_date DATE,
        priority TINYINT NOT NULL DEFAULT 3,
        description TEXT,
        PRIMARY KEY (task_id)
    )
    """

    cursor.execute(create_table_query)
    print("Table 'tasks' created successfully")

    cursor.close()


# 2️⃣ Now BELOW the function, connect and call it
try:
    myconnection = dbconnect.connect(
        host='localhost',
        database='classicmodels',
        user='pavani',
        password='Pavani@123'
    )

    if myconnection.is_connected():
        print("Connected to MySQL")

        create_table(myconnection)   # 👈 THIS CALLS THE FUNCTION

except Error as e:
    print("Error:", e)

finally:
    if myconnection.is_connected():
        myconnection.close()
    print("Connection closed")