from curses import flash
from tkinter import *
from turtle import clear
from random import choice,randint,shuffle


#constants
BACKGROUND_COLOR = "#B1DDC6"




#------------------ UI -----------------------#

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")

window = Tk()
window.title("Flashcards")
window.config(padx = 50,pady = 50)

flash_front = Canvas(height=526,width=800)
logo_img = PhotoImage(file="logo.png")
flash_front.create_image(300,400, image=card_front)
flash_front.grid(column=1,row=0)

flash_back = Canvas(height=526,width=800)
logo_img = PhotoImage(file="logo.png")
flash_back.create_image(300,400, image=card_front)
flash_back.grid(column=1,row=0)

# button = Button(image=my_image, highlightthickness=0)
