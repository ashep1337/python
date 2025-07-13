import random


# Rock Paper Scissors ASCII Art

# Rock
r = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

# Paper
p = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

# Scissors
s = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

#print(r, p, s)

choice = [r, p, s]
user_choice = int(input("Choose:\n '0' for rock\n '1' for paper\n '2' for scissors\n" ))
#user_choice = (choice[n]) 
computer_choice = random.randint(0,2)
#print(f"You chose: Computer chooses: {choice[computer_choice]}\n Computer Chose:")

#if user_choice < 0 or user_choice > 2:
#    print("Invalid Entry")
#else:
#    print(f"You chose: Computer chooses: {choice[computer_choice]}\n Computer Chose:")

#if(user_choice == 0):
#    print("You chose: ", r)
#if(user_choice == 1):
#    print("You chose: ", p)
#if(user_choice == 2):
#    print("You chose: ", s)

#if(computer_choice == 0):
#    print("Computer chose: ", r)   
#if(computer_choice == 1):
#    print("Computer chose: ", p)
#if(computer_choice == 2):
#    print("Computer chose: ", s)
if user_choice < 0 or user_choice > 2:
    print("Invalid entry")
elif(user_choice == 0 and computer_choice == 2):
    print(f"You chose: {choice[user_choice]}\n Computer Chose: {choice[computer_choice]}\n You win!")
elif(user_choice == 1 and computer_choice == 0):
    print(f"You chose: {choice[user_choice]}\n Computer Chose: {choice[computer_choice]}\n You win!")
elif(user_choice == 2 and computer_choice == 1):
    print(f"You chose: {choice[user_choice]}\n Computer Chose: {choice[computer_choice]}\n You win!")
elif(user_choice == computer_choice):
        print(f"You chose: {choice[user_choice]}\n Computer Chose: {choice[computer_choice]}\n Draw.") 
else:
    print(f"You chose: {choice[user_choice]}\n Computer Chose: {choice[computer_choice]}\n You lose")

