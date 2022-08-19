import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# get all the x,y coordinates of the states
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer_state = screen.textinput(title = "Guess the State",prompt = "What's another state's name?")

#TODO check if answer_state.Title() is in list
#IF YES
#TODO write state on to screen at x,y value
#TODO create state counter 