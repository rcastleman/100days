from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

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

#user label (0,2)
user_label = Label(text="Email/Username: ")
user_label.grid(column=0,row=2)

#user entry (col = 1,row = 2,columnspan = 2)
user_entry = Entry(width=35)
user_entry.grid(column=1,row=2,columnspan=2)

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
add_button = Button(text = "Add to Clipboard",width = 36)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()