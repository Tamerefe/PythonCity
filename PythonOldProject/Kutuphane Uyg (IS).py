import os

kliste = list()

menu = """
                    Dolliet'in Kutuphane Fabrikasina Hosgeldiniz <3

1)Kitap Ver
2)Kitap Al
3)Tumunu Incele
Q)Cikis

"""

def kver(kitap:tuple,liste:list):
    liste.append(kitap)
    print("Verdiginiz Kitap Icin Tesekkurler")
    input("Ana Menuye Donmek Icin Enter'a Basin!")

def kontrol(kitap:tuple,liste:list):
    if kitap in liste:
        return True
    else:
        return False

def kal(kitap:tuple,liste:list):
    if kontrol(kitap,liste):
        liste.remove(kitap)
        print("Kitabi Basari Ile Aldiniz Iyi Okumalar...")
        input("Ana Menuye Donmek Icin Enter'a Basin!")
    else:
        print("Istediginiz Kitap Mevcut Degil")
        input("Ana Menuye Donmek Icin Enter'a Basin!")

def lis(liste:list):
    for a in liste:
        print("Kitap Adi : {}       Yazar : {} ".format(a[0],a[1]))
    input("Ana Menuye Donmek Icin Enter'a Basin!")

while True:
    os.system("cls")
    print(menu)

    secim = input("Islem Numarasini Giriniz :")

    if secim == "1":
        kadi = input("Kitabin Adi :")
        yazar = input("Yazar :")
        kitap = (kadi,yazar)
        kver(kitap,kliste)

    elif secim == "2":
        kadi = input("Kitabin Adi :")
        yazar = input("Yazar :")
        kitap = (kadi,yazar)
        kal(kitap,kliste)

    elif secim == "3":
        lis(kliste)
    elif secim == "Q" or secim == "q":
        print("BB Daha Sonra Seni Tekrar Bekleriz...")
        quit()
    else:
        print("Hatali Giris Yaptiniz")
        input("Ana Menuye Donmek Icin Enter'a Basin")
