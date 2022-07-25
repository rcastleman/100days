import random
from art import logo,vs
from game_data import data
from os import system, name

def clear():
    if name == 'nt':
        _ =system('cls')
    else:
        _ = system('clear')

def format_data(account):
    """Takes the account data and returns a printable format"""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name},a {account_descr},from {account_country}"

def check_answer(guess,a_followers,b_followers):
    """check if user guess is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
     
#display art
print(logo)
score = 0
game_continue = True
account_b = random.choice(data)


#make game repeateable
while game_continue == True:
    #generate random record
    account_a = account_b
    account_b = random.choice(data)
    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Against B: {format_data(account_b)}")

    #ask user for guess
    guess = input("Who has more followers? Type 'A' or 'B':  ").lower() 

    #check user guess
    ##get follower count
    a_follower_count = account_a['follower_count']
    b_follower_count = account_b['follower_count']
    is_correct = check_answer(guess,a_follower_count,b_follower_count)

    clear()
    print(logo)

    #give user feedback
    #score keeping

    if is_correct:
        score += 1
        print(f"You're right!  Current score: {score}")
    else:
        game_continue = False
        print(f"Sorry, that's wrong. Final score: {score}")


#move record at Position B to Position A

#clear the screen bewteen rounds

