#!/usr/bin/env python



import os

import py_compile



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet DERLEME ARACI")

print("""

Derleme Aracina Hosgeldin



""")



derle = raw_input("Program Ismini Girin: ")



py_compile.compile(derle)