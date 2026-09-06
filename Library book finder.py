import sqlite3
import pandas as pd

# Connect to SQLite database
conn = sqlite3.connect("library.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY,
    title TEXT,
    author TEXT,
    price REAL
)
""")

# Add books
books = [
    (1, "Harry Potter", "J.K. Rowling", 25.00),
    (2, "The Hobbit", "J.R.R. Tolkien", 20.00),
    (3, "Python Basics", "John Smith", 30.00),
    (4, "Data Science", "Jane Doe", 35.00)
]

cursor.executemany(
    "INSERT OR IGNORE INTO books VALUES (?, ?, ?, ?)", books
)

# 1. Display all books
print("ALL BOOKS")
print(pd.read_sql("SELECT * FROM books", conn))

# 2. Filter books by price
print("\nBOOKS ABOVE 25")
print(pd.read_sql(
    "SELECT * FROM books WHERE price > 25", conn
))

# 3. Search titles using LIKE
print("\nBOOKS WITH 'Python' IN TITLE")
print(pd.read_sql(
    "SELECT * FROM books WHERE title LIKE '%Python%'", conn
))

# 4. Find minimum and maximum price
print("\nMINIMUM AND MAXIMUM PRICE")
print(pd.read_sql(
    "SELECT MIN(price) AS Minimum, MAX(price) AS Maximum FROM books",
    conn
))

conn.commit()
conn.close()