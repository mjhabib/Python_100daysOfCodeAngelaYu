import tkinter

my_window = tkinter.Tk()

my_window.title("The window title :)")
my_window.minsize(width=600, height=300)

my_label = tkinter.Label(text="My name is label!", font=("Tahoma", 26, "italic"))
my_label.pack()  # this is how we place our label in the top-center (as default) of screen
# if we don't provide any args here, the program will consider the default args for us which is called 'Optional Arguments' and '...' in documentations mean that arg is optional
# my_label.pack(side="left")  # the way we can change an optional arg

my_window.mainloop()  # this is how we keep screen open
