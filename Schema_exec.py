# extend_schema.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).with_name("accessdb.db")

def extend_schema():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    cur.executescript("""
    PRAGMA foreign_keys = ON;

    CREATE TABLE IF NOT EXISTS Roles (
      role_id   INTEGER PRIMARY KEY AUTOINCREMENT,
      role_name TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS PersonRoles (
      person_id INTEGER NOT NULL,
      role_id   INTEGER NOT NULL,
      PRIMARY KEY (person_id, role_id),
      FOREIGN KEY (person_id) REFERENCES Person(person_id),
      FOREIGN KEY (role_id)   REFERENCES Roles(role_id)
    );

    CREATE TABLE IF NOT EXISTS Buildings (
      building_id INTEGER PRIMARY KEY AUTOINCREMENT,
      name        TEXT NOT NULL UNIQUE
    );

    CREATE TABLE IF NOT EXISTS AccessPoints (
      building_id INTEGER NOT NULL,
      ap_id       INTEGER NOT NULL,   -- unique within building
      ap_name     TEXT NOT NULL,
      type        TEXT,
      PRIMARY KEY (building_id, ap_id),
      FOREIGN KEY (building_id) REFERENCES Buildings(building_id)
    );

    CREATE TABLE IF NOT EXISTS Check_in (
      check_id    INTEGER PRIMARY KEY AUTOINCREMENT,
      card_uid    INTEGER NOT NULL,
      building_id INTEGER NOT NULL,
      ap_id       INTEGER NOT NULL,
      tstamp      DATETIME DEFAULT CURRENT_TIMESTAMP,
      AccessGranted INTEGER NOT NULL,  -- 1 for granted, 0 for denied
      FOREIGN KEY (card_uid)                REFERENCES Person(card_uid),
      FOREIGN KEY (building_id, ap_id)       REFERENCES AccessPoints(building_id, ap_id)
    );
                      
    CREATE TABLE Person_bldg_access (
      card_uid   INTEGER,
      building_id INTEGER,
      PRIMARY KEY (card_uid, building_id)
    );
    """)

    conn.commit()
    conn.close()
    print("✅ Schema extended with Roles, PersonRoles, Buildings, AccessPoints, Check_in")

if __name__ == "__main__":
    extend_schema()

