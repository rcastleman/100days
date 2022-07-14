from os import system, name
from art import logo

def clear():
    if name == 'nt':
        _ =system('cls')
    else:
        _ = system('clear')

print(logo)

def find_winner(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of {highest_bid}")
    
bids = {}
bidding_finished = False

while bidding_finished == False:
    name = input("Name: ")
    price = int(input("Bid Price: "))
    bids[name] = price
    should_continue = input("Any other users to bid (yes or no)?").lower()
    if should_continue == "no":
        bidding_finished = True
        print(find_winner(bids))
    elif should_continue == "yes":
        clear()
