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
            #ask user choice
            choice = input("\r\nWelcome to the Coffee Bar \r\nWhat would you like? (espresso/latte/cappuccino): ").lower()
            #shut down if 'off' 
            if choice == 'off':
                print("Okay, shutting down ... ")
                machine_on = False
            #generate report if 'report'
            elif choice == 'report':
                CoffeeMaker.report(machine)
            #is choice in Menu? 
            elif menu.find_drink(choice) and machine.is_resource_sufficient(choice):
                #create MenuItem object??
                # order = MenuItem(ARGS????)
                #ask for money
                # cashier.process_coins()
                # cashier.make_payment(MenuItem)
                # machine.make_coffee(choice)
                return choice

    barrista()