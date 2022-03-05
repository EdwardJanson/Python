from tkinter import *


def calculator():
    miles_in_km = round(float(entry.get()) * 1.6, 2)
    km_output.config(text=f"{miles_in_km}")


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=20, pady=20)

entry = Entry(width=10)
entry.insert(END, string="0")
entry.grid(column=1, row=0)

miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

calculate = Button(text="Calculate", command=calculator)
calculate.grid(column=1, row=2)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

window.mainloop()
