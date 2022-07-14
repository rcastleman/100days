from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

def find_winner(dict):
    high_bidder = {'name':'bid'}
    for name in dict:
        if name['bid'] > high_bidder['name']
        high_bidder['name'] = name
        high_bidder['bid']


def run_auction():
    auction_dict = {}
    flag = True
    while flag = True
    name = input("Name: ")
    bid_price = input("Bid Price: ")
    auction_dict["name"] = name
    auction_dict["bid price"] = bid_price
    choice = input("Is there another bidder?")
    if choice == "No":
        flag = False
        find_winner()
    elif choice  == "Yes":
        clear()

run_auction()