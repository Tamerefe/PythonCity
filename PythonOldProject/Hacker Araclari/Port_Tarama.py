#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet PORT TARAMA")

print("""

Port Tarama Aracina Hosgeldiniz :)



1) Hizli Tarama

2) Servis ve Versiyon Bilgisi

3) Isletim Sistemi Bilgisi 



""")



islemno = raw_input("Islem Numarasini Girin: ")



if(islemno=="1"):

	hedefip = raw_input("Hedef Ip Girin: ")

	os.system("nmap " + hedefip)



elif(islemno=="2"):

	hedefip = raw_input("Hedef Ip Girin: ")

	os.system("nmap -sS -sV " + hedefip)



elif(islemno=="3"):

	hedefip = raw_input("Hedef Ip Girin: ")

	os.system("nmap -sS -sV " + hedefip)

else:

	print("Hatali Secim Yaptin Reis :(")