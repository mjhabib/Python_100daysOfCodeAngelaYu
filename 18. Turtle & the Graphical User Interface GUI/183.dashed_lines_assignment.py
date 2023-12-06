from turtle import Turtle, Screen

dash = Turtle()

dash.penup()
dash.goto(-200, 0)

for _ in range(50):
    dash.pendown()
    dash.pensize(2)
    dash.forward(5)
    dash.penup()
    dash.forward(5)

screen = Screen()
screen.exitonclick()
