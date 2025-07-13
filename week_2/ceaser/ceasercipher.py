from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
repeat = True

print(logo)

def ceaser(original_text, shift_amount, encode_decode):
    encryption = ""
    
    if encode_decode == "decode":
        shift_amount *= -1

    for n in original_text:
        if n not in alphabet:
            encryption += n    
        elif n in alphabet:
            cyphertext = alphabet.index(n) + shift_amount
            cyphertext %= len(alphabet)
            encryption += alphabet[cyphertext]

    print(encryption)

while repeat:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))


    ceaser(original_text=text, shift_amount=shift, encode_decode=direction)

    go_again = input("Go again? ")

    if go_again == "yes":
        repeat = True
    else:
        repeat = False
        print("Thanks for encrypting!")


    

