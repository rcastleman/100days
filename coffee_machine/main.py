import resource
from sys import last_type
from menu import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0}

price_list = {
    "espresso": 1.5,
    "latte": 2.50,
    "cappucino": 3.50}

resource_requirements = {
    "espresso": {"water":50,
    "coffee":18,
    "milk":0 },
    "latte":{"water":200,
    "coffee":24,
    "milk":150 },
    "cappucino": {"water":250,
    "coffee":24,
    "milk":100}}

money_dict = {
    "quarters":0.25,
    "dimes":0.10,
    "nickels": 0.05,
    "pennies":0.01}

# for i in resource_requirements:
#     print(f"The water requirement for {i} is {resource_requirements[i]['water']}")

sufficient_resources = True

def cashier(money_dict,choice):
    global sufficient_resources
    print("Please insert coins.")
    quarters = float(input("How many quarters?:  "))
    dimes = float(input("How many dimes?:  "))
    nickels = float(input("How many nickels?:  "))
    pennies = float(input("How many pennies?:  "))
    paid = money_dict["quarters"]*quarters + money_dict["dimes"]*dimes + money_dict["nickels"]*nickels + money_dict["pennies"]*pennies
    f_paid = "${:.2f}".format(paid) #formatted total
    print(f"You paid: {f_paid}")
    resources["money"] = paid

    #check sufficiency against price
    price = price_list[choice]
    f_price = "${:.2f}".format(price)
    print(f"The price for your {choice} is {f_price}")
    if price > paid:
        difference = price - paid
        f_diff ="${:.2f}".format(difference)
        print(f"Sorry, you haven't paid enough. You're short  {f_diff}")
        sufficient_resources = False
    else:
        difference = paid - price
        f_diff ="${:.2f}".format(difference)
        print(f"Thank you. Your change is: {f_diff} ")
        sufficient_resources = True

def format_report(resources):
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    money = "${:.2f}".format(resources['money'])
    return f"Water: {water} ml \nMilk: {milk} ml \nCoffee: {coffee} g \nMoney: {money}"



#ACTIVE LOOP

# off = False

# while not off:

    # def machine_on():
        # pass

# TODO Check resources sufficient?
# TODO If sufficient resources, process coins
# TODO transaction successful? Give change Give coffee
# TODO “Here is your {coffee choice}. Enjoy!”.

# Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
def barrista():
    global sufficient_resources
    print(f"Sufficient resources state: {sufficient_resources}")
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        off = True
    elif choice == 'report':
        print(format_report(resources))
    elif choice in MENU.keys(): #and sufficient_resources == True:
        print(f"One {choice} coming right up ... ")
    else: 
        print("Sorry, that's not on the menu.  Please choose an espresso, latte, or cappuccino.")
    #CHECK IF RESOURCES ADEQUATE
    return choice

barrista()