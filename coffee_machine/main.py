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
    #ask for money
    print("Please insert coins.")
    quarters = float(input("How many quarters?:  "))
    dimes = float(input("How many dimes?:  "))
    nickels = float(input("How many nickels?:  "))
    pennies = float(input("How many pennies?:  "))
    #calculate total paid
    paid = money_dict["quarters"]*quarters + money_dict["dimes"]*dimes + money_dict["nickels"]*nickels + money_dict["pennies"]*pennies
    f_paid = "${:.2f}".format(paid) #formatted total
    print(f"You paid: {f_paid}")
    resources["money"] += paid
    #determine if amount paid is sufficient
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
        print(f"Sorry, there's not enough water for your {choice}")
    elif resource_requirements[choice]["milk"] > resources["milk"]:
        sufficient_resources = False
        print(f"Sorry, there's not enough milk for your {choice}")
    elif resource_requirements[choice]["coffee"] > resources["coffee"]:
        sufficient_resources = False
        print(f"Sorry, there's not enough coffee for your {choice}")
    else:
        print(f"Good news, resources are sufficient to make your {choice}!")
        sufficient_resources = True
    return sufficient_resources

def decrement_resources(choice):
    resources["water"] -= resource_requirements[choice]["water"]
    resources["milk"] -= resource_requirements[choice]["milk"]
    resources["coffee"] -= resource_requirements[choice]["coffee"]

while not off:

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

    barrista()
