import sqlite3

# Connect to the database
conn = sqlite3.connect("database.db")

# Create cursor
cursor = conn.cursor()

# Get all table names
cursor.execute("""
    SELECT name
    FROM sqlite_master
    WHERE type='table';
""")

tables = cursor.fetchall()

# Print all tables
for table in tables:
    print(table[0])

# Close connection
conn.close()