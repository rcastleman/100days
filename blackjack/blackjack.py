import random
from art import logo
from os import system, name

def clear():
    if name == 'nt':
        _ =system('cls')
    else:
        _ = system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

start_query = input("Do you want to play Blackjack?  ").lower()
if start_query == "n":
    exit()

game_over = False
user_score = 0
dealer_score = 0

# while not game_over:

user_first_card = random.choice(cards)
user_score += user_first_card
user_next_card = random.choice(cards)
user_score += user_next_card
if user_next_card == cards[0] and user_score > 21:
    user_score = user_first_card + 1

dealer_first_card = random.choice(cards)
dealer_score += dealer_first_card
dealer_next_card = random.choice(cards)
dealer_score += dealer_next_card
if dealer_next_card == cards[0] and dealer_score > 21:
    dealer_score = dealer_first_card + 1

if dealer_score == 21:
    print("Blackjack - dealer wins!")
    game_over = True

if user_score == 21:
    print("Blackjack - user wins!")
    game_over = True

if user_score > 21:
    print(f"Sorry, you're last card was {user_next_card} and your score hit {user_score}, so you busted")
    game_over = True
else:
    print(f"Your cards: [{user_first_card},{user_next_card}]. Current score: {user_score}")
    print(f"Computer's first card: {dealer_first_card}")
    user_choice = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_choice == 'n':
        game_over = True
        clear()
# else:
    # deal_cards()

