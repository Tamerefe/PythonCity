import os

tables = {a: 0 for a in range(20)}

def add():
    try:
        table_no = int(input("Table No: "))
        if table_no not in tables:
            raise ValueError("Invalid table number!")
        amount_to_add = float(input("Amount to Add: "))
        tables[table_no] += amount_to_add
        print("Your transaction is complete! Press Enter to return to the main menu!")
    except ValueError as e:
        print(f"Error: {e}")
    input()

def remove():
    try:
        table_no = int(input("Table No: "))
        if table_no not in tables:
            raise ValueError("Invalid table number!")
        amount_to_remove = float(input("Amount to Remove: "))
        if tables[table_no] < amount_to_remove:
            raise ValueError("The amount to remove cannot be greater than the current amount!")
        tables[table_no] -= amount_to_remove
        print("Your transaction is complete! Press Enter to return to the main menu!")
    except ValueError as e:
        print(f"Error: {e}")
    input()

def check(file_record):
    try:
        with open(file_record) as file:
            data = file.read().splitlines()
        for i, amount in enumerate(data):
            tables[i] = float(amount)
    except FileNotFoundError:
        with open(file_record, "w") as file:
            pass
        print("First run! Record file created")

def update():
    with open("record.txt", "w") as file:
        for amount in tables.values():
            file.write(f"{amount}\n")

def show_menu():
    print("""
                    Welcome to the Restaurant Account Application

    1) View Tables
    2) Add Account
    3) Remove Account
    Q) Exit
    """)

def main():
    check("record.txt")

    while True:
        os.system("cls")
        update()
        show_menu()
        choice = input("Enter Operation Number: ").strip().lower()

        if choice == "1":
            for table, amount in tables.items():
                print(f"Account for Table {table}: {amount}")
            print("Your transaction is complete! Press Enter to return to the main menu!")
            input()
        elif choice == "2":
            add()
        elif choice == "3":
            remove()
        elif choice == "q":
            print("Program is closing")
            break
        else:
            print("Invalid choice! Press Enter to return to the main menu!")
            input()

if __name__ == "__main__":
    main()
