print(round(1.6))

def turnInteger():
    entry = input("Enter a Integer : ")

    print("Result of rounding :  {}".format(round(float(entry))))


turnInteger()


def turnInteger2():
    entry = input("Enter a Integer : ")

    print("Result of rounding :  {}".format(round(float(entry))))

    try:
        entry = float(entry)
        print("Result of rounding :  {}".format(round(entry)))
    except:
        print("{} value is not rounded".format(entry))


turnInteger2()


def turnInteger3():
    entry = input("Enter a Integer : ")

    print("Result of rounding :  {}".format(round(float(entry))))

    try:
        entry = float(entry)
    except:
        print("{} value is not rounded".format(entry))
    else:
        print("Result of rounding :  {}".format(round(entry)))

turnInteger3()


def turnInteger4():
    entry = input("Enter a Integer : ")

    statuss = ""

    try:
        entry = float(entry)
        print("Result of rounding :  {}".format(round(float(entry))))
        statuss = "Successful"
    except:
        print("{} value is not rounded".format(entry))
        statuss = "unSuccessful"
    finally:
        print("Integer conversion {} completed as".format(statuss))


turnInteger4()


def turnIntegerWHILE():

    while True:
        entry = input("Enter a Integer : ")

        try:
            entry = float(entry)
            print("Result of rounding :  {}".format(round(float(entry))))
            break
        except:
            print("{} value is not rounded".format(entry))
            pass

turnIntegerWHILE()

# https://docs.python.org/3/tutorial/errors.html

# Exceptions Type

print(5 + "")

listt = []

print(listt[4])

member = {
    "Name" : "Faz",
    "Id_Num" :  124515
}

print(member["surname"])


try:
    print(5 + "a")
except TypeError:
    print("No action is taken with the entered data.")

try:
    print(5 + "a")
except IndexError:
    print("No action is taken with the entered data.")
except:
    print("The code is not working properly")

try:
    print(listt[-1])
except IndexError:
    print("The element you are trying to index is outside the list. ")
except:
    print("The code is not working properly")

try:
    print(member["surname"])
except KeyError:
    print("The person's information is missing or entered incorrectly. ")
except:
    print("The code is not working properly")
