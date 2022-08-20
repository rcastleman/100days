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
        self.penup()


#create dataframe from CSV file
data = pd.read_csv("50_states.csv")
all_states = data["state"].to_list()
# print(all_states)
        
#Get user input
answer_state = screen.textinput(title = "Guess the State",prompt = "What's another state's name?").title()

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.write(answer_state,font=30)
    state_data = data[data.state == answer_state]
    go_to_x = int(state_data.x)
    go_to_y = int(state_data.y)
    print(f"the xcor for {answer_state} is {go_to_x}")
    print(f"the ycor for {answer_state} is {go_to_y}")
    t.goto(go_to_x,go_to_y)
else:
    print(f"I'm sorry, {answer_state} is not a US state")

#TODO check if answer_state.Title() is in list of states
# IF YES
    #TODO write Guess to screen at x,y value
#IF NO
    #ask user to make another guess


# print(check_input(user_input))

# print(states["state"])

# if user_input in states["state"]:
#     print("You got one!")
# else:
#     print("Wrong")

#TODO record correct guesses in a list
#TODO keep track of score

screen.exitonclick()
