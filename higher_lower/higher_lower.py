import random
from secrets import choice
from art import logo,vs
from game_data import data

#initialize score
score = 0

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
choice_A = select_record(data)
choice_B = select_record(data)

# present choices and collect answer
def present_choices():
    """prints logo and two random choices from game_data, takes in user answer"""
    print(logo)
    print(f"Compare A: {choice_A[0]}, a {choice_A[1]} from {choice_A[2]}")
    print(vs)
    print(f"Against B: {choice_B[0]}, a {choice_B[1]} from {choice_B[2]}")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    return answer

#judge_answer function
def judge_answer(answer,choice_A,choice_B):
    """determines higher follow count and if answer is correct"""    
    if choice_A[3] > choice_B[3]:
        higher = 'a'
        # print(f"{choice_A[0]} had more, with {choice_A[3]} follows")
    else: 
        higher = 'b'
        # print(f"{choice_B[0]} had more, with {choice_B[3]} follows")
    if answer == higher:
        score += 1
        print(f"You're right! Current score: {score}.  ")
        # swap HIGHER for new A
    else:
        print(f"Sorry, that's wrong.  Final score = {score}. ")
    return higher

print(present_choices())
# judge_answer(present_choices(),choice_A,choice_B)
