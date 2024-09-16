allNumb = []

try:
    numb = int(input("How many numbers do you want to compare: "))
except ValueError:
    print("Idiot I'll give you a chance again write the number my boy")
    try:
        numb = int(input("How many numbers do you want to compare: "))
    except ValueError:
        print("BB beybi")
    exit()

for nb in range(1, numb + 1):
    try:
        number = float(input(f"Write the {nb}. number: "))
        allNumb.append(number)
    except ValueError:
        print(f"Invalid input for the {nb}. number. Exiting the program.")
        exit()

maxi = max(allNumb)
mini = min(allNumb)

if mini != 0:
    timis = maxi / mini
else:
    timis = "undefined (division by zero)"

print("Largest of the given numbers = ",maxi,
"\nSmallest of the given numbers = ",mini,
"\nThe difference between them (x) = ",timis)
