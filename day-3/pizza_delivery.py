print("Welcome to Pizza Delivery!")
Bill_of_pizza_delivery = 0
size_of_pizza = input("What size of pizza do you want? S, M, or L: ").upper()  #The user will be prompted to choose the size of the pizza they want to order. The available sizes are Small (S), Medium (M), and Large (L). Depending on the size selected, the base price of the pizza will be added to the total bill. The prices for each size are as follows: Small pizza costs $15, Medium pizza costs $20, and Large pizza costs $25. If the user selects an invalid size, an error message will be displayed.
if size_of_pizza == "S":
    Bill_of_pizza_delivery += 15
elif size_of_pizza == "M":
    Bill_of_pizza_delivery += 20
elif size_of_pizza == "L":
    Bill_of_pizza_delivery += 25
else:
    print("Invalid size selected.")
    exit()

add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()   #pepperoni is an optional add-on for the pizza, and the cost of adding pepperoni depends on the size of the pizza. If the user wants to add pepperoni, they will be charged an additional $2 for a small pizza and $3 for medium or large pizzas. If the user does not want to add pepperoni, there will be no additional charge.
if add_pepperoni == "Y":
    if size_of_pizza == "S":
        Bill_of_pizza_delivery += 2
    else:
        Bill_of_pizza_delivery += 3

add_extras = input("Do you want extra cheese? Y or N: ").upper()  #extra cheese is another optional add-on for the pizza, and if the user wants to add extra cheese, they will be charged an additional $1 regardless of the size of the pizza. If the user does not want to add extra cheese, there will be no additional charge.
if add_extras == "Y":
    if size_of_pizza == "S":
        Bill_of_pizza_delivery += 3
    else:
        Bill_of_pizza_delivery += 4

print(f"Your total bill is ${Bill_of_pizza_delivery}.")
