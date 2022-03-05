from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create objects and variables that will be used in code
menu = Menu()
coffee_maker = CoffeeMaker()
my_money = MoneyMachine()
machine_status = "on"

while machine_status == "on":

    options = menu.get_items() # pulls what is on the menu
    order = input(f"What drink would you like ({options})? ").lower()
    drink = menu.find_drink(order) # checks to see if what is ordered against what is on the drinks menu

    if order == "off":
        print("Coffee Machine shutting down 📴")
        machine_status = "off"
    elif order == "report":
        coffee_maker.report()
        my_money.report()
    elif drink != "None":
        if coffee_maker.is_resource_sufficient(drink) is True:
            if my_money.make_payment(drink.cost) is True:
                coffee_maker.make_coffee(drink)
