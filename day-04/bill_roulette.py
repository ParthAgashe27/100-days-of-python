import random
print("Welcome to the Russian Roulette Bill Paying Edition")
bill_payers = input("Enter the names of the bill payers, separated by a comma: ")
bill_payers_names = bill_payers.split(", ")
print(f"{random.choice(bill_payers_names)} is going to pay the bill today!")  

