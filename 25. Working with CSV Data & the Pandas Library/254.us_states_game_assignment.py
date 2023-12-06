from turtle import Turtle, Screen
import pandas

# map setup
screen = Screen()
# screen.setup(800, 600)
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

prim_turtle = Turtle()
prim_turtle.shape(image)
new_turtle = Turtle()
new_turtle.hideturtle()
new_turtle.penup()

data = pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
# list_goes_on = len(data)
# correct_answers = 0
guessed_states = []
while len(guessed_states) < 50:
    state_answer = screen.textinput(f"Guess the state: {len(guessed_states)}/50",
                                    "What is another state's name?").title()
    # list_goes_on -= 1
    # for state in data.state:
    if state_answer in states_list:
        # correct_answers += 1
        guessed_states.append(state_answer)
        state_row = data[data.state == state_answer]
        new_turtle.goto(state_row.x.item(), state_row.y.item())
        new_turtle.write(state_answer, False, "center", ("Ariel", 10, "normal"))

        # item() == Returns the first element of the underlying data as a Python scalar (without all other descriptions in data.series like index)

        # or using the long version below!
        # x_coord = state_row['x'].to_list()
        # y_coord = state_row['y'].to_list()
        # new_turtle.goto(x_coord[0], y_coord[0])

        # the method below doesn't work anymore:
        # new_turtle.goto(int(state_row.x), int(state_row.y))
        # FutureWarning: Calling int on a single element Series is deprecated and will raise a TypeError in the future. Use int(ser.iloc[0]) instead

    elif state_answer == "Exit":
        # missed_states = []
        # if state not in guessed_states:
        #     missed_states.append(state)

        # or

        # for state in guessed_states:  # in states_list
        #     if state in states_list:
        #         states_list.remove(state)

        # re-writing the code above using list comprehension
        missed_states = [state for state in states_list if state not in guessed_states]

        states_to_learn = pandas.DataFrame(missed_states)
        states_to_learn.to_csv("states_to_learn.txt")
        import os
        os.system("start " + "states_to_learn.txt")
        break
        # or
        # import sys
        # sys.exit()
        # or
        # raise SystemExit()
        # or
        # list_goes_on = 0

screen.exitonclick()

# # this is how we can get all the coordinates loaded in 50_states.csv file
# def mouse_click_coordinates(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(mouse_click_coordinates)
# turtle.mainloop()  # alternative to onscreenclick()
# # we can't use onscreenclick() here because we need to click on the map in order to get the coordinates, and we don't want it to close after each click!

# convert python project to exe
# pyinstaller direction/project_name.py --onefile
