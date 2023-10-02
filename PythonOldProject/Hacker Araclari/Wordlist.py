#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet WORLDLIST OLUSTUR")

print("""

Wordlist Olusturma Aracina Hos Geldin



""")



minimum =raw_input("Minumum Karakter Sayisini Girin: ")

maximum =raw_input("Maksimum Karakter Sayisini Girin: ")

karakter =raw_input("Istediginiz Karakterleri Girin: ")



os.system("crunch" + minimum + " " + maximum + " " + karakter )



print("Basariyla Tamamlandi")