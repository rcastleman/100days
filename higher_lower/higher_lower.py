import random
from art import logo,vs
from game_data import data

#initialize score
score = 0

#select random record
def select_record(data):
    """chooses random record from data"""
    index = random.randint(0,len(data))
    name = data[index]['name']
    description = data[index]['description']
    country = data[index]['country']
    followers = data[index]['follower_count']
    return name,description,country,followers

# a = select_record(data)
# print(a[0],a[1],a[2])

choice_A = select_record(data)
choice_B = select_record(data)

# present_choices and collect answer
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
    higher = max(choice_A[3],choice_B[3])
    print(higher)
    print(f"and the user's answer was: {answer}")
    return answer 

# present_choices()
judge_answer(present_choices(),choice_A,choice_B)
