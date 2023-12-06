from tkinter import *
from tkinter import messagebox  # because messagebox is not a class to import it via * sign
import random
import pandas
import pyperclip  # to copy text into clipboard automatically


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_pass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    new_letter_list = [random.choice(letters) for _ in range(random.randint(8, 10))]
    new_symbol_list = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    new_number_list = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = new_letter_list + new_symbol_list + new_number_list
    random.shuffle(password_list)

    password = "".join(password_list)
    # or
    # password = ""
    # for char in password_list:
    #   password += char

    pass_entry.delete(0, END)
    pass_entry.insert(0, password)
    pyperclip.copy(password)  # copy the password automatically into the clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_pass():
    web_user_pass = [web_entry.get(), user_entry.get(), pass_entry.get()]
    # or
    # web_user_pass.append(web_entry.get())
    # web_user_pass.append(user_entry.get())
    # web_user_pass.append(pass_entry.get())

    if len(web_entry.get()) < 1 or len(user_entry.get()) < 1 or len(pass_entry.get()) < 1:
        messagebox.showwarning("Warning", "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel("Are you happy with your inputs? ", f"{web_user_pass}")
        if is_ok:
            web_entry.delete(0, END)  # remove entries from start to end
            pass_entry.delete(0, END)

            data = pandas.DataFrame(web_user_pass, index=["Website: ", "Username: ", "Password: "])
            data.to_csv("data.txt", mode="a")
            # or
            # with open("data.txt" "a") as data_file:
            #     data_file.write(f"{web} | {user} | {passwd} \n")  # need to create separate variables for each entry


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pass Manager")
window.config(padx=25, pady=25)

canvas = Canvas(width=200, height=200)
LOGO = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=LOGO)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website: ")
website_label.grid(column=0, row=1)
username_label = Label(text="Email/Username: ")
username_label.grid(column=0, row=2)
password_label = Label(text="Password: ")
password_label.grid(column=0, row=3)

# Entries
web_entry = Entry(width=35)
web_entry.focus()  # put the cursor inside the entry
web_entry.grid(column=1, row=1, columnspan=2)
user_entry = Entry(width=35)
user_entry.insert(0, "mj.habib4@hotmail.com")  # pre-enter a password at index 0
user_entry.grid(column=1, row=2, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(column=1, row=3)

# Buttons
gen_button = Button(text="Generate Password", command=gen_pass)
gen_button.grid(column=2, row=3)
add_button = Button(text="Add", width=36, command=save_pass)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
