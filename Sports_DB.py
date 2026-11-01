import sqlite3
import pandas as pd

connection = sqlite3.connect(":memory:")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE players (
    player_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    jersey_number INTEGER UNIQUE,
    position TEXT DEFAULT 'Unassigned',
    points_scored INTEGER DEFAULT 0 CHECK (points_scored >= 0)
);
""")
connection.commit()

valid_players = [
    ("Alice Smith", 10, "Forward", 25),
    ("Bob Jones", 23, "Guard", 18),
    ("Charlie Brown", 5, "Center", 0)
]

cursor.executemany("""
INSERT INTO players (name, jersey_number, position, points_scored)
VALUES (?, ?, ?, ?);
""", valid_players)
connection.commit()

cursor.execute("""
INSERT INTO players (name, jersey_number)
VALUES ('Diana Prince', 7);
""")
connection.commit()

def test_insert(description, query, params=()):
    try:
        cursor.execute(query, params)
        connection.commit()
        print(f"Success: {description}")
    except sqlite3.Error as e:
        print(f"Caught Expected Error ({description}): {e}")

print("--- Testing SQL Constraints Safely ---")

test_insert(
    "Missing NOT NULL Name", 
    "INSERT INTO players (jersey_number) VALUES (99);"
)

test_insert(
    "Duplicate UNIQUE Jersey Number", 
    "INSERT INTO players (name, jersey_number) VALUES ('Evan Wright', 10);"
)

test_insert(
    "Violating CHECK Constraint (Negative Points)", 
    "INSERT INTO players (name, jersey_number, points_scored) VALUES ('Frank Miller', 14, -5);"
)

print("\n--- Database Content via Pandas ---")
df = pd.read_sql_query("SELECT * FROM players;", connection)
print(df)

connection.close()