from numpy import tri
from art import logo
import random

print(logo)

print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
difficulty = input ("Choose a difficulty: type 'easy' or 'hard': ").lower()
if difficulty == 'easy':
    diff_level = 10
else:
    diff_level = 5

tries_left = diff_level

# def tries_left():
#     print(f"You have {diff_level} attempts remaining to guess the number.")
# tries_left()

num = random.randint(1,100)
print(f"(the secret numbers is {num})")

while diff_level > 0:
    game_over = False
    guess = input("Make a guess:  ")
    print(f"You have {tries_left} tries left")
    if guess == num:
        print(f"You guessed the number ({num})!")
        game_over = True

