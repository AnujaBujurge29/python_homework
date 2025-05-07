import sqlite3
import os


def create_connection():
    try:
        db_path = os.path.abspath(os.path.join("..", "db", "magazines.db"))
        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = 1")
        print("Database connected successfully.")
        return conn
    except sqlite3.Error as e:
        print("Connection error:", e)
        return None


def create_tables(conn):
    try:
        cursor = conn.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS publishers (
                publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE,
                publisher_id INTEGER NOT NULL,
                FOREIGN KEY (publisher_id) REFERENCES publishers(publisher_id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscribers (
                subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                address TEXT NOT NULL,
                UNIQUE(name, address)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS subscriptions (
                subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
                subscriber_id INTEGER NOT NULL,
                magazine_id INTEGER NOT NULL,
                expiration_date TEXT NOT NULL,
                FOREIGN KEY (subscriber_id) REFERENCES subscribers(subscriber_id),
                FOREIGN KEY (magazine_id) REFERENCES magazines(magazine_id),
                UNIQUE(subscriber_id, magazine_id)
            )
        """)
        print("Tables created successfully.")
    except sqlite3.Error as e:
        print("Table creation error:", e)


def add_publisher(conn, name):
    try:
        conn.execute(
            "INSERT OR IGNORE INTO publishers (name) VALUES (?)", (name,))
    except sqlite3.Error as e:
        print("Publisher insert error:", e)


def add_magazine(conn, name, publisher_name):
    try:
        cursor = conn.cursor()
        cursor.execute(
            "SELECT publisher_id FROM publishers WHERE name = ?", (publisher_name,))
        publisher_id = cursor.fetchone()
        if publisher_id:
            conn.execute(
                "INSERT OR IGNORE INTO magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id[0]))
    except sqlite3.Error as e:
        print("Magazine insert error:", e)


def add_subscriber(conn, name, address):
    try:
        conn.execute("""
            INSERT OR IGNORE INTO subscribers (name, address)
            VALUES (?, ?)
        """, (name, address))
    except sqlite3.Error as e:
        print("Subscriber insert error:", e)


def add_subscription(conn, subscriber_name, subscriber_address, magazine_name, expiration_date):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT subscriber_id FROM subscribers WHERE name = ? AND address = ?",
                       (subscriber_name, subscriber_address))
        subscriber_id = cursor.fetchone()
        cursor.execute(
            "SELECT magazine_id FROM magazines WHERE name = ?", (magazine_name,))
        magazine_id = cursor.fetchone()
        if subscriber_id and magazine_id:
            conn.execute("""
                INSERT OR IGNORE INTO subscriptions (subscriber_id, magazine_id, expiration_date)
                VALUES (?, ?, ?)
            """, (subscriber_id[0], magazine_id[0], expiration_date))
    except sqlite3.Error as e:
        print("Subscription insert error:", e)


def run_queries(conn):
    try:
        print("\nAll Subscribers:")
        for row in conn.execute("SELECT * FROM subscribers"):
            print(row)

        print("\nMagazines sorted by name:")
        for row in conn.execute("SELECT * FROM magazines ORDER BY name"):
            print(row)

        print("\nMagazines by publisher 'Penguin':")
        query = """
        SELECT magazines.name 
        FROM magazines
        JOIN publishers ON magazines.publisher_id = publishers.publisher_id
        WHERE publishers.name = ?
        """
        for row in conn.execute(query, ("Penguin",)):
            print(row)

    except sqlite3.Error as e:
        print("Query execution error:", e)


if __name__ == "__main__":
    conn = create_connection()
    if conn:
        create_tables(conn)

        # Populate data
        publishers = ["Penguin", "HarperCollins", "Condé Nast"]
        for name in publishers:
            add_publisher(conn, name)

        add_magazine(conn, "Tech Today", "Penguin")
        add_magazine(conn, "Science Weekly", "Penguin")
        add_magazine(conn, "Literary Digest", "HarperCollins")

        add_subscriber(conn, "Alice", "123 Main St")
        add_subscriber(conn, "Bob", "456 Maple Ave")
        add_subscriber(conn, "Charlie", "789 Elm St")

        add_subscription(conn, "Alice", "123 Main St",
                         "Tech Today", "2025-12-31")
        add_subscription(conn, "Bob", "456 Maple Ave",
                         "Science Weekly", "2025-11-30")
        add_subscription(conn, "Charlie", "789 Elm St",
                         "Literary Digest", "2026-01-15")

        conn.commit()

        run_queries(conn)

        conn.close()
        print("Connection closed.")
