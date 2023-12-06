from tkinter import *

window = Tk()
window.title("Title for grid assignment")
window.minsize(400, 300)
window.config(padx=30, pady=30)  # define padding

label = Label(text="Label", font=("", 20))
label.grid(column=0, row=0)
label.config(padx=10, pady=10)  # padding specific to a widget

button = Button(text="Button", font=("", 20))
button.grid(column=1, row=1)

new_button = Button(text="New Button", font=("", 20))
new_button.grid(column=2, row=0)

entry = Entry(width=20)
entry.grid(column=3, row=2)

window.mainloop()
