print(range(10))
print(type(range(10)))
print(list(range(10)))
print([*range(10)])
print([*range(2,7,2)])

lists = [1,2,3]
print(type(lists))

for num in range(10):
    print(num)

print("")

letters = ["a","b","c","d","e"]

for letter in enumerate(letters):
    print(letter)

print("")

for index, letter in enumerate(letters):
    print("{}. letter: {}".format(index, letter))

print("")

countrys = ["TR","FR","DE"]
sorting = range(1,4)

print(len(sorting))

for country in zip(countrys, sorting):
    print(country)

for country, sort in zip(countrys, sorting):
    print(country,sort)


