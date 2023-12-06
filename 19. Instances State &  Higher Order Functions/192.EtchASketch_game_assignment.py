from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.listen()


def move_forward():
    tim.forward(10)


def move_back():
    tim.backward(10)


def move_clock():
    # tim.right(10)
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_counter_clock():
    # tim.left(10)
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear_turtle():
    tim.clear()
    tim.penup()
    tim.goto(0, 0)
    tim.pendown()


screen.onkey(move_forward, "w")
screen.onkey(move_back, "s")
screen.onkey(move_clock, "a")
screen.onkey(move_counter_clock, "d")
screen.onkey(clear_turtle, "c")

screen.exitonclick()
