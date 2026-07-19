import sqlite3
import pandas as pd

conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS ANIMAL;
DROP TABLE IF EXISTS KEEPER;
DROP TABLE IF EXISTS ANIMAL_KEEPER;
                     
CREATE TABLE ANIMAL (
    ANIMAL_ID     INTEGER PRIMARY KEY,
    ANIMAL_NAME   TEXT,
    ANIMAL_TYPE   TEXT,
    HABITAT       TEXT,
    AGE           INTEGER,
    FOOD_KG       REAL
);

CREATE TABLE KEEPER (
    KEEPER_ID     INTEGER PRIMARY KEY,
    KEEPER_NAME   TEXT,
    COUNTRY       TEXT
);

CREATE TABLE ANIMAL_KEEPER (
    ANIMAL_ID  INTEGER,
    KEEPER_ID  INTEGER
);

INSERT INTO ANIMAL VALUES
  (1,"LEO","MAMMAL","SAVANNAH",8,7.5),
  (2,"MAYA","MAMMAL","SAVANNAH",5,6.0),
  (3,"ELLA","BIRD","RAINFOREST",4,1.5),
  (4,"RIO","BIRD","RAINFOREST",3,1.2),
  (5,"TARA","REPTILE","WETLAND",10,2.0),
  (6,"MAX","MAMMAL","FOREST",6,4.5),
  (7,"NINA","MAMMAL","FOREST",2,3.0),
  (8,"OLLIE","BIRD","WETLAND",7,1.8),
  (9,"ZARA","REPTILE","DESERT",9,2.5),
  (10,"BEN","MAMMAL","SAVANNAH",11,8.0),
  (11,"KIWI","BIRD","FOREST",5,1.4),
  (12,"REX","REPTILE","DESERT",6,2.2);

INSERT INTO KEEPER VALUES
  (1,"AARAV", "INDIA"),
  (2,"DIYA", "INDIA"),
  (3,"MEERA", "KENYA"),
  (4,"KABIR", "AUSTRALIA"),
  (5,"RIYA", "INDIA");

INSERT INTO ANIMAL_KEEPER VALUES
  (1,1),(2,1),(3,2),(4,2),(5,3),
  (6,4),(7,4),(8,3),(9,5),(10,1);
""")

conn.commit()

print("Database Ready!")

distinct = pd.read_sql("""SELECT DISTINCT (ANIMAL_TYPE) AS "ANIMAL TYPES" FROM ANIMAL;""", conn)
distinct1 = pd.read_sql("""SELECT DISTINCT (HABITAT) AS "HABITATS" FROM ANIMAL;""", conn)
print(f"\n{distinct}\n{distinct1}")

age = pd.read_sql("""SELECT * FROM ANIMAL ORDER BY AGE DESC;""", conn)
kg = pd.read_sql("""SELECT * FROM ANIMAL ORDER BY FOOD_KG;""", conn)
name = pd.read_sql("""SELECT * FROM KEEPER ORDER BY KEEPER_NAME;""", conn)
print(f"\n{age}\n{kg}\n{name}")

number = pd.read_sql("""SELECT COUNT (ANIMAL_ID) AS "NUMBER OF MAMMALS" FROM ANIMAL WHERE ANIMAL_TYPE = "MAMMAL";""", conn)
weight = pd.read_sql("""SELECT SUM (FOOD_KG) AS "WEIGHT OF FOOD" FROM ANIMAL;""", conn)
print(f"\n{number}\n{weight}")

avg_age = pd.read_sql("""SELECT AVG (AGE) FROM ANIMAL;""", conn)
avg_food = pd.read_sql("""SELECT AVG (FOOD_KG) FROM ANIMAL WHERE ANIMAL_TYPE = "MAMMAL";""", conn)
print(f"\n{avg_age}\n{avg_food}")

animal_habitat = pd.read_sql("""SELECT COUNT (ANIMAL_ID), AVG (AGE), HABITAT FROM ANIMAL GROUP BY HABITAT;""", conn)
print(f"\n{animal_habitat}")

conn.close()