from curses import flash
import fileinput
from tkinter import *
from turtle import clear
import random
import pandas as pd
import os.path


BACKGROUND_COLOR = "#B1DDC6"

#------------------ read data -----------------------#

if os.path.exists("data/words_to_learn.csv"):
    data = pd.read_csv("data/words_to_learn.csv")
else:
    data = pd.read_csv("data/french_words.csv")

learned_words = []

#dataframe -> list
output_list = data.values.tolist()
print(output_list)
# remove learned word from list

def mark_for_removal(word):
    """adds a word to the learned_words list, marking it for removal"""
    learned_words.append(word)

def remove_word():
    """removes word from the output_list"""
    for word in output_list:
        if word in learned_words:
            output_list.remove(word)

to_learn = data.to_dict(orient="records")

current_card = {}

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(list(to_learn))
    canvas.itemconfig(card_title,text="French",fill="black")
    canvas.itemconfig(card_word,text=current_card["French"],fill="black")
    canvas.itemconfig(card_background,image = card_front_img)
    flip_timer = window.after(3000,func=flip_card)

def flip_card():
    canvas.itemconfig(card_title, text="English",fill = "white")
    canvas.itemconfig(card_word,text=current_card["English"],fill="white")
    canvas.itemconfig(card_background,image = card_back_img)

#------------------ UI -----------------------#
window = Tk()
window.title("Flashcards")
window.config(padx = 50,pady = 50,bg = BACKGROUND_COLOR)

flip_timer = window.after(3000,func=flip_card)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file = "images/card_front.png")
card_back_img = PhotoImage(file = "images/card_back.png")
card_background = canvas.create_image(400,263,image=card_front_img)
card_title = canvas.create_text(400,150,text="Title",font=("Arial",40,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0,columnspan=2)

#X Mark
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image,highlightthickness=0,command=next_card)
unknown_button.grid(row=1,column=0)

#check mark
check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image,highlightthickness=0,command=next_card)
known_button.grid(row=1,column=1)

next_card()

window.mainloop()