strvar = "Python"
print(strvar)

print(strvar[3])
print(strvar[-5])
print(strvar[:2])
print(strvar[2:])
print(strvar[:])
print(strvar[1:4])
print(strvar[::2])
print(strvar[1:5:3])
print(len(strvar))

strvar = strvar + "add"

print(strvar)

print(strvar * 5)

strvar = strvar + " waow"

print(strvar.upper())
print(strvar.lower())
print(strvar.split())
print(strvar.split("a"))
print(strvar.split(sep = "a", maxslipt = 1))

# [] tek bir eleman alınır
# [:] baslangıç ve bitiş arasındaki elemanları alır
# [::] başlangıçve bitiş arasındaki elemanlar üçüncü kisimdaki değere göre atlayarak değerler alınır