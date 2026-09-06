import sqlite3
import pandas as pd

# 1. Connect (creates the file if it doesn't exist)
conn = sqlite3.connect("sports_team.db")
cursor = conn.cursor()

# 2. Create the table with constraints
cursor.execute("DROP TABLE IF EXISTS players")   # clean start
cursor.execute("""
CREATE TABLE players (
    player_id     INTEGER PRIMARY KEY,
    name          TEXT    NOT NULL,
    jersey_number INTEGER UNIQUE,
    position      TEXT    NOT NULL,
    team          TEXT    DEFAULT 'Free Agent',
    age           INTEGER,
    goals         INTEGER DEFAULT 0
)
""")

# 3. Insert valid records
valid_players = [
    (1, "Alex Rivera", 10, "Forward", "Thunder FC", 24, 12),
    (2, "Jordan Lee", 7, "Midfielder", "Thunder FC", 22, 5),
    (3, "Sam Patel", 1, "Goalkeeper", None, 28, 0),   # team will become 'Free Agent'
    (4, "Taylor Kim", 9, "Forward", "Lightning United", None, 8)  # age is NULL
]

cursor.executemany("""
INSERT INTO players (player_id, name, jersey_number, position, team, age, goals)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", valid_players)

conn.commit()

# 4. Demonstrate DEFAULT and NULL
print("\n--- Current table contents ---")
df = pd.read_sql_query("SELECT * FROM players", conn)
print(df)

# 5. Test invalid inserts safely (this is what the assignment asks for)
print("\n--- Testing invalid inserts ---")

def try_insert(description, sql, params=None):
    try:
        if params:
            cursor.execute(sql, params)
        else:
            cursor.execute(sql)
        conn.commit()
        print(f"check {description} — unexpectedly succeeded")
    except sqlite3.IntegrityError as e:
        print(f"X {description} — correctly rejected: {e}")

# Missing required NOT NULL column
try_insert(
    "Insert without name (NOT NULL violation)",
    "INSERT INTO players (player_id, jersey_number, position) VALUES (5, 11, 'Defender')"
)

# Duplicate jersey number (UNIQUE violation)
try_insert(
    "Insert with duplicate jersey number",
    "INSERT INTO players (player_id, name, jersey_number, position) VALUES (6, 'Chris Wong', 10, 'Midfielder')"
)

# Duplicate primary key
try_insert(
    "Insert with existing player_id",
    "INSERT INTO players (player_id, name, jersey_number, position) VALUES (1, 'Duplicate ID', 99, 'Forward')"
)

# 6. Final view
print("\n--- Final table after failed inserts ---")
df_final = pd.read_sql_query("SELECT * FROM players", conn)
print(df_final)

conn.close()
print("\nDatabase closed. File: sports_team.db")