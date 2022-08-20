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
        
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"{len(guessed_states)} /50 States Correct",
    prompt = "What's another state's name?").title()

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state,font=30)

screen.exitonclick()
