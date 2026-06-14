import calculator_art

print(calculator_art.logo)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/":divide
}
program = True

def calculation():
    global program

    number1 = float(input("What's the first number?: "))

    for key in operations_dictionary:
        print(key)
    
    operation = input("Pick an operation:")
    
    number2 = float(input("What's the second number?: "))
    
    result = operations_dictionary[operation](number1, number2)
    print(f"{number1} {operation} {number2} = {result}")

    user_input = input(f"Would you like to continue calculation with {result} type 'y' to continue or type 'n' to start a new calculation:").lower()
    if user_input == "n":
        calculation()
    else:
        
        while program == True:
            number1 = result
            for key in operations_dictionary:
                print(key)
    
            operation = input("Pick an operation:")
            number3 = float(input("What's the next number?:"))
            result = operations_dictionary[operation](number1, number3)
            print(f"{number1} {operation} {number3} = {result}")


calculation()
