from turtle import Turtle, Screen

tim = Turtle()
tim.color("purple")
jim = Turtle()  # this is one way to create more than one turtle
jim.left(180)
jim.color("green")  # the attributes assigned to an object like color or movement are called 'state'
screen = Screen()


def move_forward():
    tim.forward(10)
    jim.forward(12)


screen.listen()  # our event listener
screen.onkey(move_forward, "space")  # 'onkey()' acts as a "Higher Order Function" here.
# Note: since we used our function as an input here, we don't need to add '()' of our function inside another function/method, i.e. 'onkey()'
screen.exitonclick()
