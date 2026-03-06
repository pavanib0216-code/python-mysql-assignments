import mysql.connector
from mysql.connector import Error

# ---------------------------------------------------
# 1. CREATE DATABASE
# ---------------------------------------------------
def create_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='pavani',
            password='Pavani@123'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS RegistrationDB")
            print("Database 'RegistrationDB' created successfully!")

    except Error as e:
        print("Error while creating database:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# ---------------------------------------------------
# DATABASE CONNECTION FUNCTION
# ---------------------------------------------------
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='pavani',
        password='Pavani@123',
        database='RegistrationDB'
    )


# ---------------------------------------------------
# 2. CREATE USER TABLE + INSERT INITIAL USERS
# ---------------------------------------------------
def generate_user_table():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                email VARCHAR(100) PRIMARY KEY,
                name VARCHAR(50),
                password VARCHAR(30)
            )
        """)

        connection.commit()
        print("Users table created successfully.")

        insert_query = """
        INSERT IGNORE INTO Users (email, name, password)
        VALUES (%s, %s, %s)
        """

        users = [
            ('ywbaek@perscholas.org', 'young', 'letsgomets'),
            ('mcordon@perscholas.org', 'marcial', 'perscholas'),
            ('mhaseeb@perscholas.org', 'haseeb', 'platform')
        ]

        cursor.executemany(insert_query, users)
        connection.commit()

        print("Initial users inserted successfully.")

    except Error as e:
        print("Error:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# ---------------------------------------------------
# 3. GET ALL USERS
# ---------------------------------------------------
def get_all_users():
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT email, name, password FROM Users")
        users = cursor.fetchall()

        print("\nAll Users:")
        for email, name, password in users:
            print(f"Email: {email}, Name: {name}, Password: {password}")

        return users

    except Error as e:
        print("Error:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# ---------------------------------------------------
# 4. GET USER BY NAME
# ---------------------------------------------------
def get_user_by_name(name):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT email, password FROM Users WHERE name = %s"
        cursor.execute(query, (name,))
        user = cursor.fetchone()

        if user:
            print(f"\nUser found → Email: {user[0]}, Password: {user[1]}")
        else:
            print("\nNo user found with that name.")

        return user

    except Error as e:
        print("Error:", e)

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# ---------------------------------------------------
# 5. VALIDATE USER LOGIN
# ---------------------------------------------------
def validate_user(email, password):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = "SELECT * FROM Users WHERE email = %s AND password = %s"
        cursor.execute(query, (email, password))

        user = cursor.fetchone()

        if user:
            return True
        else:
            return False

    except Error as e:
        print("Error:", e)
        return False

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# ---------------------------------------------------
# 6. UPDATE USER
# ---------------------------------------------------
def update_user(email, name, password):
    connection = None
    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
        UPDATE Users
        SET name = %s, password = %s
        WHERE email = %s
        """

        cursor.execute(query, (name, password, email))
        connection.commit()

        if cursor.rowcount > 0:
            print("\nUser updated successfully.")
            return True
        else:
            print("\nNo user found with that email.")
            return False

    except Error as e:
        print("Error:", e)
        return False

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()


# ---------------------------------------------------
# TESTING ALL FUNCTIONS
# ---------------------------------------------------
if __name__ == "__main__":

    print("\n--- Creating Database ---")
    create_database()

    print("\n--- Generating User Table ---")
    generate_user_table()

    print("\n--- Getting All Users ---")
    get_all_users()

    print("\n--- Getting User by Name (young) ---")
    get_user_by_name("young")

    print("\n--- Validating User Login ---")
    print("Login valid?", validate_user("ywbaek@perscholas.org", "letsgomets"))

    print("\n--- Updating User ---")
    update_user("ywbaek@perscholas.org", "young_updated", "newpass123")

    print("\n--- Users After Update ---")
    get_all_users()