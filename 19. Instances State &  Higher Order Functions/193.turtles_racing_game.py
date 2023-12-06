import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.listen()
screen.setup(width=500, height=400)  # positional arguments
user_bet = screen.textinput(title="Choose a color", prompt="red/green/blue/orange/purple/brown? ")

colors = ["red", "green", "blue", "orange", "purple", "brown"]
y_coordinate = -125
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle("turtle")
    # turtle class can get a shape attribute as initializer
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_coordinate)
    y_coordinate += 50
    all_turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                screen.textinput("You won :)", f"The '{winning_color}' turtle was your bet.")
            else:
                screen.textinput("You lost :(", f"The '{winning_color}' turtle was faster!.")
        else:
            rand_distance = random.randint(0, 10)
            turtle.forward(rand_distance)

# screen.exitonclick()
