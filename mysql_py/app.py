# import mysql.connector as dbconnection

# # Step 1: Create connection
# myconnection = dbconnection.connect(
#     host="localhost",
#     user="pavani",
#     password="Pavani@123",
#     database="classicmodels"
# )

# # Step 2: Get a cursor
# cursor = myconnection.cursor()

# # Step 3: Define SQL query
# SQLQuery = """
# SELECT 
#     ordernumber, 
#     SUM(quantityOrdered) AS itemsCount, 
#     SUM(priceeach * quantityOrdered) AS total
# FROM orderdetails
# GROUP BY ordernumber
# HAVING total > 1000 AND itemsCount > 600
# """
# # Step 4: Execute
# cursor.execute(SQLQuery)

# # Step 5: Fetch results
# records = cursor.fetchall()

# print("Total number of rows returned:", cursor.rowcount)
# print("\nPrinting each row\n")

# for row in records:
#     print("order number =", row[0])
#     print("item counts =", row[1])
#     print("total =", row[2], "\n")

# # Step 6: Close everything
# cursor.close()
# myconnection.close()


# import mysql.connector as dbconnect
# from mysql.connector import Error

# myconnection = None
# cursor = None

# try:
#     myconnection = dbconnect.connect(
#         host='localhost',
#         database='classicmodels',
#         user='pavani',
#         password='Pavani@123'
#     )

#     if myconnection.is_connected():
#         print("Successfully Connected to MySQL database")

#         cursor = myconnection.cursor()

#         SQLQuery = """
#         SELECT ordernumber,
#                SUM(quantityOrdered) AS itemsCount,
#                SUM(priceeach * quantityOrdered) AS total
#         FROM orderdetails
#         GROUP BY ordernumber
#         HAVING total > 1000 AND itemsCount > 600
#         """

#         cursor.execute(SQLQuery)
#         records = cursor.fetchall()

#         print("Total number of rows returned:", cursor.rowcount)
#         print("\nPrinting each row\n")

#         for row in records:
#             print("order number =", row[0])
#             print("item counts =", row[1])
#             print("total =", row[2], "\n")

# except Error as e:
#     print("Error while connecting to Database:", e)

# finally:
#     if cursor is not None:
#         cursor.close()
#     if myconnection is not None and myconnection.is_connected():
#         myconnection.close()
#     print("Database connection is closed")


