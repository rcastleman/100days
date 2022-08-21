from tkinter import *

def button_clicked():
    new_text = input.get()
    my_label["text"] = new_text

window = Tk()
window.title("My First GUI Window")
window.minsize(width=500,height=300)
window.config(padx=20,pady=20)

#label
my_label = Label(text = "I am a Label",font = ("Arial",24,"bold"))
my_label.config(text = "New Text")
# my_label.pack()
# my_label.place(x=100,y=0)
my_label.grid(column=0,row=0)
my_label.config(padx=25,pady=25)

#button
button = Button(text = "Click Me",font = ("Arial",24,"bold"),command=button_clicked)
# button.pack()
button.grid(column=1,row=1)

#new button
button_2 = Button(text = "New Button",font = ("Arial",24,"bold"))
button_2.grid(column=2,row=0)

#entry
input = Entry(relief="sunken")
print(input.get())
# input.pack()
input.grid(column=3,row=2)

window.mainloop()