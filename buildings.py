import sqlite3
from Schema_conn import initDb

##### Create
def createBldg(name):
    conn = initDb()
    cur = conn.cursor()
    try:
        cur.execute(
            "PRAGMA foreign_keys = ON;"
        )
        cur.execute(
            "INSERT INTO Buildings (name) VALUES (?)",
            (name,)
        )
        conn.commit()
        print(f"✅ Building added (building_id={cur.lastrowid})")
    except sqlite3.IntegrityError as e:
        print(f"⚠️ Insert failed: {e}")
    finally:
        conn.close()

##### Update

def updateBldg(building_id, name):
        conn = initDb()
        cur = conn.cursor()
        try:
            cur.execute(
                "PRAGMA foreign_keys = ON;"
            )
            cur.execute(
                "UPDATE Buildings SET name=? WHERE building_id=?",
                (name, building_id)
            )
            conn.commit()
            print(f"✅ Building updated (building_id={building_id})")
        except sqlite3.IntegrityError as e:
            print(f"⚠️ Insert failed: {e}")
        finally:
            conn.close()
##### Delete
def deleteBldg(building_id):
        conn = initDb()
        cur = conn.cursor()
        try:
            cur.execute(
                "PRAGMA foreign_keys = ON;"
            )
            cur.execute(
                "DELETE FROM Buildings WHERE building_id=?", (building_id,)
            )
            conn.commit()
            print(f"✅ Building deleted (building_id={building_id})")
        except sqlite3.IntegrityError as e:
            print(f"⚠️ Insert failed: {e}")
        finally:
            conn.close()
##### Get
def getBldg(building_id):
        conn = initDb()
        cur = conn.cursor()
        try:
            cur.execute(
                "PRAGMA foreign_keys = ON;"
            )
            #print(type(building_id))
            cur.execute(
                "SELECT * FROM Buildings WHERE building_id=?", (building_id,)
            )
            bldgrow = cur.fetchone()
            if bldgrow:
                return dict(bldgrow)
            return None
        except sqlite3.IntegrityError as e:
            print(f"⚠️ Insert failed: {e}")
        finally:
            conn.close()