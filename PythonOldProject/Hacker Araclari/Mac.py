#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet MAC DEGISTIRME")

print("""

MAC Adres Degistirme Aracina Hosgeldiniz :)



1) Mac Adresi Random Belirle

2) Mac Adresi Elle Belirle

3) Mac Adresi Orjinale Dondur





""")



islemno = raw_input("Islem Numarasi Girin: ")



if(islemno=="1"):

	os.system("ifconfig eth0 down")

	os.system("macchanger -r eth0")

	os.system("ifconfig eth0 up")

	print("\033[92mYeni MAC Adresi Elle Belirlendi.")



elif(islemno=="2"):

	macadres = raw_input("Yeni Mac Adresi Girin: ")

	os.system("ifconfig eth0 down")

	os.system("macchanger --mac " + macadres + "eth0")

	os.system("ifconfig eth0 up")

	print("\033[92mYeni MAC Adresi Elle Belirlendi.")



elif(islemno=="3"):

	os.system("ifconfig eth0 down")

	os.system("macchanger -p eth0")

	os.system("ifconfig eth0 up")

	print("\033[92mMAC Orjinale Dondu.")



else:

	print("Mac Adresi Belirlemiyorum Ama Gene Iyisin Yeniden Baslatcam")

	os.system("python mac.py")