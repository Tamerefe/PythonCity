from random import randrange

crte = randrange(10)

i = 0

gues = int(input("What was that my random number: "))

while True:

    if gues == crte:
        print("Congratulations {} is true number".format(gues))
        break
    elif gues <= crte:
        print('Number too small')
        gues = int(input(("Try Again: ")))
    elif gues >= crte:
        print('Number too large')
        gues = int(input(("Try Again: ")))
    else:
        gues = int(input(("Try Again: ")))
        i += 1 
    
    if i == 4:
        print("Sorry Buddy Maybe Next Time Try It Different Way")
        break