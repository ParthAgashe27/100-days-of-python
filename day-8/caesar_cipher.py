alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):
    result = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == "encode":
                new_position = (position + shift) % 26
            else:
                new_position = (position - shift) % 26
            result += alphabet[new_position]
        else:
            result += letter
    print(result)

in_progress = True

while in_progress:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)
    
    user_response = input("Would you like to continue? 'yes' or 'no':\n").lower()
    if user_response == "no":
        in_progress = False
        print("Goodbye!")
