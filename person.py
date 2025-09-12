import sqlite3
from Schema_conn import initDb

def createPerson(card_uid, first_name, last_name, email):
    conn = initDb()
    cur = conn.cursor()
    try:
        cur.execute(
            "PRAGMA foreign_keys = ON;"
        )
        cur.execute(
            "INSERT INTO Person (card_uid, first_name, last_name, email) VALUES (?, ?, ?, ?)",
            (card_uid, first_name, last_name, email or None)
        )
        conn.commit()
        print(f"✅ Person added (person_id={cur.lastrowid})")
    except sqlite3.IntegrityError as e:
        print(f"⚠️ Insert failed: {e}")
    finally:
        conn.close()

def updatePersonByCardUID(card_uid, first_name, last_name, email):
    conn = initDb()
    cur = conn.cursor()
    cur.execute("UPDATE Person SET first_name=?, last_name=?, email=? WHERE card_uid=?", 
                (first_name, last_name, email, card_uid))
    conn.commit()
    if cur.rowcount > 0:
        print(f"✅ Person with card {card_uid} updated successfully")
    else:
        print(f"⚠️ No person found with card UID {card_uid}")
    conn.close()

def updatePersonById(person_id, first_name, last_name, email):
    conn = initDb()
    cur = conn.cursor()
    cur.execute("UPDATE Person SET first_name=?, last_name=?, email=? WHERE person_id=?", 
                (first_name, last_name, email, person_id))
    conn.commit()
    if cur.rowcount > 0:
        print(f"✅ Person {person_id} updated successfully")
    else:
        print(f"⚠️ No person found with ID {person_id}")
    conn.close()

def getPersonByCardUID(card_uid):
    conn = initDb()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Person WHERE card_uid=?", (card_uid,))
    person = cur.fetchone()
    person = dict(person) if person else None
    conn.close()
    return person

def getPersonById(person_id):
    conn = initDb()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Person WHERE person_id=?", (person_id,))
    person = cur.fetchone()
    person = dict(person) if person else None
    conn.close()
    return person

def deletePersonByCardUID(card_uid):
    conn = initDb()
    cur = conn.cursor()
    # First get person details for confirmation
    cur.execute("SELECT first_name, last_name FROM Person WHERE card_uid=?", (card_uid,))
    person = cur.fetchone()
    
    if person:
        person_name = f"{person['first_name']} {person['last_name']}"
        cur.execute("DELETE FROM Person WHERE card_uid=?", (card_uid,))
        conn.commit()
        print(f"✅ {person_name} (Card: {card_uid}) deleted successfully")
    else:
        print(f"⚠️ No person found with card UID {card_uid}")
    conn.close()

def deletePersonById(person_id):
    conn = initDb()
    cur = conn.cursor()
    cur.execute("DELETE FROM Person WHERE person_id=?", (person_id,))
    conn.commit()
    if cur.rowcount > 0:
        print(f"✅ Person {person_id} deleted successfully")
    else:
        print(f"⚠️ No person found with ID {person_id}")
    conn.close()

def showAllPersons():
    conn = initDb()
    cur = conn.cursor()
    cur.execute("SELECT * FROM Person")
    rows = cur.fetchall()
    if not rows:
        print("(no persons found)")
    else:
        print("\n📋 All Persons:")
        print("-" * 80)
        for row in rows:
            person = dict(row)
            print(f"ID: {person['person_id']} | Name: {person['first_name']} {person['last_name']} | Card: {person['card_uid']} | Email: {person.get('email', 'N/A')}")
    conn.close()