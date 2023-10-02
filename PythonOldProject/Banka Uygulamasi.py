import os

class Musteri():
    def __init__(self,TC,SIFRE,ISIM):
        self.tc = TC
        self.sifre = SIFRE
        self.isim = ISIM
        self.bakiye = 0

class Banka():
    def __init__(self):
        self.musteriler = list()


    def musteriol(self,TC,SIFRE,ISIM):
        self.musteriler.append(Musteri(TC,SIFRE,ISIM))
        print("Internet Bankaciligimiz'a Hosgeldiniz")

banka = Banka()


while True:
    os.system("cls")
    print("""

                    Dolliet'in Darphane Gorunumlu Bankasina Hosgeldiniz $

    1) Musteriyim
    2) Musteri Olmak Istiyorum

    """)

    secim = int(input("Seciminiz :"))

    if secim == 1:
        tcx = [a.tc for a in banka.musteriler]
        TC = input("TC : ")
        if TC in tcx:
            for musteri in banka.musteriler:
                if TC == musteri.tc:
                    sifre = input("Sifrenizi Giriniz : ")
                    if sifre == musteri.sifre:
                        while True:
                            os.system("cls")
                            print("                                 Hosgeldiniz Sayin {}".format(musteri.isim))
                            print("""

                            1) Bakiye Sorgulama
                            2) Para Yatir [Kendi Hesabina]
                            3) Para Yatir [Baskasinin Hesabina]
                            4) Para Cek
                            Q) Cikis

                            """)

                            secim2 = input("Islem Numarasi Giriniz :")

                            if secim2 == "1":
                                print("Bakiyeniz : {}".format(musteri.bakiye))
                                input("Ana Menuye Donmek Icin Enter'a Basiniz!")

                            elif secim2 == "2":
                                miktar = int(input("Miktar :"))
                                onay = input("Kendi Hesabiniza {} TL Para Yatirmayi Onayliyor Musunuz? E/H\n".format(miktar))
                                if onay == "E" or onay == "e":
                                    musteri.bakiye += miktar
                                    print("Paraniz Yatirildi!")
                                    print("Ana Menuye Donmek Icin Enter'a Basiniz")

                                elif onay == "H" or onay == "h":
                                    print("Islem Iptal Edildi")
                                    print("Ana Menuye Donmek Icin Enter'a Basiniz")

                                else:
                                    print("Hatali Giris Yaptiniz")
                                    input("Ana menuye Donmek Icin Enter'a Basiniz")

                            elif secim2 == "3":
                                arananTc = input("Musteri TC : ")
                                if arananTc in tcx:
                                    for digermusteri in banka.musteriler:
                                        if arananTc == digermusteri.tc:
                                            miktar = int(input("Miktar :"))
                                            if miktar <= musteri.bakiye:
                                                onay = input(" {} Adli Musterimize {} TL Tutarinda Para Yatirmayi Onayliyor Musunuz? E/H\n".format(digermusteri.isim,miktar))
                                                if onay == "E" or onay == "e":
                                                    digermusteri.bakiye += miktar
                                                    print("Para Aktarildi!")
                                                    input("Ana Menuye Donmek Icin Enter'a Basiniz")
                                                elif onay == "H" or onay == "h":
                                                    print("Islem Iptal Edildi")
                                                    input("Ana Menuye Donmek Icin Enter'a Basiniz")
                                                else:
                                                    print("Hatali Giris Yaptiniz,Islem Iptal Edildi")
                                                    input("Ana Menuye Donmek Icin Enter'a Basiniz")
                                            else:
                                                print("Bakiyeniz Yetersiz,Islem Iptal Edildi")
                                                input("Ana Menuye Donmek Icin Enter'a Basiniz")
                                    else:
                                        print("Musteri Bulunamadi")
                            elif secim2 == "4":
                                miktar = int(input("Miktar :"))
                                if miktar <= musteri.bakiye:
                                    musteri.bakiye -= miktar
                                    print("Islem Tamamlandi, Paranizi Aliniz")
                                    input("Ana Menuye Donmek Icin Enter'a Basiniz")
                                else:
                                    print("Bakiyeniz Yetersiz,Islem Iptal Edildi")
                                    input("Ana Menuye Donmek Icin Enter'a Basiniz")

                            elif secim2 == "Q" or secim2 == "q" :
                                break

    elif secim == 2:
        a = input("TC Giriniz :")
        b = input("Isim Giriniz :")
        c = input("Sifre Giriniz :")
        banka.musteriol(a,c,b)
        input("Ana Menuye Donmek Icin Enter'a Basiniz")

    else:
        print("Birseyler Ters Gitti, Belkide Hatali Secim Yaptiniz")

        # for a in banka.musteriler:
        #     tcx += [a.tc f]
