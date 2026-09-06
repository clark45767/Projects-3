import sqlite3
import pandas as pd

# 1. Connect to (or create) the database
conn = sqlite3.connect("wildlife_park.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS animals (
    animal_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    species TEXT NOT NULL,
    habitat TEXT NOT NULL,
    age INTEGER,
    weight_kg REAL,
    arrival_date TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS habitats (
    habitat_id INTEGER PRIMARY KEY,
    habitat_name TEXT UNIQUE,
    climate TEXT,
    size_hectares REAL
)
""")

conn.commit()

animals_data = [
    (1, "Leo", "Lion", "Savanna", 8, 190.5, "2021-03-15"),
    (2, "Ellie", "Elephant", "Savanna", 12, 4200.0, "2019-07-22"),
    (3, "Zara", "Zebra", "Savanna", 5, 320.0, "2022-01-10"),
    (4, "Penny", "Penguin", "Arctic", 4, 25.0, "2020-11-05"),
    (5, "Kiki", "Koala", "Forest", 6, 9.5, "2021-09-18"),
    (6, "Max", "Meerkat", "Desert", 3, 1.2, "2023-02-14"),
    (7, "Bella", "Bear", "Forest", 9, 280.0, "2018-05-30"),
    (8, "Sunny", "Snake", "Desert", 2, 4.8, "2023-06-01"),
    (9, "Frost", "Penguin", "Arctic", 5, 28.0, "2020-12-12"),
    (10, "Gina", "Giraffe", "Savanna", 7, 1100.0, "2021-04-20"),
]

cursor.executemany("""
INSERT OR REPLACE INTO animals 
(animal_id, name, species, habitat, age, weight_kg, arrival_date)
VALUES (?, ?, ?, ?, ?, ?, ?)
""", animals_data)

conn.commit()

# 1. DISTINCT – unique habitats
unique_habitats = pd.read_sql_query(
    "SELECT DISTINCT habitat FROM animals ORDER BY habitat", conn)
print("Unique habitats:")
print(unique_habitats)

# 2. ORDER BY – animals sorted by weight (descending)
sorted_by_weight = pd.read_sql_query(
    "SELECT name, species, weight_kg FROM animals ORDER BY weight_kg DESC", conn)
print("\nAnimals sorted by weight (heaviest first):")
print(sorted_by_weight)

# 3. COUNT() and SUM()
counts = pd.read_sql_query("""
SELECT 
    COUNT(*) AS total_animals,
    SUM(weight_kg) AS total_weight_kg
FROM animals
""", conn)
print("\nTotal animals and total weight:")
print(counts)

# 4. AVG()
avg_age = pd.read_sql_query(
    "SELECT AVG(age) AS average_age FROM animals", conn)
print("\nAverage age of animals:")
print(avg_age)

# 5. GROUP BY – animals grouped by habitat
by_habitat = pd.read_sql_query("""
SELECT 
    habitat,
    COUNT(*) AS animal_count,
    AVG(age) AS avg_age,
    AVG(weight_kg) AS avg_weight,
    SUM(weight_kg) AS total_weight
FROM animals
GROUP BY habitat
ORDER BY animal_count DESC
""", conn)
print("\nSummary by habitat:")
print(by_habitat)