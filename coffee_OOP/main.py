from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
cashier = MoneyMachine()
menu = Menu()

machine_on = True
while machine_on:
    def barrista():
            global machine_on
            options = menu.get_items()
            choice = input(f"\r\nWelcome to the Coffee Bar \r\nWhat would you like? ({options}): ").lower()
            if choice == 'off':
                print("Okay, shutting down ... ")
                machine_on = False
            elif choice == 'report':
                machine.report()
                cashier.report()
            else:
                drink = menu.find_drink(choice)
                if (machine.is_resource_sufficient(drink)) and cashier.make_payment(drink.cost):
                        machine.make_coffee(drink)
    barrista()