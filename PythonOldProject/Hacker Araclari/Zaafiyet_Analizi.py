#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet ZAAFIYET ANALIZI")



print("""

Zaafiyet Analizi Aracina Hosgeldiniz





""")



hedefip = raw_input("Hedef Ip Girin")

os.system("nikto -h " + hedefip)