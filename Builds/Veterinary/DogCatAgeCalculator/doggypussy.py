animalage = input("To calculate the age of your chosen animal:\nPress 'D' for dog \nPress 'C' for cat\
                  \nPress 'R' for rabbit\nPress 'B' for bird\nPress 'H' for hamster\nPress 'F' for fish \n: ").lower()

if animalage == "d":
    gvmepet = int(input("How old is your pet: "))
    if gvmepet == 1:
        print("Dog's age relative to human age is 15")
    elif gvmepet == 2:
        print("Dog's age relative to human age is 24")
    elif gvmepet > 2:   
        print("Dog's age relative to human age is {0}".format((gvmepet-2)*4 + 24))     
elif animalage == "c":
    gvmepet = int(input("How old is your pet: "))
    if gvmepet == 1:
        print("Cat's age relative to human age is 15")
    elif gvmepet == 2:
        print("Cat's age relative to human age is 25")
    elif gvmepet > 2:
        print("Cat's age relative to human age is {0}".format((gvmepet-2)*4 + 25))     
elif animalage == "r":
    gvmepet = int(input("How old is your pet: "))
    print("Rabbit's age relative to human age is {0}".format((gvmepet*8)+12))
elif animalage == "b":
    gvmepetname = input("What type of bird: \nPress 'B' for budgerigar\nPress 'P' for parrot\nPress 'C' for canary\n: ").lower()
    gvmepet = int(input("How old is your pet: "))
    if gvmepetname == "b":
        print("Budgerigar's age relative to human age is {0}".format((gvmepet*6)+10))
    elif gvmepetname == "p":
        print("Parrot's age relative to human age is {0}".format((gvmepet*2)+2))
    elif gvmepetname == "c":
        print("Canary's age relative to human age is {0}".format((gvmepet*8)+10))     
elif animalage == "h":
    print("Information! The ages of the hamsters are calculated in months, and the value you will write here is in months.")
    gvmepet = int(input("How old is your pet (in months): "))
    if 3 >= gvmepet > 0:
        print("Hamster's age relative to human age is {0}".format(((gvmepet-1.5)*6)+17))
    elif 12 >= gvmepet > 3:
        print("Hamster's age relative to human age is {0}".format((gvmepet*4)+10))
    elif 24 >= gvmepet > 12:
        print("Hamster's age relative to human age is {0}".format((gvmepet*1)+46))
    elif gvmepet > 24:
        print("Hamster's age relative to human age is {0} ".format((gvmepet*1.5)+46))   
elif animalage == "f":
    gvmepetname = input("What type of fish: \nPress 'P' for piranha\nPress 'K' for koi\nPress 'J' for japanese fish\
        \nPress 'L' for little fishes \n: ").lower()
    gvmepet = int(input("How old is your pet: "))
    if gvmepetname == "p":
        print("Piranha's age relative to human age is {0}".format((gvmepet*8)+2))
    elif gvmepetname == "k":
        print("Koi's age relative to human age is {0}".format((gvmepet*3)+3))
    elif gvmepetname == "j":
        print("Japanese fish's age relative to human age is {0}".format((gvmepet*8)+10))
    elif gvmepetname == "l":
        print("Little fish's age relative to human age is {0}".format(((gvmepet-1)*40)+30))      
else:
    print("We will also add other animal age calculations in the future.")