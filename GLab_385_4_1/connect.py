import mysql.connector as mydbconnection
from mysql.connector import Error

def connect():
    """ Connect to MySQL database """
    conn = None
    try:
        conn = mydbconnection.connect(
            host='localhost',
            database='classicmodels',
            user='pavani',
            password='Pavani@123'
        )

        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print("Error:", e)

    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print("Connection closed")


if __name__ == '__main__':
    connect()