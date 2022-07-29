from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def barrista():
        global sufficient_resources, enough_money, off
        #ask user choice
        choice = input("\r\nWelcome to the Coffee Bar \r\nWhat would you like? (espresso/latte/cappuccino): ").lower()
        #shut down if 'off' 
        if choice == 'off':
            print("Okay, shutting down ... ")
            off = True
        #generate report if 'report'
        elif choice == 'report':
            print(format_report(resources))
        #if choice is legit, ask for $ and decrement resources
        elif choice in MENU.keys():
            if check_resources(resources,resource_requirements,choice):
                cashier(money_dict,choice)
                decrement_resources(choice)
        else: 
            print("Sorry, that's not on the menu.  Please choose an espresso, latte, or cappuccino.")
        return choice