import sqlite3
import pandas as pd
import os

# Set the path to the lesson.db file
db_path = os.path.abspath(os.path.join("..", "db", "lesson.db"))

# Connect to the database
conn = sqlite3.connect(db_path)
# SQL query to retrieve data from line_items and products tables
query = """
SELECT 
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    products.product_name,
    products.price
FROM line_items
JOIN products ON line_items.product_id = products.product_id
"""

# Read data into DataFrame
df = pd.read_sql_query(query, conn)

# Show first 5 rows of the raw DataFrame
print("\n--- Raw Data ---")
print(df.head())

# Add a 'total' column = quantity * price
df["total"] = df["quantity"] * df["price"]

# Show first 5 rows with 'total' column
print("\n--- With Total ---")
print(df.head())

# Group by product_id and summarize
summary_df = df.groupby("product_id").agg({
    "line_item_id": "count",         # how many times ordered
    "total": "sum",                  # total price paid
    "product_name": "first"          # get product name
}).reset_index()

# Rename columns
summary_df.columns = ["product_id", "order_count",
                      "total_revenue", "product_name"]

# Sort by product_name
summary_df = summary_df.sort_values(by="product_name")

# Show first 5 rows of the summary
print("\n--- Summary ---")
print(summary_df.head())

# Write to CSV in the current (assignment7) directory
csv_file_path = os.path.join(os.path.dirname(__file__), "order_summary.csv")
summary_df.to_csv(csv_file_path, index=False)

print(f"\n✅ Summary saved to: {csv_file_path}")

# Close the DB connection
conn.close()
