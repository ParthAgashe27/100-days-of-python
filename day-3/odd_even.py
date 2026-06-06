print("Welcome to Odd or Even checker!")
number = int(input("please enter a number: "))
if number < 0:
        print(f"The number {number} is negative, but it is still {'even' if number % 2 == 0 else 'odd'}.")
elif number == 0:
        print("The number 0 is not even nor odd.")
else:
        print(f"The number {number} is {'even' if number % 2 == 0 else 'odd'}.")
