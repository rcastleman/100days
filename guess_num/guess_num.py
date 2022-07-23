# from art import logo
import random
from os import system, name

def clear():
    if name == 'nt':
        _ =system('cls')
    else:
        _ = system('clear')

# print(logo)

#welcome
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

tries_left = 0

#user chooses level
difficulty = input ("Choose a difficulty: type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    tries_left = 10
else:
    tries_left = 5

#choose number
num = random.randint(1,100)
print(f"(the secret numbers is {num})")
print(f"You have {tries_left} tries left")
guess = int(input("Make a guess:  "))

# game_over = False

# while game_over == False:
def evaluate_guess():
    global tries_left, guess, game_over
    if tries_left < 1:
        print("Game Over! You ran out of tries.")
        # game_over = True
        return 
    if guess == num:
        print(f"You guessed the number ({num})!")
        # game_over = True
        return
    elif guess < num:
        tries_left -= 1
        guess = int(input(f"Too low. You have {tries_left} tries left.  Guess again:  "))
        evaluate_guess()
    elif guess > num:
        tries_left -= 1
        guess = int(input(f"Too high. You have {tries_left} tries )left.  Guess again:  "))
        evaluate_guess()

evaluate_guess()

# while input("Do you want to play again? Type 'y' or 'n'") == "y":
#     clear()
#     play_game()