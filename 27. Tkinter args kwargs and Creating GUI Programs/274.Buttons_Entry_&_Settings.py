from tkinter import Tk, Label, Button, Entry


def button1_clicked():
    label2["text"] = "The button got clicked!"


def button2_clicked():
    label2["text"] = entry1.get()


window = Tk()
window.title("This is what this is!")
window.minsize(600, 300)

label1 = Label(text="Label's text ...", font=("", 16))
label1["text"] = "One way to change a label's text"
label1.config(text="Another way to change a label's text")
label1.pack()

label2 = Label(text="Another label ...", font=("", 18))
label2.pack()

button1 = Button(text="I'm a button", command=button1_clicked)
button1.pack()

button2 = Button(text="I'm another button", command=button2_clicked)
button2.pack(side="bottom")

entry1 = Entry(width=15)
entry1.pack(side="bottom")

label3 = Label(text="Label's layout manager using place()", font=("", 20))
label3.place(x=20, y=150)
# instead of pack() we can use place() for a very precise positioning
# these coordinates are different from how turtle works! - 0, 0 = top-left corner not in the middle

label4 = Label(text="Label's layout manager using grid()", font=("", 20))

# label4.grid(column=0, row=0)
# ***
# the grid() will divide our window any amount of columns and rows chosen by us and place our widget there.
# important note: grid is relative to other widgets
# another note: grid() won't work with pack() layout manager and returns an error

window.mainloop()
