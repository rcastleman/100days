from curses import flash
from tkinter import *
from turtle import clear
import random
import pandas as pd


#constants
BACKGROUND_COLOR = "#B1DDC6"

#------------------ read data -----------------------#

data = pd.read_csv("data/french_words.csv")
data_dict = data.to_dict(orient="records")

def generate_random_word():
    random_word = random.choice(list(data_dict))
    return random_word['French']

# word = generate_random_word()

#------------------ UI -----------------------#

# card_back = PhotoImage(file="/images/card_back.png")

window = Tk()
window.title("Flashcards")
window.config(padx = 50,pady = 50,bg = BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
canvas.create_text(400,263,text=generate_random_word(),font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

#X Mark
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=generate_random_word)
unknown_button.grid(row=1,column=0)

#check mark
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0,command=generate_random_word)
known_button.grid(row=1,column=1)

# flash_back = Canvas(height=526,width=800)
# logo_img = PhotoImage(file="logo.png")
# flash_back.create_image(300,400, image=card_front)
# flash_back.grid(column=1,row=0,columnspan=2)

# button = Button(image=my_image, highlightthickness=0)

window.mainloop()