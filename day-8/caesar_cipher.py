alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift, direction):  
    result = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter) #identifies the position of letter in text 
            if direction == "encode":
                new_position = (position + shift) % 26 # to continue the alphabet list
            else:
                new_position = (position - shift) % 26
            result += alphabet[new_position] # to encrypt and decrypt
        else:
            result += letter #skips symbols
    print(result)

in_progress = True # controls whether the program continues running

while in_progress: #loop of encode and decode
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    
    caesar(text, shift, direction)
    
    user_response = input("Would you like to continue? 'yes' or 'no':\n").lower()
    if user_response == "no":
        in_progress = False
        print("Goodbye!")
