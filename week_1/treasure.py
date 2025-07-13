print("Welcome to treasure island! ")
print("Your mission is to find the treasure!")
print("You're at a crossroads. Where do you want to go? ")
n = input("Type 'left' or 'right' ").lower()

if (n == "left"):
    n = input(" Type 'swim' or 'wait' ").lower()
    if (n == "wait"):
        n = input("Which door? 'red', 'yellow', or 'blue' ").lower()
        if (n == "yellow"):
            print("You Win!!!!")
        elif (n == "red"):
            print("Burned by fire game over")
        elif (n == "blue"):
            print("Eaten by beasts game over")
        else:
            print("Game over")
    else:
        print("attacked by trout game over")
else: 
    print("Fell in hole game over")
