from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).with_name("accessdb.db")

def initDb():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # This allows accessing columns by name
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn