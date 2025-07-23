import random

logo = r"""

 __  _ _  _ __ __ __ ___ ___    __ _  _ ___  __   __  ___ ___  
|  \| | || |  V  |  \ __| _ \  / _] || | __/' _//' _/| __| _ \ 
| | ' | \/ | \_/ | -< _|| v / | [/\ \/ | _|`._`.`._`.| _|| v / 
|_|\__|\__/|_| |_|__/___|_|_\  \__/\__/|___|___/|___/|___|_|_\ 


"""

game = True


def main():
    computer_choice = random.randint(1, 100)
    difficulty = input("Would you like 'easy' or 'hard' mode?: ").lower()
    lives = 0
    game_over = False

    if difficulty == "easy":
        lives += 10
    elif difficulty == "hard":
        lives += 5
    else:
        print("Invalid input")

    while not game_over:
        lives, game_over = guess(computer_choice, lives)


def guess(computer_choice, lives):
    if lives == 0:
        return lives, True
    guess = int(input("What is your guess?: "))
    if guess < 1 or guess > 100:
        print("invalid input try again")
    elif guess == computer_choice:
        print("You Win")
        return lives, True
    elif guess > computer_choice:
        print(f"{guess} is too high, guess again.")
        lives -= 1
        print(f"Lives: {lives}")
    elif guess < computer_choice:
        print(f"{guess} is too low, guess again")
        lives -= 1
        print(f"Lives: {lives}")
    return lives, False


print(logo)
print(
    "Number Guesser!\nGuess the number I am thinking of between 1 and 100\
        \nEasy mode = 10 lives\nHard mode = 5 lives"
)

while game:
    main()
    if input("Play again?: 'y' or 'n' ").lower() == "y":
        game = True
    else:
        game = False
