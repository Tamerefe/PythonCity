# Kullanım Yapısı

# for <degisken> in <iterable>:
# <buraya yazilani yap>

commenters = ["faik bo","copi","dan","as1","derin"]

for users in commenters:
    print(users)

numberOfusers = 0

for users in commenters:
    numberOfusers = numberOfusers + 1
    print(users,numberOfusers)

print("")

for users in commenters:
    print(users,numberOfusers)
    numberOfusers = numberOfusers + 1

print(commenters[0].split(), 
      commenters[0].split()[0],
      commenters[0].split()[1])

name, surname = commenters[0].split()[0], commenters[0].split()[1]

print(name,surname)

print("")

for users in commenters:
    numberOfusers += 1
    name1 = users.split()[0]

    try:
        surname1 = users.split()[1]
    except IndexError:
        print("{0}. Users Name {1}".format(
            numberOfusers,name1))
    else:
        print("{0}. Users Name {1} and Surname {2}".format(numberOfusers, name1, surname1))

    # Being a software developer is insane.

print("")

moderator = "faik"

moderatornum = 0

for users in commenters:
    numberOfusers += 1
    name1 = users.split()[0]

    if(name1 == moderator):
        moderatornum += 1
        usertype = "Moderator"
    else:
        usertype = "Users"

    try:
        surname1 = users.split()[1]
    except IndexError:
        print("{0}. {1} Name {2}".format(
            numberOfusers, usertype, name1))
    else:
        print("{0}. {1} Name {2} and Surname {3}".format(
            numberOfusers, usertype, name1, surname1))

    # I totally agree with this idea now.


