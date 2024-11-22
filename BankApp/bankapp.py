import os

class Customer():
    def __init__(self, ID, PASSWORD, NAME):
        self.id = ID
        self.password = PASSWORD
        self.name = NAME
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return True
        else:
            return False

class Bank():
    def __init__(self):
        self.customers = list()

    def register_customer(self, ID, PASSWORD, NAME):
        self.customers.append(Customer(ID, PASSWORD, NAME))
        print("Welcome to our Internet Banking")

    def find_customer(self, ID):
        for customer in self.customers:
            if customer.id == ID:
                return customer
        return None

def main_menu():
    os.system("cls")
    print("""

                    Welcome to Dolliet's Mint-Looking Bank $

    1) I am a Customer
    2) I Want to Become a Customer

    """)

def customer_menu(customer):
    while True:
        os.system("cls")
        print("                                 Welcome Mr/Ms {}".format(customer.name))
        print("""

        1) Check Balance
        2) Deposit Money [To Own Account]
        3) Deposit Money [To Another Account]
        4) Withdraw Money
        Q) Exit

        """)
        choice = input("Enter Transaction Number: ")

        if choice == "1":
            print("Your Balance: {}".format(customer.balance))
            input("Press Enter to Return to Main Menu!")

        elif choice == "2":
            amount = int(input("Amount: "))
            confirmation = input("Do you confirm depositing {} TL to your own account? Y/N\n".format(amount))
            if confirmation.lower() == "y":
                customer.deposit(amount)
                print("Your money has been deposited!")
            else:
                print("Transaction Cancelled")
            input("Press Enter to Return to Main Menu")

        elif choice == "3":
            target_id = input("Customer ID: ")
            target_customer = bank.find_customer(target_id)
            if target_customer:
                amount = int(input("Amount: "))
                if amount <= customer.balance:
                    confirmation = input("Do you confirm depositing {} TL to {}'s account? Y/N\n".format(amount, target_customer.name))
                    if confirmation.lower() == "y":
                        customer.withdraw(amount)
                        target_customer.deposit(amount)
                        print("Money Transferred!")
                    else:
                        print("Transaction Cancelled")
                else:
                    print("Insufficient Balance, Transaction Cancelled")
            else:
                print("Customer Not Found")
            input("Press Enter to Return to Main Menu")

        elif choice == "4":
            amount = int(input("Amount: "))
            if customer.withdraw(amount):
                print("Transaction Completed, Please Take Your Money")
            else:
                print("Insufficient Balance, Transaction Cancelled")
            input("Press Enter to Return to Main Menu")

        elif choice.lower() == "q":
            break

        else:
            print("Invalid Choice, Please Try Again")
            input("Press Enter to Return to Main Menu")

bank = Bank()

while True:
    main_menu()
    try:
        choice = int(input("Your Choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        ID = input("ID: ")
        customer = bank.find_customer(ID)
        if customer:
            password = input("Enter Your Password: ")
            if password == customer.password:
                customer_menu(customer)
            else:
                print("Incorrect Password")
                input("Press Enter to Return to Main Menu")
        else:
            print("Customer Not Found")
            input("Press Enter to Return to Main Menu")

    elif choice == 2:
        ID = input("Enter ID: ")
        NAME = input("Enter Name: ")
        PASSWORD = input("Enter Password: ")
        bank.register_customer(ID, PASSWORD, NAME)
        input("Press Enter to Return to Main Menu")

    else:
        print("Something Went Wrong, Maybe You Made an Invalid Choice")
        input("Press Enter to Return to Main Menu")
