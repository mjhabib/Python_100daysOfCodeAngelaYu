from tkinter import *

window = Tk()
window.title("Miles to Km Converter ...")
window.minsize(150, 150)
window.config(padx=10, pady=10)


def mile_to_km():
    mile = entry.get()
    to_km = float(mile) * 1.609
    label_converter["text"] = round(to_km, 2)


entry = Entry(width=20)
entry.grid(column=1, row=0)

label_miles = Label(text="Miles", font=("", 16))
label_miles.grid(column=2, row=0)

label_equal = Label(text="is equal to ", font=("", 16))
label_equal.grid(column=0, row=1)

label_converter = Label(text="0", font=("", 16))
label_converter.grid(column=1, row=1)

label_km = Label(text="Km", font=("", 16))
label_km.grid(column=2, row=1)

button = Button(text="Convert", font=("", 16), command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()
