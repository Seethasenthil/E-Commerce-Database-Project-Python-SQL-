import sqlite3

DB = "ecommerce_learning.db"
conn = sqlite3.connect(DB)
cursor = conn.cursor()

print("All customers:")
for row in cursor.execute("SELECT * FROM Customers"):
    print(row)

print("\nAll orders:")
for row in cursor.execute("SELECT * FROM Orders"):
    print(row)

conn.close()
