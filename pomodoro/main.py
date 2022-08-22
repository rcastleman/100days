from sqlite3 import Date
from tkinter import *
import time
import datetime

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    pass

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2,row=2)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def timer():
    total_seconds = 25*60*60
    pomodoro_count = 0

    while total_seconds > 0:
        timer = datetime.timedelta(seconds =  total_seconds)
        canvas.create_text.config(text = timer)
        time.sleep(1)
        total_seconds -= 1

    pomodoro_count += 1
    print("Time's Up!")

start_button = Button(text="Start", command=timer)
start_button.grid(column=0,row=2)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

countdown_label = Label(text = "✓",fg = GREEN)
countdown_label.grid(column=1,row=3)

# ---------------------------- UI SETUP ------------------------------- #

# window
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg = YELLOW)

# timer label
# time_label = Label(text = "Timer",font = (FONT_NAME,40,"bold"))
# countdown_label.grid(column=1,row=0)

#canvas
canvas = Canvas(width=200, height=224,bg = YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
canvas.grid(column=1,row=1)
canvas.create_text(100,130,text=timer,
fill = "white",
font = (FONT_NAME,35,"bold"))

window.mainloop()