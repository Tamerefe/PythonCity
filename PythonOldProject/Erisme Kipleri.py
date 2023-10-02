#dosya = open("deneme1.txt","w")
#dosya = open("deneme1.txt","a")
#dosya = open("deneme1.txt","x")
#dosya = open("deneme1.txt","r+")
#dosya = open("deneme1.txt","w+")
dosya = open("deneme1.txt","a+")

#yazi = "Etik Hacker"
yazi = "Etik Hacker"

dosya.write(yazi)

veri = dosya.read()

dosya.close()

print(veri)
