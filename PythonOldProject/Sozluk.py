#sozluk = {"Yas":15,
#"Dogum":"Angara",
#"Meslek":"Ogrenci"}

#print(sozluk["Yas"])
#print(sozluk["Dogum"])
#print(sozluk["Meslek"])

#sozluk = dict()

#Ninja = {

#"Guc": 165,
#"Sp" : 78,
#"Str": 142,
#"Hp" : 4050

#}

#Silahci = {

#"Guc": 682,
#"Sp" : 102,
#"Str": 12,
#"Hp" : 1002

#}

#def vur(vuran:dict,vurulan:dict):
#    eksilen = vuran["Guc"]
#    vurulan["Hp"] = vurulan["Hp"] - eksilen

#while True:

#input("Vurmak Icin Enter'a Basiniz!")
#vur(Ninja,Silahci)
#print("Silahci'nin Cani:",Silahci["Hp"])

#input("Vurmak Icin Enter'a Basiniz!")
#vur(Silahci,Ninja)
#print("Ninja'nin Cani:",Ninja["Hp"])

#SOZLUK METODLARI

sozluk = {"Siyah":"Kara","Ak":"Beyaz","Abide":"Anit","Adet":"Tane"}

#giris = input("Kelime Giriniz : ")

#print(sozluk.get(giris,"Aradiniz Sey Bulunamadi"))

for b in sozluk.items():
    print(b)
print(20*"=")
for c in sozluk.keys():
    print(c)
print(20*"=")
for a in sozluk.values():
    print(a)
