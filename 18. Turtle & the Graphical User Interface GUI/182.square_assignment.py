from turtle import Turtle, Screen

draw_square = Turtle()

for _ in range(4):
    draw_square.forward(100)
    draw_square.right(90)

screen = Screen()
screen.exitonclick()
