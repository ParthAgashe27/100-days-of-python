import machine_data
import art

coffee_machine_supply = {

    'water': 2000,
    'milk': 1000,
    'coffee':150

}   
machine_money = 0 

def machine_report():
        machine_water = coffee_machine_supply["water"]
        machine_milk = coffee_machine_supply["milk"]
        machine_coffee = coffee_machine_supply["coffee"]
        
        return (f"The amount of water in coffee machine is {machine_water}ml\n The amount of milk in coffee machine is {machine_milk}ml\n The amount of coffee in coffee machine is {machine_coffee}gm\n The amount of money in coffee machine is ${machine_money:.2f}")

    
def coffee(coffee_name):

    global machine_money
    
    coffee_ingredients = machine_data.MENU[coffee_name]["ingredients"]
    coffee_ingredients_water = coffee_ingredients["water"]
    coffee_ingredients_milk = coffee_ingredients["milk"]
    coffee_ingredients_coffee = coffee_ingredients["coffee"]
    coffee_machine_money = machine_data.MENU[coffee_name]["cost"]

    coffee_machine_water = coffee_machine_supply["water"]
    coffee_machine_milk = coffee_machine_supply["milk"]
    coffee_machine_coffee = coffee_machine_supply["coffee"]


    if coffee_machine_water >= coffee_ingredients_water and coffee_machine_milk >= coffee_ingredients_milk and coffee_machine_coffee >= coffee_ingredients_coffee:
        
        print("Please insert the coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickles = int(input("How many nickles?: "))
        pennies = int(input("How many pennies?: "))
        user_money = 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies

        if user_money >= coffee_machine_money:

            change = user_money - coffee_machine_money
            machine_money += coffee_machine_money

            coffee_machine_supply["water"] -= coffee_ingredients_water
            coffee_machine_supply["milk"] -= coffee_ingredients_milk
            coffee_machine_supply["coffee"] -= coffee_ingredients_coffee

                # THE RECEIPT GENERATOR:
            receipt = f"""
=========================================
            COFFEE MACHINE v1.0
    Active Profile: [The Client]
=========================================
ORDER: {coffee_name.title()}
-----------------------------------------
Water deducted:   -{coffee_ingredients_water} ml  (Tank: {coffee_machine_supply['water']})
Milk deducted:    -{coffee_ingredients_milk} ml  (Tank: {coffee_machine_supply['milk']})
Coffee deducted:   -{coffee_ingredients_coffee} gm  (Tank: {coffee_machine_supply['coffee']})

Coins inserted:    $ {user_money:.2f}
Drink Cost:        $ {coffee_machine_money:.2f}
Change dispensed:  $ {change:.2f}

STATUS: [ 200 OK - BREW SUCCESSFUL ]
=========================================
    "Here is your {coffee_name}. Enjoy!"
=========================================
            """
            print(receipt)

        elif user_money < coffee_machine_money:

            print(f"Sorry that's not enough money. Money refunded. ${user_money:.2f}")

    else:
        print("Sorry there is not enough ingredients in the coffee machine. Please contact The Admin.")
        
print(art.main_logo)

while True:

    user_input = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_input == "off":
        print(art.maintenance)

        break

    elif user_input == "report":
        print(machine_report())

    elif user_input in ["espresso", "latte", "cappuccino"]:
        coffee(user_input)

    elif user_input == "refill":
        coffee_machine_supply["water"] = 2000
        coffee_machine_supply["milk"] = 1000
        coffee_machine_supply["coffee"] = 150
        print("🛠️ Route Operator recognized. All ingredient tanks restored to 100%.")
    

