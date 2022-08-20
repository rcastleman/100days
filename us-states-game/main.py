import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

class StateObject(turtle.Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1,2)
        self.write("TEST TEXT", True, align="center")
        self.penup()
        #user_input -> state -> lookup x,y in states dataframe
        state_location = states[states["state"] == user_input]
        go_to_location = state_location[(states["x"],states["y"])]
        self.goto(state_location)


#create dataframe from CSV file
states = pd.read_csv("50_states.csv")
        
#Get user input
answer_state = screen.textinput(title = "Guess the State",prompt = "What's another state's name?")
#convert user input to Title Case
user_input = answer_state.title()
print_object = turtle.Turtle()
print_object.hideturtle()
print_object.write(user_input,font=30)
target_state = states[states.state == user_input]
goto_x = target_state["x"]
goto_y = target_state["y"] 
# print(target_state)
print_object.goto(goto_x,goto_y)

#TODO check if answer_state.Title() is in list of states
#IF YES
    #TODO write Guess to screen at x,y value
#IF NO
    #ask user to make another guess

def check_input(user_input):
    for state in states["state"]:
        if input == state:
            return True
        else:
            return False

# print(check_input(user_input))

# print(states["state"])

# if user_input in states["state"]:
#     print("You got one!")
# else:
#     print("Wrong")

#TODO record correct guesses in a list
#TODO keep track of score

screen.exitonclick()
