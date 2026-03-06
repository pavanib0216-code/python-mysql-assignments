import requests
import mysql.connector as dbconnect

# ------------------------------
# Fetch data from API
# ------------------------------
def fetch_posts():
    url = "https://jsonplaceholder.typicode.com/posts/"
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Failed to fetch data")
        return None


# ------------------------------
# Load API data into MySQL
# ------------------------------
def load_to_mysql(data):

    conn = dbconnect.connect(
        host="localhost",
        port="3306",
        user="pavani",
        password="Pavani@123",
        database="classicmodels"
    )

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INT PRIMARY KEY,
            userId INT,
            title VARCHAR(255),
            body TEXT
        )
    """)

    for post in data:
        cursor.execute("""
            INSERT INTO posts (id, userId, title, body)
            VALUES (%s, %s, %s, %s)
        """, (post['id'], post['userId'], post['title'], post['body']))

    conn.commit()
    cursor.close()
    conn.close()

    print("Data loaded successfully to MySQL database")


# ------------------------------
# Fetch data from MySQL
# ------------------------------
def fetch_from_mysql():

    conn = dbconnect.connect(
        host="localhost",
        port="3306",
        user="pavani",
        password="Pavani@123",
        database="classicmodels"
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM posts")

    records = cursor.fetchall()

    print("Total rows:", cursor.rowcount)

    for row in records[:5]:
        print(row)

    cursor.close()
    conn.close()


# ------------------------------
# Main Execution
# ------------------------------
posts_data = fetch_posts()

if posts_data:
    load_to_mysql(posts_data)
    fetch_from_mysql()