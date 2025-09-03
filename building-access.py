#Badge Access Application
import sqlite3
#Sql lite
#brew install sqlite if you don't have it on your machine 
#Connect to db so we only have to define the db name once
#make sure you close the connection after every init call though
def initDb():
    #Name this 'building_access.db' whatever your database is you created
    dbConnection = sqlite3.connect('building_access.db')
    return dbConnection

#TODO: Create a Person
def createPerson(name, email, major):
    dbConnection = initDb()
    cursor = dbConnection.cursor()
    #TODO: Update insert to insert appropriate entity values
    cursor.execute("INSERT INTO Person (name, email, major) VALUES (?, ?, ?)", (name, email, major))
    dbConnection.commit()
    dbConnection.close()

#Update a Person
#TODO: Add all attributes for the entity
def updatePersonById(id, name, email, major):
    dbConnection = initDb()
    cursor = dbConnection.cursor()
    cursor.execute("UPDATE Person SET name=?, email=?, major=? WHERE id=?", (name, email, major, id))
    dbConnection.commit()
    dbConnection.close()

#Get a Person by ID
def getPersonById(id):
    dbConnection = initDb()
    cursor = dbConnection.cursor()
    cursor.execute("SELECT * FROM Person WHERE id=?", (id,))
    person = cursor.fetchone()
    dbConnection.close()
    return person


#TODO: Delete a Person
def deletePersonById(id):
    dbConnection = initDb()
    cursor = dbConnection.cursor()
    cursor.execute("DELETE FROM Person WHERE id=?", (id,))
    dbConnection.commit()
    dbConnection.close()

#TODO: Create a Building

#TODO: Update a Building

#TODO: Delete a Building

#TODO: Get a Building by ID


#Add Building Access
def addBuildingAccess(personId, buildingId):
    dbConnection = initDb()
    cursor = dbConnection.cursor()
    cursor.execute("INSERT INTO PersonBuildingAccess (person_id, building_id) VALUES (?, ?)", (personId, buildingId))
    dbConnection.commit()
    dbConnection.close()

#Check Building Access by Person ID
def checkBuildingAccess(personId, buildingId):
    dbConnection = initDb()
    cursor = dbConnection.cursor()
    cursor.execute("""
        SELECT * FROM PersonBuildingAccess 
       WHERE person_id=? AND building_id=?
    """, (personId, buildingId))
    access = cursor.fetchone()
    if access:
        print(f"Person {personId} has access to building {buildingId}.")
    else:
        print(f"Person {personId} does not have access to building {buildingId}.")
    dbConnection.close()

#App Menu
def showAppMenu():
    print("Welcome to the Building Access Application")
    print("1. Create Person")
    print("2. Get Person by ID")
    print("3. Check Building Access")
    print("4. Add Building Access")
    print("5. Exit")

#Call this any time we want the user to have the option to return to the main menu
def returnToMenu():
    if input("Return to main menu? Y or N").lower() == 'y':
        showAppMenu()
        menuSelection(input("Select an option from the menu : "))

showAppMenu()

#menu selection function, this will call all of our database operations
def menuSelection(menuOption):
    match menuOption:
        case "1":
            #TODO: Create a person input and function call
            pass #Remove once todo is done
        case "2":
            #Get person id and print the person data from the db
            personId = input("Enter person id: ")
            print(getPersonById(personId))
            returnToMenu()
        case "3":
            #Check Building Access
            personId = input("Enter person id: ")
            buildingId = input("Enter building id: ")
            checkBuildingAccess(personId, buildingId)
            returnToMenu()
        case "4":
            #TODO: Add building Access
            pass #remove once TODO is done
        case "5":
            print("Exiting application.")
            exit()
        case _:
            print("Invalid option. Please try again.")


menuSelection(input("Select an option from the menu : "))
