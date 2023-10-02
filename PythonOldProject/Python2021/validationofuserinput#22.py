def numcontrol():
    inp = input("Enter a number : ")

    if inp.isdigit():
        print("Congratulations that's have a variable a real number type ")
    else:
        print("I'm Sorry But that's not a real number type")

numcontrol()


def numcontrol2():
    inp = input("Enter a number : ")

    while not inp.isdigit():
        print("I'm Sorry! But that's not a real number type, Please Retry")
        inp = input("Enter a number : ")
    else:
        print("Congratulations! that's have a variable a real number type")


numcontrol2()

def checkemail():
    # blabla@hotmail.com, blabbaala@boun.edu.tr
    inp1 = input("Please Retry your Email Address : ")

    while not (("." in inp1) and ("@" in inp1)):
        print("I'm Sorry! this is not a valid email")
        inp1 = input("Please Retry your Email Address : ")
    else:
        print("Congratulations! you have successfully logged in Email address")

checkemail()
