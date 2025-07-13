#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = random.randint(1, 12) 
nr_symbols = random.randint(1, 12) 
nr_numbers = random.randint(1, 12) 

password = [] 
passw = ""
for number in range(nr_letters):
    x = random.choice(letters)
    password += x   
for number in range(nr_symbols):
    y = random.choice(symbols)
    password += y    
for number in range(nr_numbers):
    z = random.choice(numbers)
    password += z

random.shuffle(password)

for number in password:
    passw += number

print(passw)

  


