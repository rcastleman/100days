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

        self.score_label = Label(text = "Score: 0",fg = "white",bg = THEME_COLOR,font = ("courier",20))
        self.score_label.grid(column=1,row=0)

        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text = self.canvas.create_text(150,125,text="Some Question Text...",fill = THEME_COLOR,font=("arial",20,"italic"))
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)

        false_image = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_image,highlightthickness=0,command=mark_false)
        self.false_button.grid(column=1,row=2)

        true_image = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_image,highlightthickness=0,command=mark_true)
        self.true_button.grid(column=0,row=2)

        self.window.mainloop()
