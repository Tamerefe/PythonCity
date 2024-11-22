import random

while True:
    rastgele = random.randint(1, 9)
    number = int(input("Enter a Number: "))
    print("The Number Was: ", rastgele)

    if number == rastgele:
        print("Congratulations! You guessed the number!")
    else:
        input("Unlucky! Better luck next time. Press Enter to continue.")
