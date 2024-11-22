def display_menu():
    print("1. View Directory")
    print("2. Add Contact")
    print("3. Delete Contact")
    print("4. Update Contact")
    print("5. Exit")

def display_directory(directory):
    for contact, details in directory.items():
        print(f"Contact: {contact}")
        for type, number in details.items():
            print(f"  {type}: {number}")

def add_contact(directory):
    contact = input("New Contact Name: ")
    mobile = input("Mobile Phone: ")
    work = input("Work Phone: ")
    home = input("Home Phone: ")
    directory[contact] = {"Mobile": mobile, "Work": work, "Home": home}
    print(f"{contact} added to the directory.")

def delete_contact(directory):
    contact = input("Name of Contact to Delete: ")
    if contact in directory:
        del directory[contact]
        print(f"{contact} deleted from the directory.")
    else:
        print("Contact Not Found!")

def update_contact(directory):
    contact = input("Name of Contact to Update: ")
    if contact in directory:
        mobile = input("New Mobile Phone: ")
        work = input("New Work Phone: ")
        home = input("New Home Phone: ")
        directory[contact] = {"Mobile": mobile, "Work": work, "Home": home}
        print(f"{contact}'s information updated.")
    else:
        print("Contact Not Found!")

directory = {
    "contact1": {"Mobile": "2141522511615215", "Work": "12515215235217598", "Home": "876855674596807675"},
    "contact2": {"Mobile": "798654765654436", "Work": "7869457433453423", "Home": "5436754748645363"}
}

while True:
    display_menu()
    choice = input("Your Choice: ")

    if choice == "1":
        display_directory(directory)
    elif choice == "2":
        add_contact(directory)
    elif choice == "3":
        delete_contact(directory)
    elif choice == "4":
        update_contact(directory)
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice, please try again.")

    input("Press Enter to Return to Main Menu")
