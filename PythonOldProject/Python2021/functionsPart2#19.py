def bigNumRep(a, b):
    if a > b:
        return a
    elif b > a:
        return b


print(bigNumRep(5, 10))


def writeText(c, d):
    bigNum = bigNumRep(c, d)
    templateText = "{} is bigger than the other".format(bigNum)
    print(templateText)


writeText(12, 22)

# sinir bozucu

print("Derinlerde Bir Çığlık Sesi".split())


def nameSurname(nameSurnameDivision):
    name = nameSurnameDivision.split()[0]
    surname = nameSurnameDivision.split()[1]
    return name,surname

print(nameSurname("AtHirsizi Ahmet"))

def nameSurname2(*args):
    for item in args:
        print(item)
    return " ".join(args)


nameSurname2("Fatih","Mehmet","Macoglu")

print("-".join(["Ahmet","Dergi"]))


def middleName(**kwargs):
    if "middlename" in kwargs:
        print(kwargs["middlename"])
    else:
        print("Dont have it") 


middleName(middlename="Faik")
middleName(name="Faik")
