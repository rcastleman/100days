from tkinter import *

window = Tk()
window.title("My First GUI Window")
window.minsize(width=500,height=300)
#label
my_label = Label(text = "I am a Label",
font = ("Arial",24,"bold"))
my_label.pack()
#update label text
my_label["text"] = "New Text"

def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text

#button
button = Button(text = "Click Me",
font = ("Arial",24,"bold"),
command=button_clicked)
button.pack()

input = Entry(relief="sunken")
input.pack()

window.mainloop()