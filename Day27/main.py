from tkinter import *

window = Tk()

window.title("My GUI Program")
window.config(padx=20, pady=20)


def button_clicked():
    new_text = float(input.get())
    new_value = round(new_text * 1.609)
    miles_to_km_label.config(text=f"{new_value}")


# Label
miles_label = Label(text="Miles")
# miles_label.config(text="New text")
miles_label.grid(column=2, row=0)

text_label = Label(text="is equal to")
text_label.grid(column=0, row=1)

miles_to_km_label = Label()
miles_to_km_label.config(text="0")
miles_to_km_label.grid(column=1, row=1)

km_label = Label(text="km")
km_label.grid(column=2, row=1)


# Button
button = Button(text="Calculate!", command=button_clicked)
button.grid(column=1, row=2)


# Input
input = Entry(width=10)
input.grid(column=1, row=0)


window.mainloop()
