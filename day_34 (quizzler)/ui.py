from tkinter import *

THEME_COLOR = "#375362"

def mark_false():
    pass

def mark_true():
    pass

class QuizInterface:

    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")

        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.score_label = Label(text = "Score",fg = "white",bg = THEME_COLOR,font = ("courier",20))
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250)
        self.question_text = self.canvas.create_text(100,130,text="TEST TEXT",fill = "black",font=("courier",20))
        self.canvas.grid(column=0,row=1,columnspan=2)

        self.false_button = Button(text="False",command=mark_false)
        self.false_button.grid(column=1,row=2)
        self.true_button = Button(text="True",command=mark_true)
        self.true_button.grid(column=0,row=2)

        self.window.mainloop()