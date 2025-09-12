import sqlite3
from Schema_conn import initDb

#Check if person has access to building using card_uid and log check-in
def checkAccess(card_uid, building_id):
    conn = initDb()
    cur = conn.cursor()
    # First get the person_id from card_uid
    cur.execute("SELECT person_id, first_name, last_name FROM Person WHERE card_uid=?", (card_uid,))
    person = cur.fetchone()
    
    if not person:
        conn.close()
        return print(f"❌ No person found with card UID: {card_uid}")
    
    person_id = person['person_id']
    person_name = f"{person['first_name']} {person['last_name']}"
    
    # Check access using person_id
    cur.execute("SELECT 1 FROM Person_bldg_access WHERE person_id=? AND building_id=?", (person_id, building_id))
    has_access = cur.fetchone() is not None
    
    # Set AccessGranted based on access result (1 for granted, 0 for denied)
    access_granted = 1 if has_access else 0
    
    # Log the access attempt to check_in table with AccessGranted status
    try:
        cur.execute(
            "INSERT INTO check_in (person_id, building_id, ap_id, AccessGranted) VALUES (?, ?, NULL, ?)",
            (person_id, building_id, access_granted)
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"⚠️ Warning: Could not log check-in: {e}")
    
    conn.close()
    
    if has_access:
        print(f"✅ {person_name} (Card: {card_uid}) has access to building {building_id}")
        print(f"   Access GRANTED - Check-in logged")
    else:
        print(f"❌ {person_name} (Card: {card_uid}) does NOT have access to building {building_id}")
        print(f"   Access DENIED - Attempt logged")
    

#Add access for person to building using card_uid
def addAccess(card_uid, building_id):
    conn = initDb()
    cur = conn.cursor()
    try:
        cur.execute(
            "PRAGMA foreign_keys = ON;"
        )
        
        # First get the person_id from card_uid
        cur.execute("SELECT person_id, first_name, last_name FROM Person WHERE card_uid=?", (card_uid,))
        person = cur.fetchone()
        
        if not person:
            print(f"❌ No person found with card UID: {card_uid}")
            return
        
        person_id = person['person_id']
        person_name = f"{person['first_name']} {person['last_name']}"
        
        # Add access using person_id
        cur.execute(
            "INSERT INTO Person_bldg_access (person_id, building_id) VALUES (?, ?)",
            (person_id, building_id)
        )
        conn.commit()
        print(f"✅ Access added for {person_name} (Card: {card_uid}) to building {building_id}")
    except sqlite3.IntegrityError as e:
        print(f"⚠️ Insert failed: {e}")
    finally:
        conn.close()