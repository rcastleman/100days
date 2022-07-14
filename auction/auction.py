# from replit import clear
from art import logo

# print(logo)

auction_dict = {'Tom':100,'Bob':50}

def find_winner(auction_dict):
    winner = {'name':0}
    for bidder in auction_dict:
        if bidder[1] > winner[1]:
            winner[0] = bidder[0]
            winner[1] = bidder[1]
    print(winner)

find_winner(auction_dict)

# def run_auction():
    
#     name = input("Name: ")
#     bid_price = input("Bid Price: ")
#     auction_dict["name"] = name
#     auction_dict["bid price"] = bid_price
#     choice = input("Is there another bidder?").lower()
#     if choice == "no":
#         print(f"the bidders are {auction_dict}")
#         # print("Let's find a winner...")
#         # find_winner()
#         return auction_dict
#     elif choice == "yes":
    
#         # clear()

# run_auction()