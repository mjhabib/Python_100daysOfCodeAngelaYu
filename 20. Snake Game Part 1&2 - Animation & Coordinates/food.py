from turtle import Turtle
import random


class Food(Turtle):  # calling Turtle() as a super-class for inheritance
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("purple")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)  # 10*10 px
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        ran_x = random.randint(-280, 280)
        ran_y = random.randint(-280, 280)
        self.goto(ran_x, ran_y)


