# one time only - to extract colors:
# import colorgram
#
# colors = colorgram.extract('the_hirst_painting.jpg', 26)
#
# rgb_colros = []
#
# for i in colors:
#     # rgb_colros.append(i.rgb)
#     r = i.rgb.r
#     g = i.rgb.g
#     b = i.rgb.b
#     new_color = (r, g, b)
#     rgb_colros.append(new_color)
#
# print(rgb_colros)
import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
# if we want to give our turtle an RGB color, we have to add this line of code

color_list = [(199, 175, 117), (124, 36, 24), (168, 106, 57), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120)]

hirst_painting = Turtle()
hirst_painting.speed(10)
hirst_painting.penup()
hirst_painting.goto(-240, -240)
y_pos = -240

for _ in range(10):
    y_pos += 40
    hirst_painting.goto(-240, y_pos)
    for _ in range(10):
        hirst_painting.pendown()
        hirst_painting.dot(20, random.choice(color_list))
        hirst_painting.penup()
        hirst_painting.forward(50)

hirst_painting.hideturtle()
screen = Screen()
screen.exitonclick()
