import sqlite3
from pathlib import Path

DB_PATH = Path("database/predictions.db")


def get_connection():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
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