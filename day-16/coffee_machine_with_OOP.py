from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    user_input = input(f"What would you like? ({menu.get_items()}):  ").lower()
    if user_input == "off":
        break
    elif user_input == "report":
        coffee_maker.report()
        money_machine.report()
    elif user_input in ["espresso", "latte", "cappuccino"]:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
   
