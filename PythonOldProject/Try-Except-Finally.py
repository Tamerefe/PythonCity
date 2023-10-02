a = float(input("Bolunen :"))
b = float(input("Bolen :"))

try:
    print("Sonuc :",a/b)

except ZeroDivisionError as hata :
    print("0'a Bolum Tanimsizdir!")
    print(hata)
except TypeError :
    print("Veri Tipi Hatali")
finally:
    print("Bu Her Zaman Calisir")
