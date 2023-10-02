kliste = list()

menu = """

1) Kitap Ekle
2) Kitap Cikar
3) Kitaplari Goster
Q) Cikis


"""

def kekle(liste,kitap):
    liste += [kitap]
    print("Kitap Basari Ile Eklendi")
    input("Ana Menuye Donmek Icin Enter'a Basiniz!")

def kcikar ():
    pass
def listele(liste):
    for a in liste:
        print("Kitap Adi >>>>>>>> {} ".format(a))
    input("Ana Menuye Donmek Icin Enter'a Basiniz!")

def cikis():
    quit()

while True:
    print(menu)

    secim = input("Seciminiz :")

    if secim == "1":
        kadi = input("Kitap Adi")
        kekle(kliste,kadi)
    elif secim == "2":
        kcikar()
    elif secim =="3":
        listele(kliste)
    elif secim =="Q" or secim == "q":
        cikis()
    else:
        print("Brom Yanlis Secim")
        input("Ana Menuye Donmek Icin Enter'a Basiniz!")
