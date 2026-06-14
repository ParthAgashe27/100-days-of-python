print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 5, 10, 15, or 20? "))
Final_Bill = bill + tip/100 * bill
print("The total bill including tip is: $", round(Final_Bill, 2))
