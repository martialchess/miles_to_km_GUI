from tkinter import *

def calculate():
    new_text = float(mile_input.get())
    result = round(new_text * 1.60934)
    default.config(text=result)

window = Tk()
window.title("Mile to KM Converter")
window.minsize(width=300, height=100)
window.config(padx=20, pady=20, bg="white")

#Label
miles = Label(text="Miles", font=("Arial", 10, "normal"), bg="white")
# miles.config(text="New Text")
miles.grid(column=3, row=0)
miles.config(padx=10, pady=10)

is_equal_to = Label(text="is equal to", font=("Arial", 10, "normal"), bg="white")
is_equal_to.grid(column=1, row=2)
is_equal_to.config(padx=10, pady=10)

default = Label(text="0", font=("Arial", 10, "normal"), bg="white")
default.grid(column=2, row=2)
default.config(padx=10, pady=10)

KM = Label(text="KM", font=("Arial", 10, "normal"), bg="white")
KM.grid(column=3, row=2)
KM.config(padx=10, pady=10)

#Button
button = Button(text="Calculate", command=calculate, bg="white", fg="black")
button.grid(column=2, row=3)

#Entry
mile_input = Entry(width=10, bg="white")
# print(mile_input.get())
mile_input.grid(column=2, row=0)


window.mainloop()