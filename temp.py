import sqlite3

conn = sqlite3.connect("database/predictions.db")

cursor = conn.execute("SELECT * FROM predictions")

print(cursor.fetchall())

conn.close()