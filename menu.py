def showAppMenu():
    print("\n" + "="*50)
    print("Welcome to the Building Access Application")
    print("="*50)
    
    print("\n📋 PERSON MANAGEMENT")
    print("-" * 30)
    print("1.  Create Person")
    print("2.  Get Person by ID")
    print("3.  Update Person")
    print("4.  Delete Person")
    
    print("\n🏢 BUILDING MANAGEMENT")
    print("-" * 30)
    print("5.  Create Building")
    print("6.  Get Building by ID")
    print("7.  Update Building")
    print("8.  Delete Building")
    
    print("\n🔐 ACCESS MANAGEMENT")
    print("-" * 30)
    print("9.  Check Building Access")
    print("10. Add Building Access")
    
    print("\n📊 REPORTS & UTILITIES")
    print("-" * 30)
    print("11. Generate Reports")
    print("12. Exit Application")
    print("="*50)

def returnToMenu(menu_callback, selection_callback):
    response = input("\n🔄 Return to main menu? (Y/N): ").lower()
    if response == 'y':
        menu_callback()
        selection_callback(input("\n📌 Select an option from the menu: "))

def get_input(prompt, cast_type=str):
    while True:
        try:
            val = input(prompt)
            if cast_type == int and val.strip() == "":
                print("⚠️  Please enter a number.")
                continue
            return cast_type(val)
        except ValueError:
            print(f"⚠️  Invalid input. Please enter a valid {cast_type.__name__}.")