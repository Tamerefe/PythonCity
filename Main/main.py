import sys
import os

# Add the Builds directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Builds'))

# Add the Bot directory to the system path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'Bot'))

# Now you can import modules from the Builds and Bot directories
from Cinema.FinDetailsMovies import fdire
from Consulate import current, detail, find, map, regionsearch, weather, zip
from Library import lib
from Pastry import store
from Restaurant import payment
from School.GradeGenerator import generator
from School.MathCalculations import decimaltoroman, derivatives, fibo, logaritmic, math_and_frequency, MaximusMinimusSikitus, palindrome, triangle
from School.PeriodicTable import peri
from Veterinary.DogCatAgeCalculator import doggypussy
from sim import LifeSimulation, Character
from Cinema.CinEmote import emote

def display_menu():
    print("Select a module to access:")
    print("1. Cinema - FinDetailsMovies")
    print("2. Cinema - Emote")
    print("3. Consulate - Current")
    print("4. Consulate - Detail")
    print("5. Consulate - Find")
    print("6. Consulate - Map")
    print("7. Consulate - Region Search")
    print("8. Consulate - Weather")
    print("9. Consulate - Zip")
    print("10. Library")
    print("11. Pastry - Store")
    print("12. Restaurant - Payment")
    print("13. School - Grade Generator")
    print("14. School - Math Calculations - Decimal to Roman")
    print("15. School - Math Calculations - Derivatives")
    print("16. School - Math Calculations - Fibonacci")
    print("17. School - Math Calculations - Logarithmic")
    print("18. School - Math Calculations - Math and Frequency")
    print("19. School - Math Calculations - Maximus Minimus Sikitus")
    print("20. School - Math Calculations - Palindrome")
    print("21. School - Math Calculations - Triangle")
    print("22. School - Periodic Table")
    print("23. Veterinary - Dog Cat Age Calculator")
    print("24. Life Simulation")
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
            text = input("Enter text to convert to emoji: ")
            print(emote.textToEmote(text))
        elif choice == '3':
            print(current.some_function())
        elif choice == '4':
            print(detail.some_function())
        elif choice == '5':
            print(find.some_function())
        elif choice == '6':
            print(map.some_function())
        elif choice == '7':
            print(regionsearch.some_function())
        elif choice == '8':
            print(weather.some_function())
        elif choice == '9':
            print(zip.some_function())
        elif choice == '10':
            print(lib.some_function())
        elif choice == '11':
            print(store.some_function())
        elif choice == '12':
            print(payment.some_function())
        elif choice == '13':
            print(generator.some_function())
        elif choice == '14':
            print(decimaltoroman.some_function())
        elif choice == '15':
            print(derivatives.some_function())
        elif choice == '16':
            print(fibo.some_function())
        elif choice == '17':
            print(logaritmic.some_function())
        elif choice == '18':
            print(math_and_frequency.some_function())
        elif choice == '19':
            print(MaximusMinimusSikitus.some_function())
        elif choice == '20':
            print(palindrome.some_function())
        elif choice == '21':
            print(triangle.some_function())
        elif choice == '22':
            print(peri.some_function())
        elif choice == '23':
            print(doggypussy.some_function())
        elif choice == '24':
            character = Character()
            simulation = LifeSimulation(character)
            character.show_status()
            while simulation.play_turn():
                user_input = input("Advance the year: ")
                if user_input.lower() == 'q':
                    break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()