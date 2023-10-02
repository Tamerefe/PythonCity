#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet WORDPRESS TARAMA")



print("""



Wordpress Tarama Aracina Hosgeldin



1) Hizli Tarama

2) Eklenti Tarama

3) Tema Tarama

4) Yonetici Kullanici Adi Tarama





""")



islemno = raw_input("Islem Numarasi Girin: ")



if(islemno=="1"):

	site = raw_input("Site Adresi Girin: ")

	os.system("wpscan --url " + site)



elif(islemno=="2"):

	site = raw_input("Site Adresi Girin: ")

	os.system("wpscan --url " + site + " --enumerate p" )



elif(islemno=="3"):

	site = raw_input("Site Adresi Girin: ")

	os.system("wpscan --url " + site + " --enumerate t" )



elif(islemno=="4"):

	site = raw_input("Site Adresi Girin: ")

	os.system("wpscan --url " + site + " --enumerate u" )

else:

	print("Hatali Secim Yaptiniz Programi Kapatiyorum")