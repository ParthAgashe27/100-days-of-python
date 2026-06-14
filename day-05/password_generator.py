import random
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
print("Welcome to the PyPassword Generator!")
py_number = int(input("How many numbers would you like in your password?\n"))
py_symbol = int(input("How many symbols would you like in your password?\n"))
py_alphabet = int(input("How many letters would you like in your password?\n"))
password = []  # Initialize an empty list to store the characters of the password
for number1 in range(1, py_number + 1):    
    password += random.choice(number)

for symbol1 in range(1, py_symbol + 1):
    password += random.choice(symbols)
    
for alphabet1 in range(1, py_alphabet + 1):
    password += random.choice(alphabet)

random.shuffle(password)  # Shuffle the characters in the password to make it more secure
final_password = ''.join(password)  # Join the list of characters into a single string

print(f"Your generated password is: {final_password}")
