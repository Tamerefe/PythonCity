tup1 = (1,3,5)

for num in tup1:
    print(num)

lists = [[1,2],[3,4]]

for num1,num2 in lists:
    print(num1,num2)

print("")

lists2 = [[1, 2,3], [3,4,5]]

for num1, num2, num3 in lists2:
    print(num1, num2, num3)

lists2 = [[1, 2], [3, 4],[5,6]]

print("")

for num1, num2 in lists2:
    print(num1, num2)


print("")

for num1, num2 in lists2:
    print(num1 * num2)

users1 = {
    "name": "Naz",
    "surname": "Rain"
}

print(users1.items())
print(users1.keys())

print("")

for k,v in users1.items():
    print("Key: {} \t Value: {}".format(k,v))

for k in users1.keys():
    print("Key: {}".format(k))
