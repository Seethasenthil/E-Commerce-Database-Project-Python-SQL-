import sqlite3
from pprint import pprint

DB = "ecommerce_learning.db"
conn = sqlite3.connect(DB)
cursor = conn.cursor()

print("🔹 1) SELECT - Get all customers")
cursor.execute("SELECT * FROM Customers")
for row in cursor.fetchall():
    pprint(row)

print("\n🔹 2) WHERE - Customers from India only")
cursor.execute("SELECT name, country FROM Customers WHERE country = 'India'")
for row in cursor.fetchall():
    pprint(row)

print("\n🔹 3) JOIN - Get orders with customer names")
cursor.execute("""
SELECT Orders.order_id, Customers.name, Orders.order_date, Orders.status
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
""")
for row in cursor.fetchall():
    pprint(row)

print("\n🔹 4) JOIN Multiple Tables - Show product names with order_id")
cursor.execute("""
SELECT Orders.order_id, Customers.name AS customer, Products.name AS product, Order_Items.quantity
FROM Order_Items
JOIN Orders ON Order_Items.order_id = Orders.order_id
JOIN Customers ON Orders.customer_id = Customers.customer_id
JOIN Products ON Order_Items.product_id = Products.product_id
ORDER BY Orders.order_id
""")
for row in cursor.fetchall():
    pprint(row)

print("\n🔹 5) GROUP BY - Total quantity sold per product")
cursor.execute("""
SELECT Products.name, SUM(Order_Items.quantity) AS total_qty
FROM Order_Items
JOIN Products ON Order_Items.product_id = Products.product_id
GROUP BY Products.name
ORDER BY total_qty DESC
""")
for row in cursor.fetchall():
    pprint(row)

print("\n🔹 6) GROUP BY - Total orders per customer (only completed orders)")
cursor.execute("""
SELECT Customers.name, COUNT(Orders.order_id) AS completed_orders
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id
WHERE Orders.status = 'Completed'
GROUP BY Customers.name
ORDER BY completed_orders DESC
""")
for row in cursor.fetchall():
    pprint(row)

conn.close()
