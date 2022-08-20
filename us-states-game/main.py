import turtle
import pandas as pd 
import csv

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
#create list so can find membership (??)
all_states = data["state"].to_list()
        
guessed_states = []

while len(guessed_states) < 50:

    answer_state = screen.textinput(title = f"{len(guessed_states)} /50 States Correct",
    prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        missed = []
        for state in all_states:
            if state not in guessed_states:
                missed.append(state)
        missed_data = pd.DataFrame(missed)
        missed_data.to_csv("states_to_learn.csv")
        break
    
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(),state_data.y.item())
        t.write(answer_state,font=30)

#generate 


# with open("states_to_learn.csv",mode="w") as file:
#     write = csv.writer(file)
#     write(missed)

# screen.exitonclick()