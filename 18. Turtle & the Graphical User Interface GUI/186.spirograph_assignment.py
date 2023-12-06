from turtle import Turtle, Screen
import random

spirograph = Turtle()
spirograph.speed("fastest")


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        ran_color = random.randint(111111, 999999)
        spirograph.color(f"#{ran_color}")
        spirograph.circle(100)
        spirograph.setheading(spirograph.heading() + size_of_gap)


draw_spirograph(10)

# for _ in range(36):
#     ran_color = random.randint(100000, 999999)
#     spirograph.color(f"#{ran_color}")
#     spirograph.circle(100)
#     spirograph.setheading(spirograph.heading() + 10)

screen = Screen()
screen.exitonclick()
