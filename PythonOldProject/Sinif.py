# SINIF OLUSTURMA

# class Asker():
#     pass

# SINIFIN NITELIKLERI

# class Asker():
#     Saglik = 100
#     Silah = "Ak47"
#     Ekipman = "Grenade"

# print(Asker.Saglik)

# Asker.mermisayisi = 30

# print(Asker.mermisayisi)

# SINIFIN ORNEKLENDIRMESI

# class Asker():
#     saglik = 0
#     silah = []
#     ekipman = ''
#     isim = ''
#     mermi = 0

# ahmet = Asker()

# ahmet.saglik = 76
# ahmet.silah = ["M4A1-S"]
# ahmet.ekipman = "Flash Bang"
# ahmet.isim = "Ahmet"
# ahmet.mermi = 20

# ilk = 10
# b = ilk
# b = 20
# print(b)

# b = []
# b += ["Selamlar"]
# b += ["Muzrokyafra"]
# print(b)

#tamer = Asker()

# tamer.saglik = 240
# tamer.silah = ["AWP"]
# tamer.ekipman = "Nuke"
# tamer.isim = "Ghost"
# tamer.mermi = 7

# print(ahmet.isim,ahmet.silah,ahmet.saglik,ahmet.ekipman,ahmet.mermi)
# print()
# print()
# print(tamer.isim,tamer.silah,tamer.saglik,tamer.ekipman,tamer.mermi)

# ORNEK NITELIKLER

# class Asker():
#      silah = []
#      print("Ver Mehteri Ver Ver")

# mehmet = Asker()
# mehmet.silah += ["Tabanca"]

# ruzgar = Asker()
# ruzgar.silah += ["Bicak"]

# print(mehmet.silah)

# class Asker():

    # def __init__(self):
    #     self.silah = []
    #     print("Selamlar Turkiyem")

# mehmet = Asker()
# mehmet.silah += ["Tabanca"]

# ruzgar = Asker()
# ruzgar.silah += ["Bicak"]

# print(mehmet.silah,ruzgar.silah)

# class A():
#     print("Hayat Guzel")

class Asker():
    silah = []

    def __init__(self,silah,mermi):
         self.silah = silah
         self.mermi = mermi

ahmet = Asker("Tabanca",80)
mehmet = Asker("El Bombasi",0)

# print(ahmet.mermi,ahmet.silah)
# print(mehmet.mermi,mehmet.silah)
print(ahmet.silah)
print(Asker.silah)
