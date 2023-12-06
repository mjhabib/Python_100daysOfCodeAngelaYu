# import turtle  # if we want to use this module only once
# turtle.Turtle()
import random
import turtle

# import turtle as alias_name  # we can give our module an alias name
# alias_name.Turtle()

from turtle import Turtle, Screen  # if we want to use these modules multiple times

# from turtle import *  # another way of importing everything in a module
# forward(100)
"""
that way, we don't even have to call the name of our class, but this is confusing since we might don't know where the forward() method comes from.
"""

timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")
timmy_the_turtle.forward(-100)
timmy_the_turtle.right(90)  # 90 degrees

my_tuple = (5, 2, 7)
# this is a 'tuple' similar to a list which we can't change its values (immutable)
print(my_tuple[1])  # 2


turtle.colormode(255)
# if we want to give our turtle an RGB color, we have to add this line of code


def rand_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


timmy_the_turtle.color(rand_color())
timmy_the_turtle.forward(100)

screen = Screen()
screen.exitonclick()
