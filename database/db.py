import sqlite3
from config.settings import DATABASE_PATH


def get_connection():

    conn = sqlite3.connect(DATABASE_PATH)

    conn.row_factory = sqlite3.Row

    return conn


def initialize_database():

    conn = get_connection()

    conn.execute("""
    CREATE TABLE IF NOT EXISTS predictions(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        model_name TEXT NOT NULL,
        disease_name TEXT NOT NULL,
        image_name TEXT,
        confidence REAL
    )
    """)

    conn.commit()
    conn.close()