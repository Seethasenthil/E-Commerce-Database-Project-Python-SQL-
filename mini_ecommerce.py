import sqlite3

DB = "ecommerce_learning.db"

# Connect to database (creates file if not exists)
conn = sqlite3.connect(DB)
cursor = conn.cursor()

# Enable foreign key support
cursor.execute("PRAGMA foreign_keys = ON")

# 1. Customers Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    country TEXT
)
""")

# 2. Products Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Products (
    product_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT,
    price REAL
)
""")

# 3. Orders Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date TEXT,
    status TEXT CHECK(status IN ('Pending', 'Completed', 'Cancelled')),
    FOREIGN KEY(customer_id) REFERENCES Customers(customer_id)
)
""")

# 4. Order_Items Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Order_Items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    FOREIGN KEY(order_id) REFERENCES Orders(order_id),
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
)
""")

print("✅ Tables created successfully!")
conn.commit()
conn.close()
