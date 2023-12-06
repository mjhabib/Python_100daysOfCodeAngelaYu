import test_module
print(test_module.test_variable)

# import turtle
# timmy = turtle.Turtle()

# simpler version:
from turtle import Turtle, Screen  # from module import Class, Class
timmy = Turtle()  # object = Class()
print(timmy)  # this is where our class is stored in memory
timmy.shape("turtle")
timmy.color("green")
timmy.forward(100)  # or timmy.fd(100)

my_screen = Screen()  # object = Class()
print(my_screen.canvheight)  # object.attribute
my_screen.exitonclick()  # object.method()


