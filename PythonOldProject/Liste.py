#liste = ["abc",12,45,"dasd"]

#for a in liste:
    #print(type(a))

#liste = list("dsagsd",2145)

#liste =["Ankara","Istabul","Adana","Izmir"]

#liste += ["dsagsasd"]
#print(liste)

#for a in liste:
    #print(a)
#giris = input("Sehir Ekleyin : ")

#liste += [giris]

#for b in liste:
    #print(b)

#LISTE METODLARI

liste = ["Ankara","Istanbul","Adana","Izmir"]

#liste.append("Konya")
#liste.append("Antalya")
#liste.remove("Adana")

liste2 = liste.copy()

print(liste)
print(liste2)
print(50*"=")

liste.append("Konya")
liste.remove("Adana")
liste2.append("Antalya")
liste2.extend(liste)


print(liste)
print(liste2)
print(liste2.count("Ankara"))
liste2.sort()
print(liste2)
print(50*"=")

liste3 = [1,28,3,99,5,6,17,8,2314,1502,125,214,79,56]

print(liste3)
liste3.sort()
print(liste3)
print(50*"=")

print(liste.index("Izmir"))

gersay = int(liste.index("Izmir"))
gersay += 1
print(gersay)
