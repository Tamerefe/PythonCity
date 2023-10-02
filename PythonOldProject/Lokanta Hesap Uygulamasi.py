import os

masalar = dict()

for a in range(20):
    masalar[a] = 0

def ekle():
    masano = int(input("Masa No : "))
    gecerli = masalar[masano]
    eklenecek = float(input("Eklenecek Ucret : "))
    toplam = gecerli + eklenecek
    masalar[masano] = toplam

def sil():
     masano = int(input("Masa No : "))
     gecerli = masalar[masano]
     silinecek = float(input("Eksilecek Ucret : "))
     toplam = gecerli - silinecek
     if toplam < 0 :
         print("Islemde Hata Var!")
         print("Ana Menuye Donmek Icin Enter'a Basiniz!")
         input()
     else:
         masalar[masano] = toplam
         print("Isleminiz Tamamlandi! Ana Menuye Donmek Icin Enter'a Basiniz!")

def kontrol(dosya_kayit):
    try:
        dosya=open(dosya_kayit)
        veriler = dosya.read()
        veriler =veriler.split("\n")
        veriler.pop()
        dosya.close()
        flag = True
    except FileNotFoundError:
        dosya=open(dosya_kayit,"w")
        dosya.close()
        print("Ilk Kez Calistirildi! Kayit Dosyasi Olusturuldu")
        flag = False
    if flag:
        for a in enumerate(veriler):
            masalar[a[0]] = float(a[1])
    else:
        pass

def guncelle():
    dosya = open("defter.txt","w")
    for a in range(20):
        ucret = masalar[a]
        ucret = str(ucret)
        dosya.write(ucret+"\n")
    dosya.close()

def ana():
    kontrol("defter.txt")

    while True:
        os.system("cls")

        guncelle()

        print("""

                    Lokanta Hesap Uygulamasina Hosgeldin Isletmeci

    1) Masalari Goruntule
    2) Hesap Ekle
    3) Hesap Sil
    Q) Cikis

        """)
        secim = input("Islem Numarasi Giriniz : ")

        if secim =="1":
            for a in range(20):
                print("Masa {} icin hesap: {} ".format(a,masalar[a]))
            print("Isleminiz Tamamlandi! Ana Menuye Donmek Icin Enter'a Basiniz!")
            input()

        elif secim =="2":
            ekle()
            print("Isleminiz Tamamlandi! Ana Menuye Donmek Icin Enter'a Basiniz!")
            input()
        elif secim =="3":
            sil()
        elif secim == "Q" or secim == "q":
            print("Program Kapaniyor")
            quit()
ana()
