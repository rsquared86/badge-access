#Badge Access Application
import sqlite3
from menu import showAppMenu, returnToMenu, get_input
from person import createPerson, updatePersonByCardUID, getPersonByCardUID, deletePersonByCardUID, showAllPersons
from Schema_conn import initDb
from buildings import createBldg, updateBldg, deleteBldg, getBldg
from access import checkAccess, addAccess
from reports import denial_report, most_checkins_by_building, most_checkins_by_date, most_checkins_by_date_with_prompt, most_checkins_by_building_with_prompt, denial_report_with_prompt
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
            #Get person by card UID and print the person data from the db
            card_uid = get_input("Enter card UID: ")
            person = getPersonByCardUID(card_uid)
            if person:
                print(person)
            else:
                print(f"No person found with card UID {card_uid}")
            returnToMenu(showAppMenu, menuSelection)
        case "3":
            #update a person
            card_uid = get_input("Enter the card UID to update: ")
            first_name = get_input("Enter the new first name: ")
            last_name = get_input("Enter the new last name: ")
            email = get_input("Enter the new email (or leave blank): ")
            if email.strip() == "":
                email = None
            updatePersonByCardUID(card_uid, first_name, last_name, email)
            returnToMenu(showAppMenu, menuSelection)
        case "4":
            #delete a person
            card_uid = get_input("Enter the card UID to delete: ")
            deletePersonByCardUID(card_uid)
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
            card_uid = get_input("Enter card UID: ")
            building_id = get_input("Enter building ID: ", int)
            checkAccess(card_uid, building_id)
            returnToMenu(showAppMenu, menuSelection)
        case "10":
            #add building access
            card_uid = get_input("Enter card UID: ")
            building_id = get_input("Enter building ID: ", int)
            addAccess(card_uid, building_id)
            returnToMenu(showAppMenu, menuSelection)
        case "11":
            #reports menu
            print("\n**** Reports ****")
            print("1. Most Checkins by Date")
            print("2. Most Checkins by Building")
            print("3. Denial Report")
            report_choice = get_input("Select report option: ")

            match report_choice:
                case "1":
                    most_checkins_by_date_with_prompt()
                    returnToMenu(showAppMenu, menuSelection)
                case "2":
                    most_checkins_by_building_with_prompt()
                    returnToMenu(showAppMenu, menuSelection)
                case "3":
                    denial_report_with_prompt()
                    returnToMenu(showAppMenu, menuSelection)
                case _:
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
