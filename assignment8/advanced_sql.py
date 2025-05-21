import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("../db/lesson.db")
conn.execute("PRAGMA foreign_keys = 1")  # Enable FK constraints -- Task 3
cursor = conn.cursor()

# Task 1: Complex JOINs with Aggregation
print('--------------------TASK 1-------------------------')
# SQL query with JOIN and aggregation
query = """
SELECT 
    orders.order_id, 
    SUM(products.price * line_items.quantity) AS total_price
FROM 
    orders
JOIN 
    line_items ON orders.order_id = line_items.order_id
JOIN 
    products ON line_items.product_id = products.product_id
GROUP BY 
    orders.order_id
ORDER BY 
    orders.order_id
LIMIT 5;
"""

# Execute and fetch results
cursor.execute(query)
results = cursor.fetchall()

# Print results
print("Order ID   |       Total Price")
print("-------------------------------------")
for row in results:
    print(f"{row[0]:>8}  | ${row[1]:.2f}")

print('--------------------TASK 2-------------------------')
# --- Task 2: Average order price per customer using subquery ---
query2 = """
SELECT 
    customers.customer_name, 
    AVG(order_totals.total_price) AS average_total_price
FROM 
    customers
LEFT JOIN (
    SELECT 
        orders.customer_id AS customer_id_b,
        SUM(products.price * line_items.quantity) AS total_price
    FROM 
        orders
    JOIN 
        line_items ON orders.order_id = line_items.order_id
    JOIN 
        products ON line_items.product_id = products.product_id
    GROUP BY 
        orders.order_id
) AS order_totals
ON customers.customer_id = order_totals.customer_id_b
GROUP BY customers.customer_id;
"""

cursor.execute(query2)
results2 = cursor.fetchall()

print("Task 2: Average Order Price per Customer")
print("Customer Name       | Avg Total Price")
print("--------------------+-----------------")
for row in results2:
    name = row[0] if row[0] else "Unknown"
    avg_price = f"${row[1]:.2f}" if row[1] is not None else "N/A"
    print(f"{name:<40}| {avg_price}")
# Task 3: An Insert Transaction Based on Data
print('--------------------TASK 3-------------------------')
try:
    # Start transaction
    conn.execute("BEGIN")

    # 1. Get customer_id for "Perez and Sons"
    cursor.execute(
        "SELECT customer_id FROM customers WHERE customer_name = ?", ("Perez and Sons",))
    customer_row = cursor.fetchone()
    if not customer_row:
        raise Exception("Customer 'Perez and Sons' not found")
    customer_id = customer_row[0]

    # 2. Get employee_id for "Miranda Harris"
    cursor.execute(
        "SELECT employee_id FROM employees WHERE first_name = ? AND last_name = ?", ("Miranda", "Harris"))
    employee_row = cursor.fetchone()
    if not employee_row:
        raise Exception("Employee 'Miranda Harris' not found")
    employee_id = employee_row[0]

    # 3. Get product_ids of 5 least expensive products
    cursor.execute(
        "SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    products = cursor.fetchall()
    if len(products) < 5:
        raise Exception("Less than 5 products found")
    product_ids = [p[0] for p in products]

    # 4. Insert order record and get order_id
    cursor.execute(
        "INSERT INTO orders (customer_id, employee_id) VALUES (?, ?) RETURNING order_id",
        (customer_id, employee_id)
    )
    order_id = cursor.fetchone()[0]

    # 5. Insert 5 line_items, quantity = 10 each
    for pid in product_ids:
        cursor.execute(
            "INSERT INTO line_items (order_id, product_id, quantity) VALUES (?, ?, ?)",
            (order_id, pid, 10)
        )

    # Commit transaction
    conn.commit()

except Exception as e:
    print("Error during transaction:", e)
    conn.rollback()
    conn.close()
    exit()

# 6. Select and print inserted line items with product names
cursor.execute("""
SELECT 
    line_items.line_item_id, 
    line_items.quantity, 
    products.product_name
FROM line_items
JOIN products ON line_items.product_id = products.product_id
WHERE line_items.order_id = ?
""", (order_id,))

print("\nTask 3: Inserted line items for new order")
print("Line Item ID | Quantity | Product Name")
print("--------------------------------------")
for row in cursor.fetchall():
    print(f"{row[0]:>12} | {row[1]:>8} | {row[2]}")

# Cleanup: delete inserted line_items and order
cursor.execute("DELETE FROM line_items WHERE order_id = ?", (order_id,))
cursor.execute("DELETE FROM orders WHERE order_id = ?", (order_id,))
conn.commit()

# Task 4: Aggregation with HAVING
print('-------------------------------------------------')
print('--------------------TASK 4-------------------------')
query = """
SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
FROM employees e
JOIN orders o ON e.employee_id = o.employee_id
GROUP BY e.employee_id, e.first_name, e.last_name
HAVING COUNT(o.order_id) > 5
ORDER BY order_count DESC;
"""

cursor.execute(query)
rows = cursor.fetchall()

print("Employees with more than 5 orders:")
print("Employee ID | First Name | Last Name | Order Count")
print("--------------------------------------------------")

for row in rows:
    print(f"{row[0]:>11} | {row[1]:<10} | {row[2]:<9} | {row[3]}")
# Close the connection
conn.close()
