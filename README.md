# E-Commerce-Database-Project-Python-SQL-
This is a **beginner-friendly project** to practice SQL and Python integration.   It simulates a small e-commerce database with `Customers`, `Products`, `Orders`, and `Order_Items` tables.
##  Project Overview

###  What I Learned:
- **Database Schema Design**
  - Creating tables with Primary Key, Foreign Key, and Constraints
- **SQL Basics**
  - SELECT, WHERE, JOIN, GROUP BY, ORDER BY
- **Data Insertion**
  - Adding sample data into multiple related tables
- **Python + SQLite Integration**
  - Running SQL queries inside Python
  - Fetching and printing results in a readable format
  📦 ecommerce-sql-project
┣ 📜 create_tables.py # Creates tables (Customers, Products, Orders, Order_Items)
┣ 📜 insert_sample_data.py # Inserts sample data into all tables
┣ 📜 learn_sql_queries.py # SELECT, JOIN, GROUP BY, ORDER BY examples
┣ 📜 ecommerce_learning.db # SQLite database file (auto-created)
┗ 📜 README.md # Project documentation


---

##  Example Queries & Outputs

- **List All Customers**
```sql
SELECT * FROM Customers;

## ORDERS WITH CUSTOMER NAME

SELECT Orders.order_id, Customers.name, Orders.status
FROM Orders
JOIN Customers ON Orders.customer_id = Customers.customer_id;

##TOP SELLING PRODUCTS

SELECT Products.name, SUM(Order_Items.quantity) AS total_qty
FROM Order_Items
JOIN Products ON Order_Items.product_id = Products.product_id
GROUP BY Products.name
ORDER BY total_qty DESC;

##HOW TO RUN THE FILES

1. python create_tables.py
2. python insert_sample_data.py
3. python learn_sql_queries.py
4. python learn_sql_queries.py
5. Open ecommerce_learning.db in DB Browser for SQLite
to explore tables visually and run custom queries.

##Key Skills Gained

**SQL Query Writing (Beginner → Intermediate)

**Relational Database Design

**Data Analysis with SQL

**Python-Database Integration (sqlite3 module)
