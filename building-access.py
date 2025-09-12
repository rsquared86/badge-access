#Badge Access Application
import sqlite3
from menu import showAppMenu, returnToMenu, get_input
from person import createPerson, updatePersonById, getPersonById, deletePersonById, showAllPersons
from Schema_conn import initDb
from buildings import createBldg, updateBldg, deleteBldg, getBldg
#from access import addBuildingAccess, checkBuildingAccess

#Display the menu on startup
showAppMenu()

#menu selection function, this will call all of our database operations
def menuSelection(menuOption):
    match menuOption:
        case "1":
            # Prompt the user for all Person fields
            card_uid   = get_input("Please type the card RFID/UID: ")
            first_name = get_input("Please type the first name: ")
            last_name  = get_input("Please type the last name: ")
            email      = get_input("Please type the email (or leave blank): ")
            if email.strip() == "":
                email = None

                # Call the function to insert into the DB
            createPerson(card_uid, first_name, last_name, email)
            returnToMenu(showAppMenu, menuSelection)
        case "2":
            #Get person id and print the person data from the db
            personId = input("Enter person id: ")
            print(getPersonById(personId))
            returnToMenu(showAppMenu, menuSelection)
        case "3":
            #update a person
            person_id = get_input("Enter the person ID to update: ", int)
            first_name = get_input("Enter the new first name: ")
            last_name = get_input("Enter the new last name: ")
            email = get_input("Enter the new email (or leave blank): ")
            if email.strip() == "":
                email = None
            updatePersonById(person_id, first_name, last_name, email)
            returnToMenu(showAppMenu, menuSelection)
        case "4":
            #delete a person
            personId = get_input("Enter the person ID to delete: ", int)
            deletePersonById(personId)
            print(f"Person with ID {personId} has been deleted.")
            returnToMenu(showAppMenu, menuSelection)
        case "5":
            #create a building
            building_name = get_input("Enter building name: ")
            #building_address = get_input("Enter building address: ")
            createBldg(building_name)
            returnToMenu(showAppMenu, menuSelection)
        case "6":
            #get building by id
            building_id = get_input("Enter building ID: ", int)
            building = getBldg(building_id)
            if building:
                print(building)
            else:
                print(f"No building found with ID {building_id}")
            returnToMenu(showAppMenu, menuSelection)
        case "7":
            #update a building
            building_id = get_input("Enter building ID to update: ", int)
            building_name = get_input("Enter new building name: ")
            #building_address = get_input("Enter new building address: ")
            updateBldg(building_id, building_name)
            returnToMenu(showAppMenu, menuSelection)
        case "8":
            #delete a building
            building_id = get_input("Enter building ID to delete: ", int)
            deleteBldg(building_id)
            returnToMenu(showAppMenu, menuSelection)
        case "9":
            #check building access
            person_id = get_input("Enter person ID: ", int)
            building_id = get_input("Enter building ID: ", int)
            #checkBuildingAccess(person_id, building_id)
            returnToMenu(showAppMenu, menuSelection)
        case "10":
            #add building access
            person_id = get_input("Enter person ID: ", int)
            building_id = get_input("Enter building ID: ", int)
            #addBuildingAccess(person_id, building_id)
            returnToMenu(showAppMenu, menuSelection)
        case "11":
            #reports menu
            print("\n**** Reports ****")
            print("1. Show all persons")
            print("2. Show all buildings")
            print("3. Show all access permissions")
            report_choice = get_input("Select report option: ")
            
            print("Invalid report option")
            returnToMenu(showAppMenu, menuSelection)
        case "12":
            #exit
            print("Thank you for using the Building Access Application. Goodbye!")
            exit()
        case _:
            print("Invalid option. Please try again.")
            returnToMenu(showAppMenu, menuSelection)
      

menuSelection(input("\n📌 Select an option from the menu: "))
