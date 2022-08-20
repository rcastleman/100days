from re import U
from socketserver import UnixStreamServer
import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_state = screen.textinput(title = "Guess the State",
prompt = "What's another state's name?")

user_input = answer_state.title()

states = pd.read_csv("50_states.csv")

def check_input(user_input):
    for state in states["state"]:
        if input == state:
            print("Y")
        else:
            print("N")

print(check_input(user_input))

# print(states["state"])

# if user_input in states["state"]:
#     print("You got one!")
# else:
#     print("Wrong")

#TODO check if answer_state.Title() is in list of states
#IF YES
    #TODO write Guess to screen at x,y value
#IF NO
    #ask user to make another guess
#TODO record correct guesses in a list
#TODO keep track of score