#bug: used > so 18 produced no output, didnt use try: with valueError.
#fix: change > to >= and added try and except ValueError.
try:
    age = int(input("How old are you?"))
    if age >= 18:
        print(f"You can drive at age {age}.")
except ValueError:
    print("Please input a valid numerical input")
