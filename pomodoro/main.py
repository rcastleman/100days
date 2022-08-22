from itertools import count
from tkinter import *
import time

# CONSTANTS #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# def countdown():
#     t = 25*60
    
#     while t > 0:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         # print(timer, end="\r")
#         # canvas.create_text(textvariable = timer)
#         time.sleep(1)
#         t -= 1

def count_down(count):
    # print(count)
    canvas.itemconfig(timer_text,text=count)
    if count > 0:
        window.after(1000,count_down,count-1)

# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg = YELLOW)

title_label = Label(text = "Timer",fg = GREEN, bg = YELLOW,font = (FONT_NAME,50))
title_label.grid(column=1,row=0)

canvas = Canvas(width=200, height=224,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill = "white",font = (FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

count_down(5)

start_button = Button(text="Start",highlightthickness=0)
start_button.grid(column=0,row=2)

reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(column=2,row=2)

check_marks = Label(text = "✓",fg = GREEN,bg = YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()