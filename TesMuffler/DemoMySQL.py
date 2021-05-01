import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="HamRadio@3",
    database="db1"              # Will cause error if db doesn't exist
)

# Print memory location connector object
print(mydb)

mycursor = mydb.cursor()

# Create a new database
#mycursor.execute("CREATE DATABASE db1")

# Determin if a database exists
#mycursor.execute("SHOW DATABASES")

# Create TABLE inside a database
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)



