import turtle
import pandas as pd 

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

#create dataframe from CSV file
data = pd.read_csv("50_states.csv")
#create list so can find membership (??)
all_states = data["state"].to_list()
        
#Get user input
answer_state = screen.textinput(title = "Guess the State",prompt = "What's another state's name?").title()

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    t.write(answer_state,font=40)
    t.goto(int(state_data.x),int(state_data.y))
    # print(f"the xcor for {answer_state} is {go_to_x}")
    # print(f"the ycor for {answer_state} is {go_to_y}")
else:
    print(f"Sorry, {answer_state} is not a US state")


#TODO record correct guesses in a list
#TODO keep track of score

screen.exitonclick()
