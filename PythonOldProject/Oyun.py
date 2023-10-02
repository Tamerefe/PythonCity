import random,os

class Hedef():
    def __init__(self):
        self.saglik = random.randint(5,10)
        self.guc = random.randint(3,7)
        self.kalkan = random.randint(3,7)
        self.sag = True

    def vur(self,oyuncu):
        atak = self.guc = oyuncu.kalkan
        oyuncu.saglik -= atak
        if oyuncu.saglik <= 0:
            oyuncu.sag = False

class Oyuncu():
    def __init__(self):
        self.saglik = 50
        self.guc = 7
        self.kalkan = 3
        self.sag = True

    def vur(self,hedef):
        atak = self.guc - hedef.kalkan
        hedef.saglik -= atak
        if hedef.saglik <= 0:
            hedef.sag = False
            hedefler.remove(hedef)

hedefler = list()
for a in range(5):
    hedefler.append(Hedef())
oyuncu = Oyuncu()

while True:
    os.system("cls")
    print("Oyuncu Durumu : ------ Saglik Degeri : {} ------  Saldiri Degeri {} ------  Kalkan Degeri {} ".format(oyuncu.saglik,oyuncu.guc,oyuncu.kalkan))
    if oyuncu.sag == False:
        print("Oyun Bitti!")
        quit()
    if not hedefler:
        print("Tebrikler Kazandiniz...")
        quit()
    for a in hedefler:
        print("{}. Hedef ------  Saglik Degeri : {} ------  Saldiri Degeri {} ------  Kalkan Degeri {} ".format(hedefler.index(a),a.saglik,a.guc,a.kalkan))

    secim = int(input("Hedef Secin : "))
    hedeff = hedefler[secim]
    oyuncu.vur(hedeff)
    if hedefler:
        saldirgan = hedefler[random.randint(0,len(hedefler)-1)]
        saldirgan.vur(oyuncu)
