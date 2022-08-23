from asyncio.proactor_events import _ProactorBaseWritePipeTransport
from readline import insert_text
from tkinter import *
from tkinter.ttk import Separator
from turtle import clear


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# using ADD button, save entered info (website,email,password) into data.txt
# separator = "|" or whatever

# user tkinter insert() method
# use Write to file method
# use delete() to clear entries after Add button is used

def clear_fields():
    website_entry.delete(0,END)
    user_entry.delete(0,END)
    password_entry.delete(0,END)

def save():
    with open ("data.txt","a") as file:
        site = website_entry.get()
        email = user_entry.get()
        password = password_entry.get()
        file.write(f"{site} | {email} | {password}\n")
        clear_fields()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50,pady = 50)

canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100, image=logo_img)
canvas.grid(column=1,row=0)

#website label (col=0,row=1)
website_label = Label(text="Website: ")
website_label.grid(column=0,row=1)

#website entry (col = 1,row = 1,columnspan = 2,width = 35 )
website_entry = Entry(width=35)
website_entry.grid(column=1,row=1,columnspan=2)
website_entry.focus()

#user label (0,2)
user_label = Label(text="Email/Username: ")
user_label.grid(column=0,row=2)

#user entry (col = 1,row = 2,columnspan = 2)
user_entry = Entry(width=35)
user_entry.grid(column=1,row=2,columnspan=2)
user_entry.insert(0,"rcastleman@gmail.com")

#password label (0,3)
password_label = Label(text="Password: ")
password_label.grid(column=0,row=3)

#password box (1,3,width = 21)
password_entry = Entry(width = 21)
password_entry.grid(column=1,row=3)

#generate button (2,3)
generate_button = Button(text = "Generate Password")
generate_button.grid(column=2,row=3)

#add button (1,4,colspan = 2,width = 36)
add_button = Button(text = "Add to Clipboard",width = 36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()