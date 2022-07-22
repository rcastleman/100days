import random
from art import logo
from os import system, name

def clear():
    if name == 'nt':
        _ =system('cls')
    else:
        _ = system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# start_query = input("Do you want to play Blackjack?  ").lower()

# if start_query == "n":
#     exit()

# # def play_again():
#     choice = input("Would you like to play again?:  ").lower()
#     if choice == "y":
#         clear()
#         user_hand()
#     else:
#         game_over = True

game_over = False
# user_score = 0
# dealer_score = 0

# while not game_over:

#Angela's code

def calculate_score(cards):
    """Takes a list of cards and calculates score"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    elif 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def deal_card():
    """Returns a random card from the deck"""
    card = random.choice(cards)
    return card 

user_cards = []
dealer_cards = []

for _ in range(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

while game_over == False:

    user_score = calculate_score(user_cards)
    dealer_score = calculate_score(dealer_cards)

    print(f"Your cards: {user_cards} and current score: {user_score}")
    print(f"Dealer's first card: {dealer_cards[0]}")

    if user_score == 0 or user_score > 21 or dealer_score == 0:
        game_over = True
        print(f"Game Over! User Score = {user_score} and Dealer Score = {dealer_score}")
    else: 
        user_choice = input("Type 'y' to get another card or 'n' to pass:  ")
        if user_choice == 'y':
            user_cards.append(deal_card())
        else:
            game_over = True
            print(f"Game Over! User Score = {user_score} and Dealer Score = {dealer_score}")



# def user_hand():
#     user_first_card = random.choice(cards)
#     user_score += user_first_card
#     user_next_card = random.choice(cards)
#     user_score += user_next_card
#     if user_next_card == cards[0] and user_score > 21:
#         user_score = user_first_card + 1
#     return user_score,user_next_card

# def dealer_hand():
#     dealer_first_card = random.choice(cards)
#     dealer_score += dealer_first_card
#     dealer_next_card = random.choice(cards)
#     dealer_score += dealer_next_card
#     if dealer_next_card == cards[0] and dealer_score > 21:
#         dealer_score = dealer_first_card + 1
#     return dealer_score, dealer_next_card

# if dealer_score == 21:
#     print("Blackjack - dealer wins!")
#     game_over = True

# elif user_score == 21:
#     print("Blackjack - user wins!")
#     game_over = True

# elif user_score > 21:
#     print(f"Sorry, you're last card was {user_next_card} and your score hit {user_score}, so you busted")
#     game_over = True
#     play_again()

# else:
#     print(f"Your cards: [{user_first_card},{user_next_card}]. Current score: {user_score}")
#     print(f"Computer's first card: {dealer_first_card}")
#     user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
#     if user_choice == 'n':
#         dealer_hand()

