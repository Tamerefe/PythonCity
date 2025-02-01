import sys
import os

# Proje kök dizinini al
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Gerekli dizinleri sys.path'e ekle
sys.path.append(os.path.join(BASE_DIR, 'Builds'))
sys.path.append(os.path.join(BASE_DIR, 'Bot'))

# Modülleri içe aktar
try:
    from Cinema.FinDetailsMovies import fdire
    from Consulate import maps
    from Library import lib
    from Pastry import store
    from Restaurant import payment
    from School.GradeGenerator import generator
    from School.MathCalculations import (
        decimaltoroman, derivatives, fibo, logaritmic, 
        math_and_frequency, MaximusMinimusSikitus, palindrome, triangle
    )
    from School.PeriodicTable import peri
    from Veterinary.DogCatAgeCalculator import doggypussy
    from sim import LifeSimulation, Character
    from Cinema.CinEmote import emote
except ImportError as e:
    print(f"Module import error: {e}")
    sys.exit(1)

# Menü seçenekleri
MENU_OPTIONS = {
    '1': ('Cinema - FinDetailsMovies', fdire, 'some_function', "Enter the movie name: "),
    '2': ('Cinema - Emote', emote, 'textToEmote', "Enter text to convert to emoji: "),
    '3': ('Consulate', maps, 'some_function', None),
    '4': ('Library', lib, 'some_function', None),
    '5': ('Pastry - Store', store, 'some_function', None),
    '6': ('Restaurant - Payment', payment, 'some_function', None),
    '7': ('School - Grade Generator', generator, 'some_function', None),
    '8': ('School - Math Calculations - Decimal to Roman', decimaltoroman, 'some_function', None),
    '9': ('School - Math Calculations - Derivatives', derivatives, 'some_function', None),
    '10': ('School - Math Calculations - Fibonacci', fibo, 'some_function', None),
    '11': ('School - Math Calculations - Logarithmic', logaritmic, 'some_function', None),
    '12': ('School - Math Calculations - Math and Frequency', math_and_frequency, 'some_function', None),
    '13': ('School - Math Calculations - Maximus Minimus Sikitus', MaximusMinimusSikitus, 'some_function', None),
    '14': ('School - Math Calculations - Palindrome', palindrome, 'some_function', None),
    '15': ('School - Math Calculations - Triangle', triangle, 'some_function', None),
    '16': ('School - Periodic Table', peri, 'some_function', None),
    '17': ('Veterinary - Dog Cat Age Calculator', doggypussy, 'some_function', None),
    '18': ('Life Simulation', None, None, None),
}

def display_menu():
    """Menüyü ekrana yazdırır."""
    print("\nSelect a module to access:")
    for key, (desc, _, _, _) in MENU_OPTIONS.items():
        print(f"{key}. {desc}")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if not choice:  # Kullanıcı boş giriş yaparsa, tekrar menüyü göster
            print("Invalid input. Please select a valid option.")
            continue

        if choice == '0':
            print("Exiting program...")
            break

        if choice in MENU_OPTIONS:
            desc, module, func_name, prompt = MENU_OPTIONS[choice]

            try:
                if module and func_name:
                    func = getattr(module, func_name, None)
                    if callable(func):
                        arg = input(prompt).strip() if prompt else None
                        result = func(arg) if arg else func()
                        print(result)
                    else:
                        print(f"Error: {func_name} not found in {desc}.")
                elif choice == '18':
                    character = Character()
                    simulation = LifeSimulation(character)
                    character.show_status()
                    while simulation.play_turn():
                        user_input = input("Advance the year (press Q to quit): ").strip().lower()
                        if user_input == 'q':
                            break
            except Exception as e:
                print(f"An error occurred in {desc}: {e}")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
