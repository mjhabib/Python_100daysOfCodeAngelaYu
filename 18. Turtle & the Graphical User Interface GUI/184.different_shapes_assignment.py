import random
from turtle import Turtle, Screen

shapes = Turtle()
shapes.penup()
shapes.goto(0, 100)
shapes.pendown()

counter = 8  # triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon
angels = 3
while counter > 0:
    counter -= 1

    ran_color = random.choice(range(100000, 999999))
    shapes.color(f"#{ran_color}")

    degrees = 360 / angels

    for _ in range(angels):
        shapes.right(degrees)
        shapes.forward(100)
    angels += 1


screen = Screen()
screen.exitonclick()
