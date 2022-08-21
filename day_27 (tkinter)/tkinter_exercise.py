from tkinter import *

# conversion function
def conversion():
    #string -> float for calculation
    miles = float(miles_input.get())
    #calculation
    km = miles * 1.609
    #float -> string for ouput
    output_label.config(text=f"{km}")

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20,pady=20)

# entry: miles (c=1,r=0)
miles_input = Entry(width=7)
miles_input.grid(column=1,row=0)

# label:miles (c=2,r=0)
miles_label = Label(text="Miles")
miles_label.grid(column=2,row=0)

# label: equals (c=0,r=1)
equals_label = Label(text="is equal to")
equals_label.grid(column=0,row=1)

# label: output (c=1,r=1)
output_label = Label(text="0")
output_label.grid(column=1,row=1)

# label: Km (c=2,r=1)
km_label = Label(text="Km")
km_label.grid(column=2,row=1)

# button: Calculate (c=1,r=3)
button = Button(text="Calculate",command = conversion)
button.grid(column=1,row=2)

window.mainloop()