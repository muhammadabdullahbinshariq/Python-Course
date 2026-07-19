import sqlite3
import pandas as pd

conn = sqlite3.connect("basketball.db")

read = pd.read_sql("""SELECT * FROM sqlite_master WHERE TYPE = 'table';""", conn)
print(read)