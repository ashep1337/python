import pandas

# student_dict = {
#    "student": ["Angela", "James", "Lily"],
#    "score": [56, 76, 98]
# }

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#    #Access key and value
#    pass

# student_data_frame = pandas.DataFrame(student_dict)

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score
#    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

data = pandas.read_csv("nato_phonetic_alphabet.csv")
alphabet = {row.letter: row.code for index, row in data.iterrows()}
user_input = input("Enter your name: ")

while True:
    letters_list = [letter.upper() for letter in user_input]
    output = [alphabet[letter] for letter in letters_list if letter in alphabet]

    if output == []:
        print("\nPlease enter valid characters. \n")
        user_input = input("Enter your name: ")
    else:
        print(output)
        break
