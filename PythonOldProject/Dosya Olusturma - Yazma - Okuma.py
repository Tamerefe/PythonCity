#dosya = open("deneme.txt","w")
dosya = open("deneme.txt","r")

veri = dosya.readlines()

#yaz = "Life"
#dosya.write(yaz)

#veri = dosya.read()

dosya.close()

print(veri)
