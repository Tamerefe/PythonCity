import os

def show_menu():
    print("Welcome to PythonCity!")
    print("Choose an application to run:")
    print("1. Cinema")
    print("2. Restaurant")
    print("3. Library")
    print("4. Pastry")
    print("5. Veterinary")
    print("6. School")
    print("7. Consulate")
    print("8. Mnos")
    print("9. Extras")
    print("10. Bot")
    print("0. Exit")

def run_application(choice):
    if choice == '1':
        os.system('python ../Builds/Cinema/cinema.py')
    elif choice == '2':
        os.system('python ../Builds/Restaurant/payment.py')
    elif choice == '3':
        os.system('python ../Builds/Library/lib.py')
    elif choice == '4':
        os.system('python ../Builds/Pastry/store.py')
    elif choice == '5':
        os.system('python ../Builds/Veterinary/DogCatAgeCalculator/doggypussy.py')
    elif choice == '6':
        school_menu()
    elif choice == '7':
        os.system('python ../Builds/Consulate/maps.py')
    elif choice == '8':
        os.system('python ../Builds/Mnos/PhoneDirectory/iPhone.py')
    elif choice == '9':
        extras_menu()
    elif choice == '10':
        os.system('python ../Bot/sim.py')
    elif choice == '0':
        print("Exiting...")
        exit()
    else:
        print("Invalid choice. Please try again.")

def school_menu():
    print("School Applications:")
    print("1. Grade Generator")
    print("2. Math Calculations")
    print("3. Periodic Table")
    choice = input("Enter your choice: ")
    if choice == '1':
        os.system('python ../Builds/School/GradeGenerator/generator.py')
    elif choice == '2':
        math_calculations_menu()
    elif choice == '3':
        os.system('python ../Builds/School/PeriodicTable/peri.py')
    else:
        print("Invalid choice. Returning to main menu.")

def math_calculations_menu():
    print("Math Calculations:")
    print("1. Decimal to Roman")
    print("2. Derivatives")
    print("3. Fibonacci")
    print("4. Logarithmic Integration")
    print("5. Basic Math and Frequency")
    print("6. Maximus Minimus")
    print("7. Palindrome")
    print("8. Triangle Details")
    choice = input("Enter your choice: ")
    if choice == '1':
        os.system('python ../Builds/School/MathCalculations/decimaltoroman.py')
    elif choice == '2':
        os.system('python ../Builds/School/MathCalculations/derivatives.py')
    elif choice == '3':
        os.system('python ../Builds/School/MathCalculations/fibo.py')
    elif choice == '4':
        os.system('python ../Builds/School/MathCalculations/logaritmic.py')
    elif choice == '5':
        os.system('python ../Builds/School/MathCalculations/math_and_frequency.py')
    elif choice == '6':
        os.system('python ../Builds/School/MathCalculations/MaximusMinimusSikitus.py')
    elif choice == '7':
        os.system('python ../Builds/School/MathCalculations/palindrome.py')
    elif choice == '8':
        os.system('python ../Builds/School/MathCalculations/triangle.py')
    else:
        print("Invalid choice. Returning to school menu.")

def extras_menu():
    print("Extras:")
    print("1. HeatMap")
    print("2. ProgressBar")
    print("3. CreateBarcode")
    choice = input("Enter your choice: ")
    if choice == '1':
        os.system('python ../Extras/HeatMap/heat.py')
    elif choice == '2':
        print("ProgressBar options:")
        print("1. Strong ProgressBar")
        print("2. Downloading Bar")
        sub_choice = input("Enter your choice: ")
        if sub_choice == '1':
            os.system('python -m tqdm')
        elif sub_choice == '2':
            os.system('python -m rich.progress')
        else:
            print("Invalid choice. Returning to extras menu.")
    elif choice == '3':
        os.system('python -m ipython')
    else:
        print("Invalid choice. Returning to main menu.")

if __name__ == "__main__":
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        run_application(choice)