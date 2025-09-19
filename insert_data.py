import sqlite3

DB = "ecommerce_learning.db"
conn = sqlite3.connect(DB)
cursor = conn.cursor()

# Enable foreign keys
cursor.execute("PRAGMA foreign_keys = ON")

# --- Insert Customers ---
customers = [
    (1, "Anita", "anita@example.com", "India"),
    (2, "Rahul", "rahul@example.com", "India"),
    (3, "Simi", "simi@example.com", "USA"),
    (4, "David", "david@example.com", "UK"),
    (5, "Karan", "karan@example.com", "India")
]

cursor.executemany("INSERT OR IGNORE INTO Customers VALUES (?, ?, ?, ?)", customers)

# --- Insert Products ---
products = [
    (1, "Laptop", "Electronics", 70000),
    (2, "Mouse", "Electronics", 500),
    (3, "Keyboard", "Electronics", 1500),
    (4, "Shoes", "Fashion", 2500),
    (5, "T-shirt", "Fashion", 700),
    (6, "Watch", "Accessories", 3500)
]

cursor.executemany("INSERT OR IGNORE INTO Products VALUES (?, ?, ?, ?)", products)

# --- Insert Orders ---
orders = [
    (1, 1, "2024-09-10", "Completed"),
    (2, 2, "2024-09-12", "Completed"),
    (3, 1, "2024-09-15", "Pending"),
    (4, 3, "2024-09-16", "Cancelled"),
    (5, 4, "2024-09-17", "Completed")
]

cursor.executemany("INSERT OR IGNORE INTO Orders VALUES (?, ?, ?, ?)", orders)

# --- Insert Order Items ---
order_items = [
    (1, 1, 1, 1),  # order 1 -> 1 laptop
    (2, 1, 2, 2),  # order 1 -> 2 mouse
    (3, 2, 4, 1),  # order 2 -> 1 shoes
    (4, 3, 5, 3),  # order 3 -> 3 t-shirts
    (5, 5, 6, 1),  # order 5 -> 1 watch
    (6, 5, 3, 1)   # order 5 -> 1 keyboard
]

cursor.executemany("INSERT OR IGNORE INTO Order_Items VALUES (?, ?, ?, ?)", order_items)

conn.commit()
conn.close()
print("✅ Sample data inserted successfully!")
