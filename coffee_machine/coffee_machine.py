from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0}

def format_report(resources):
    return f"Water: {resources['water']}"
    return f"Milk: {resources['milk']}"
    return f"Coffee: {resources['coffee']}"
    return f"Money: {resources['money']}"

print(format_report(resources=))

# TODO Turn off the Coffee Machine by entering “ off ” to the prompt.
"""For maintainers of the coffee machine, they can use 'off' as the secret word to turn off
the machine. Your code should end execution when this happens."""
# flag = True
# while flag: 

# TODO Print report.


# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# TODO Check resources sufficient?
# TODO If sufficient resources, process coins
# TODO transaction successful? Give change Give coffee
# TODO “Here is your {coffee choice}. Enjoy!”.

# Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
# choice = input("What would you like? (espresso/latte/cappuccino): ")
