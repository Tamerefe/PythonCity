a = input("Ilk Sayiyi Giriniz : ")
a = float(a)
c = input("Yapilacak Islem : ")
b = input("Ikinci Sayiyi Giriniz : ")
b = float(b)

if c=="+":
	print("Sonuc :",a+b)

elif c=="-":
	print("Sonuc :",a-b)

elif c=="*":
	print("Sonuc :",a*b)

elif c=="/":
	print("Sonuc :",a/b)

elif c=="**":
	print("Sonuc :",a**b)

else:	
	print("Hatali Islem Yaptiniz")