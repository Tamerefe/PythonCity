from random import randrange

coinr = randrange(100)

ttlslctcoin = 0

slctcoin = input("You can select 50c 25c 10c 5c 1c: ")

while True: 
    if not (slctcoin in("50","25","10","5","1")):
        slctcoin = input("Try Again, You can select 50c 25c 10c 5c 1c: ")
        print("Please just write number not use c value:")
    else:
        slctcoin = int(slctcoin)
        
        ttlslctcoin += slctcoin
        print("Your coin value is {}c".format(ttlslctcoin))

        if ttlslctcoin == coinr:
            print("Congratulations you won the game")
            break
        elif ttlslctcoin >= coinr:
            print("Sorry you lose that value too much")
            break
        elif ttlslctcoin <= coinr:
            slctcoin = input("You can select 50c 25c 10c 5c 1c: ")
