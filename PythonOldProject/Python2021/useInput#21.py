input("Give Me 1 Number:")
give = input("Give Me 1 Number:")

print(type(int(give)))

def app():
    giveMeONE = input("Enter a number : ")
    operates = input("check are a number single or double : ")

    if operates == "double":
        if int(giveMeONE) % 2 == 0 :
            return print("Yeah {} that one is a double number".format(giveMeONE))
        else:
            return print("No {} that one is a single number".format(giveMeONE))
    if operates == "single":
        if int(giveMeONE) % 2 == 1:
            return print("Yeah {} that one is a single number".format(giveMeONE))
        else:
            return print("No {} that one is a double number".format(giveMeONE))

app()
