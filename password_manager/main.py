from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Separator
from turtle import clear
from random import choice,randint,shuffle
import pyperclip 
import json 

#DONE add a search button
#DONE create find_password()
#DONE link find_password to search button
#DONE search data.json
#DONE YES -> messagebox with [website] and [password]
#TODO Catch exception if data.json does exist
#TODO NO -> messagebox "Site not found"

# ---------------------------- FIND PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try: 
        with open("data.json") as data_file:
                data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"website: {website} \nemail: {email} \npassword: {password}")
        else:
            messagebox.showinfo(title = "Error", message = f"No record for '{website}' was found.")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
  
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8, 10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = pass_letters + pass_symbols + pass_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def clear_fields():
    website_entry.delete(0,END)
    user_entry.delete(0,END)
    password_entry.delete(0,END)

def save():
    
        website = website_entry.get()
        email = user_entry.get()
        password = password_entry.get()

        new_data = {
        website: {
            "email": email,
            "password": password
        }
    }
        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showinfo(message="Don't leave any fields empty")
        else:
            try:
                with open("data.json", "r") as data_file:
                    #Reading old data
                    data = json.load(data_file)
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file, indent=4)
            else:
                #Updating old data with new data
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    #Saving updated data
                    json.dump(data, data_file, indent=4)
            finally:
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
website_label = Label(text="Website: ",width=21)
website_label.grid(column=0,row=1)

#website entry (col = 1,row = 1,columnspan = 2,width = 35 )
website_entry = Entry(width=21)
website_entry.grid(column=1,row=1,columnspan=1)
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
generate_button = Button(text = "Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)

#search button 
search_button = Button(text = "Search",width=12,command=find_password)
search_button.grid(column=2,row=1)

#add button (1,4,colspan = 2,width = 36)
add_button = Button(text = "Add to Clipboard",width = 36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()