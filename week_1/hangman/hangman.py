import random
import hangmanart
import hangmanwords

# from hangmanwords import word_list (this will avoid having to use the prefix "hangmanwords." that just importing will need

lives = 6
print(hangmanart.logo)


chosen_word = random.choice(hangmanwords.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "-"
print("Word to guess: " + placeholder)

game_over = False
correct_letter = []
incorrect_letter = []
while not game_over:
    print(f"****************************{lives} LIVES LEFT****************************\n")
    print(f" Incorrect Guesses: {incorrect_letter}\n")
    guess = input("Guess a letter: ").lower()


    if guess in incorrect_letter:
        lives += 1
        print("You already guessed this letter")
        incorrect_letter.remove(guess)
    elif guess in correct_letter:
        print("You already guess this letter")

    display = ""

    
    for letter in chosen_word:
        if letter == guess:
            correct_letter.append(guess)
            display += letter
        elif letter in correct_letter:
            display += letter
        else:
            display += "-"
 
    print("Word to guess: " + display)

    if guess not in chosen_word: 
        lives -= 1 
        incorrect_letter.append(guess)
        print(f"\n***************The letter '{guess}' is not in the word. Try again.*****************")
        if lives == 0:
            game_over = True
            print(f"***********************THE WORD WAS {chosen_word.upper()} YOU LOSE**********************")

    if "-" not in display:
        print("****************************YOU WIN****************************")
        game_over = True

    print(hangmanart.stages[lives])
