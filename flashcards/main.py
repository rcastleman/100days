from curses import flash
from tkinter import *
from turtle import clear
from random import choice,randint,shuffle


#constants
BACKGROUND_COLOR = "#B1DDC6"




#------------------ UI -----------------------#

# card_back = PhotoImage(file="/images/card_back.png")

window = Tk()
window.title("Flashcards")
window.config(padx = 50,pady = 50,bg = BACKGROUND_COLOR)

canvas = Canvas(width=800,height=526)
card_front_img = PhotoImage(file="images/card_front.png")
canvas.create_image(400,263,image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
canvas.grid(row=0,column=0)

# flash_back = Canvas(height=526,width=800)
# logo_img = PhotoImage(file="logo.png")
# flash_back.create_image(300,400, image=card_front)
# flash_back.grid(column=1,row=0,columnspan=2)

# button = Button(image=my_image, highlightthickness=0)

window.mainloop()