import resource
from menu import MENU

#global variables
off = False
sufficient_resources = True
enough_money = False

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0}

price_list = {
    "espresso": 1.5,
    "latte": 2.50,
    "cappuccino": 3.50}

resource_requirements = {
    "espresso": {"water":50,
    "coffee":18,
    "milk":0 },
    "latte":{"water":200,
    "coffee":24,
    "milk":150 },
    "cappuccino": {"water":250,
    "coffee":24,
    "milk":100}}

money_dict = {
    "quarters":0.25,
    "dimes":0.10,
    "nickels": 0.05,
    "pennies":0.01}

def cashier(money_dict,choice):
    print("Please insert coins.")
    quarters = float(input("How many quarters?:  "))
    dimes = float(input("How many dimes?:  "))
    nickels = float(input("How many nickels?:  "))
    pennies = float(input("How many pennies?:  "))
    paid = money_dict["quarters"]*quarters + money_dict["dimes"]*dimes + money_dict["nickels"]*nickels + money_dict["pennies"]*pennies
    f_paid = "${:.2f}".format(paid) #formatted total
    print(f"You paid: {f_paid}")
    resources["money"] += paid

    price = price_list[choice]
    f_price = "${:.2f}".format(price)
    print(f"The price for your {choice} is {f_price}")
    if price > paid:
        difference = price - paid
        f_diff ="${:.2f}".format(difference)
        print(f"Sorry, you haven't paid enough. You're short  {f_diff}")
    else:
        difference = paid - price
        f_diff ="${:.2f}".format(difference)
        print(f"Thank you. Your change is: {f_diff} ")

def format_report(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = "${:.2f}".format(resources['money'])
    return f"Water: {water} ml \nMilk: {milk} ml \nCoffee: {coffee} g \nMoney: {money}"

def check_resources(resources,resource_requirements,choice):
    global sufficient_resources
    if resource_requirements[choice]["water"] > resources["water"]:
        sufficient_resources = False
        print(f"Sorry, there's not enough water for a {choice}")
    elif resource_requirements[choice]["milk"] > resources["milk"]:
        sufficient_resources = False
        print(f"Sorry, there's not enough milk for a {choice}")
    elif resource_requirements[choice]["coffee"] > resources["coffee"]:
        sufficient_resources = False
        print(f"Sorry, there's not enough coffee for a {choice}")
    else:
        sufficient_resources = True

# check_resources(resources,resource_requirements,"cappuccino")

choice = 'latte'
print(resource_requirements[choice]["water"], "vs", resources["water"])
print(resource_requirements[choice]["milk"] > resources["milk"])
print(resource_requirements[choice]["coffee"] > resources["coffee"])

while not off:

    def barrista():
        global sufficient_resources, enough_money, off
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == 'off':
            print("Okay, shutting down ... ")
            off = True
        elif choice == 'report':
            print(format_report(resources))
        elif choice in MENU.keys():
            if sufficient_resources == True:
                cashier(money_dict,choice)
        else: 
            print("Sorry, that's not on the menu.  Please choose an espresso, latte, or cappuccino.")
        return choice

    # barrista()

#TODO decrement resources
#TODO increment / decrement