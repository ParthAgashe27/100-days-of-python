# DAY 3 Mini Project - Rollercoaster

print("Welcome to the rollercoaster!")
height_of_customer = float(input("Enter the height of the customer in cm: "))
bill_of_rollercoaster = 0
if height_of_customer >= 120:
    print("You can ride the rollercoaster!")
    age_of_customer = int(input("Enter the age of the customer: "))
    if 18 <= age_of_customer < 45:
        bill_of_rollercoaster = 12
        print("Please pay for Adult tickets $12.")
    elif 45 <= age_of_customer <= 55:
        bill_of_rollercoaster = 0
        print("You qualify for a free ride!")
    else:
        bill_of_rollercoaster = 5
        print("Please pay for Child tickets $5.")
    wants_photo = input("Do you want a photo taken? Type y for Yes or n for No: ")
    if wants_photo == "y":
        bill_of_rollercoaster += 3
    print(f"Your total bill is ${bill_of_rollercoaster}.")
else:
    print("Sorry, you have to grow taller before you can ride.")
