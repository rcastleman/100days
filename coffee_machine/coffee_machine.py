import resource
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 10}

def format_report(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = "${:.2f}".format(resources['money'])
    return f"Water: {water} ml \nMilk: {milk} ml \nCoffee: {coffee} g \nMoney: {money}"

# print(format_report(resources))

# TODO Turn off the Coffee Machine by entering “ off ” to the prompt.
"""For maintainers of the coffee machine, they can use 'off' as the secret word to turn off
the machine. Your code should end execution when this happens."""
# flag = True
# while flag: 


# TODO Check resources sufficient?
# TODO If sufficient resources, process coins
# TODO transaction successful? Give change Give coffee
# TODO “Here is your {coffee choice}. Enjoy!”.

# Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
def get_choice():
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice in MENU.keys():
        print(f"One {choice} coming right up ... ")
    else: 
        print("Sorry, that's not on the menu.  Please choose an espresso, latte, or cappuccino.")
    #CHECK IF RESOURCES ADEQUATE
    return choice

get_choice()
