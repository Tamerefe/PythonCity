import random

while True:
    rastgele = random.randint(1,9)
    sayi = int(input("Bir Sayi Giriniz : "))
    print("Sayi Buydu Brom = ",rastgele)

    if sayi == rastgele:
        print("Tebrikler Sayiyi Tutturdunuz!")
    else:
        input("Unlucky Brom Birdahaki Sefere Artik Bir Enter'imiz Var Brom")
