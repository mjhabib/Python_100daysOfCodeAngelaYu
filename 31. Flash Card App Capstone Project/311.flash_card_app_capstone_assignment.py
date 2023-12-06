from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
WHITE = "#ffffff"
BLACK = "#000000"
ran_word = {}
words_to_learn = {}
data_to_dict = {}


# Create a data-frame
def new_data_frame():
    global data_to_dict
    data = pandas.read_csv("data/german_words.csv")
    data_to_dict = data.to_dict(orient="records")


def right_button_clicked():
    global ran_word, data_to_dict, words_to_learn, flip_timer
    window.after_cancel(flip_timer)  # to fix clicking multiple times on a button to change the word

    if bool(data_to_dict):  # if bool(data_to_dict) == True
        ran_word = random.choice(data_to_dict)
        data_to_dict.remove(ran_word)
        words_to_learn = pandas.DataFrame(data_to_dict)
        words_to_learn.to_csv("data/words_to_learn.csv", index=False)
        canvas.itemconfig(canvas_img, image=card_front_img)
        canvas.itemconfig(card_title, text="German", fill=BLACK)
        canvas.itemconfig(card_word, text=ran_word["German"], fill=BLACK)
        flip_timer = window.after(3000, english_random_word)
    else:
        new_data_frame()
        right_button_clicked()


# pick a random word from the dict and display it into the screen
def german_random_word():
    global words_to_learn, ran_word, flip_timer
    window.after_cancel(flip_timer)

    try:
        ran_word = random.choice(words_to_learn)
        canvas.itemconfig(canvas_img, image=card_front_img)
        canvas.itemconfig(card_title, text="German", fill=BLACK)
        canvas.itemconfig(card_word, text=ran_word["German"], fill=BLACK)
        flip_timer = window.after(3000, english_random_word)
    except:
        right_button_clicked()


def english_random_word():
    global ran_word
    canvas.itemconfig(canvas_img, image=card_back_img)
    canvas.itemconfig(card_title, text="English", fill=WHITE)
    canvas.itemconfig(card_word, text=ran_word["English"], fill=WHITE)


# UI Setup
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, english_random_word)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")
canvas_img = canvas.create_image(400, 263)
card_title = canvas.create_text(400, 100, font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 350, font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Button images
button_right = Button(image=right_img, highlightthickness=0, command=right_button_clicked)
button_right.grid(row=1, column=1)
button_wrong = Button(image=wrong_img, highlightthickness=0, command=german_random_word)
button_wrong.grid(row=1, column=0)

german_random_word()  # to show a random card before we press any button


window.mainloop()
