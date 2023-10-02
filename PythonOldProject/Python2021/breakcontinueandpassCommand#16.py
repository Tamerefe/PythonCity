letters = ['a','b','c','d','e'] * 100

for index, letter in enumerate(letters):
    if letter == 'c':
        print("{} letter {}. index!".format(letter,index))
        break

for num in range(1,6):
    if num %2 == 0: # çift sayı sorgulama mantığı
        continue
    print(num)

print("")

for num in range(1, 6):
    if num % 2 == 0:  # çift sayı sorgulama mantığı
        pass
    else:
        print(num)

print("")

if num < 5:
    pass
else:
    print("Hey")
