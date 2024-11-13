import periodictable
from colorama import init, Fore, Style

init()

atomicNo = int(input("Enter atomic number: "))

element = periodictable.elements[atomicNo]
print(Fore.GREEN + "Element:", Fore.YELLOW + element.name)
print(Fore.GREEN + "Symbol:", Fore.YELLOW + element.symbol)
print(Fore.GREEN + "Atomic Weight:", Fore.YELLOW + str(element.mass))
print(Fore.GREEN + "Density:", Fore.YELLOW + str(element.density))
print(Fore.GREEN + "Isotopes:", Fore.YELLOW + str(element.isotopes))
print(Style.RESET_ALL)