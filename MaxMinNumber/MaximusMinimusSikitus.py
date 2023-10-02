allNumb = []

try:
    numb = int(input("How many number do you want for to compare: "))
except ValueError:
    print("Idiot I'll give you a chance again write the number my boy")
    try:
        numb = int(input("How many number do you want for to compare: "))
    except ValueError:
        print("BB beybi")
    exit()

for nb in range(numb):
    nb += 1
    allNumb.append(float(input(f"Write {nb}. number: ")))

maxi = max(allNumb)
mini = min(allNumb)

timis = maxi/mini 

print("Largest of the given numbers = ",maxi,
"\nSmallest of the given numbers = ",mini,
"\nThe difference between them (x) = ",timis)
