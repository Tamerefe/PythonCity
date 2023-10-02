# Kullanım Senaryosu - 1:

# if <koşul sağlanıyorsa>
#    <burada yazılanı yap>

weather = "snowy"

if weather == "rainy":
    print("U can take umbrella")

# Kullanım Senaryosu - 2:

# if <koşul sağlanıyorsa>
#    <burada yazılanı yap>
# else:
#    <burada yazılanı yap>

if weather == "rainy":
    print("U can take umbrella")
else:
    print("No Problems")
if weather == "snowy":
    print("U can take scarf")
else:
    print("No Problems")

age = 35

if age > 18:
    print("Hi babe")
else:
    print("Sorry Babe You Cant Join Us")

lists = ["a","b","c"]

choose_character = "d"

if choose_character in lists:
    print("I found")
else:
    lists.append(choose_character)
    print("I added character in list")
    print("Last status of list {}".format(lists))

if (choose_character in lists) and (choose_character == lists[0]):
    print("I found and character is first in position")
elif choose_character in lists:
    print("I found but character isnt first in position")
else:
    lists.append(choose_character)
    print("I added character in list")
    print("Last status of list {}".format(lists))

if choose_character in lists:
    print("I found and character is first in position")
elif (choose_character in lists) and (choose_character == lists[0]):
    print("I found but character isnt first in position")
else:
    lists.append(choose_character)
    print("I added character in list")
    print("Last status of list {}".format(lists))
