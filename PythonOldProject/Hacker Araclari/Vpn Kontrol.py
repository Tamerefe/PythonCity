#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet VPN KONTROL")



print("""



VPN Kontrol Aracina Hosgeldin Kral



""")



hedefip = raw_input("Hedef Ip Girin: ")

os.system("ike-scan " + hedefip)