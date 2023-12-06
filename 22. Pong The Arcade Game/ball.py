from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1  # default speed of ball

    def move(self):  # loop endlessly
        self.goto(self.xcor() + self.x_move, self.ycor() + self.y_move)

    def y_bounce(self):  # collide with the wall (up & down)
        self.y_move *= -1

    def x_bounce(self):  # collide with paddles
        self.x_move *= -1  # reverse the direction of ball
        self.move_speed *= 0.9  # speed up ball

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_bounce()
