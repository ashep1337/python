 
#n1 = 0
#n2 = 0
#name1 = input("1: ")
#name2 = input("2: ")

#for letter in name1:
#    for char in "true":
#        if letter == char:
#            n1 += 1

#for letter in name2:
#    for char in "love":
#        if letter == char:
#            n2 += 1

#print(n1, n2)


def calculate_love_score(name1, name2):
    n1 = 0 
    n2 = 0
    for letter in name1:
        for char in "true":
            if letter == char:
                n1 += 1
                n2 += 1
                                                                                    
    for letter in name1:
        for char in "love":
            if letter == char:
                n1 += 1
                n2 += 1
    print(f"Love Score = {n1}")

calculate_love_score("Kanye West", "Kim Kardashian") 
