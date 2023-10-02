# Kullanım Yapısı
# while <şart doğruyken>Ş
#   <burada yazılanı yap>

x = 0

while x < 10:
    print("{} value < 10 thats true".format(x))
    x += 1

# while True:
#     print("abc")

print("")

# Kullanım Yapısı
# while <şart doğruyken>Ş
#   <burada yazılanı yap>
# else:
#   <burada yazilani yap>

y = 11

while y < 10:
    print("{} value < 10 thats true".format(y))
    y += 1
else:
    print("{} value < 10 thats not true".format(y))

num = 6
total = 1

while num > 0:
    total = total * num
    num -= 1
    print(total)

print("")
print("total : {}".format(total))
