import random
from secrets import choice
from art import logo,vs
from game_data import data

#function for picking a random record
def select_record(data):
    """chooses random record from data"""
    index = random.randint(0,len(data))
    name = data[index]['name']
    description = data[index]['description']
    country = data[index]['country']
    followers = data[index]['follower_count']
    return name,description,country,followers

#generate initial two choices
initial_A = select_record(data)
initial_B = select_record(data)

#initialize score
score = 0

# present choices and collect answer
def present_choices():
    """shows two choices from game_data, takes user answer"""
    print(logo)
    global score
    if score == 0:
        print(f"[init]Compare A: {initial_A[0]}, a {initial_A[1]} from {initial_A[2]}")
        print(vs)
        print(f"Against B: {initial_B[0]}, a {initial_B[1]} from {initial_B[2]}")
        choice_1 = initial_A
        choice_2 = initial_B    
    else:
        choice_A = select_record(data)
        choice_B = select_record(data)
        print(f"Compare A: {choice_A[0]}, a {choice_A[1]} from {choice_A[2]}")
        print(vs)
        print(f"Against B: {choice_B[0]}, a {choice_B[1]} from {choice_B[2]}")
        choice_1 = choice_A
        choice_2 = choice_B
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    print(f"user answer = {answer}")
    return answer,choice_1,choice_2

#judge_answer function,increment score or end game
def judge_answer(answer,choice_1,choice_2):
    """determines higher follow count and if answer is correct"""    
    if choice_1[3] > choice_2[3]:
        higher = 'a'
        # print(f"{choice_A[0]} had more, with {choice_A[3]} follows")
    else: 
        higher = 'b'
        #if higher is Choice B, Choice B becomes Choice A for next round 
        choice_1 = choice_2
        # print(f"{choice_B[0]} had more, with {choice_B[3]} follows")
    if answer == higher:
        score += 1
        print(f"You're right! Current score: {score}.  ")
        present_choices()
    else:
        print(f"Sorry, that's wrong.  Final score = {score}. ")
        game_over = True
    return higher

present_choices()
# game()