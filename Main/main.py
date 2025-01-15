import sys
import os

# Add the Builds directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Builds'))

# Now you can import modules from the Builds directory
from Cinema.FinDetailsMovies import fdire
from Consulate import current, detail, find, map, regionsearch, weather, zip
from Library import lib
from Pastry import store
from Restaurant import payment
from School.GradeGenerator import generator
from School.MathCalculations import decimaltoroman, derivatives, fibo, logaritmic, math_and_frequency, MaximusMinimusSikitus, palindrome, triangle
from School.PeriodicTable import peri
from Veterinary.DogCatAgeCalculator import doggypussy

def display_menu():
    print("Select a module to access:")
    print("1. Cinema - FinDetailsMovies")
    print("2. Consulate - Current")
    print("3. Consulate - Detail")
    print("4. Consulate - Find")
    print("5. Consulate - Map")
    print("6. Consulate - Region Search")
    print("7. Consulate - Weather")
    print("8. Consulate - Zip")
    print("9. Library")
    print("10. Pastry - Store")
    print("11. Restaurant - Payment")
    print("12. School - Grade Generator")
    print("13. School - Math Calculations - Decimal to Roman")
    print("14. School - Math Calculations - Derivatives")
    print("15. School - Math Calculations - Fibonacci")
    print("16. School - Math Calculations - Logarithmic")
    print("17. School - Math Calculations - Math and Frequency")
    print("18. School - Math Calculations - Maximus Minimus Sikitus")
    print("19. School - Math Calculations - Palindrome")
    print("20. School - Math Calculations - Triangle")
    print("21. School - Periodic Table")
    print("22. Veterinary - Dog Cat Age Calculator")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '0':
            break
        elif choice == '1':
            print(fdire.some_function())
        elif choice == '2':
            print(current.some_function())
        elif choice == '3':
            print(detail.some_function())
        elif choice == '4':
            print(find.some_function())
        elif choice == '5':
            print(map.some_function())
        elif choice == '6':
            print(regionsearch.some_function())
        elif choice == '7':
            print(weather.some_function())
        elif choice == '8':
            print(zip.some_function())
        elif choice == '9':
            print(lib.some_function())
        elif choice == '10':
            print(store.some_function())
        elif choice == '11':
            print(payment.some_function())
        elif choice == '12':
            print(generator.some_function())
        elif choice == '13':
            print(decimaltoroman.some_function())
        elif choice == '14':
            print(derivatives.some_function())
        elif choice == '15':
            print(fibo.some_function())
        elif choice == '16':
            print(logaritmic.some_function())
        elif choice == '17':
            print(math_and_frequency.some_function())
        elif choice == '18':
            print(MaximusMinimusSikitus.some_function())
        elif choice == '19':
            print(palindrome.some_function())
        elif choice == '20':
            print(triangle.some_function())
        elif choice == '21':
            print(peri.some_function())
        elif choice == '22':
            print(doggypussy.some_function())
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()