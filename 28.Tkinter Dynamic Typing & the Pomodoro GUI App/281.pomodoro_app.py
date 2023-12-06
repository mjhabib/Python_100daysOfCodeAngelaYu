from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_SEC = 20 * 60   # min to sec
SHORT_BREAK_SEC = 5 * 60
LONG_BREAK_SEC = 20 * 60
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)  # this is how we can stop the timer
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    check_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1

    if reps % 8 == 0:  # only 8 % 8 = 0
        count_down(LONG_BREAK_SEC)
        timer_label.config(text="Break", fg=RED)
    elif reps % 2 == 0:  # 2, 4, 6
        count_down(SHORT_BREAK_SEC)
        timer_label.config(text="Break", fg=PINK)
    else:  # 1, 3, 5, 7
        count_down(WORK_SEC)
        timer_label.config(text="Work", fg=GREEN)

    # another way to do this:
    # if reps == 1 or reps == 3 or reps == 5 or reps == 7:
    #     reps += 1
    #     count_down(WORK_SEC)
    # elif reps == 2 or reps == 4 or reps == 6:
    #     reps += 1
    #     count_down(SHORT_BREAK_SEC)
    # elif reps == 8:
    #     reps = 0
    #     count_down(LONG_BREAK_SEC)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    minutes = math.floor(count / 60)  # Ex: 4.8 = 4
    seconds = count % 60
    if seconds < 10:  # this is how we can show two digits of a number instead of one
        seconds = f"0{seconds}"
    if minutes < 10:
        minutes = f"0{minutes}"
    # note: we don't get a 'TypeError' message here because of "dynamic typing" which is going to convert integer to string and vice-versa
    # dynamic typing = a = 5 --- a = "5" ==> it's going to replace 5 as a string into our variable instead of 5 as an integer

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    elif count == 0:
        start_timer()
        if reps == 2:
            check_label.config(text="✔️", fg=GREEN)
        elif reps == 4:
            check_label.config(text="✔️✔️", fg=GREEN)
        elif reps == 6:
            check_label.config(text="✔️✔️✔️", fg=GREEN)
        elif reps == 8:
            check_label.config(text="✔️✔️✔️✔️", fg=GREEN)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(pady=50, padx=50, bg=YELLOW)

canvas = Canvas(width=210, height=230, bg=YELLOW, highlightthickness=0)
TOMATO_IMG = PhotoImage(file="tomato.png")  # how to read an image file
canvas.create_image(105, 115, image=TOMATO_IMG)  # center, half of the canvas' position
timer_text = canvas.create_text(105, 130, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="TIMER", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, "bold"))
timer_label.grid(column=1, row=0)

check_label = Label(bg=YELLOW, fg=GREEN, font=(FONT_NAME, 15, "bold"))
check_label.grid(column=1, row=3)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
