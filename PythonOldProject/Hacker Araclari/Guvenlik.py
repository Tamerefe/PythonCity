#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet GUVENLIK DUVARI TESPIT")



print("""

Guvenlik Duvari Tespit Etme Aracina Hosgeldiniz 





""")



site = raw_input("Site Adresini Girin: ")

os.system("wafw00f " + site)