from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.randint(1, 6) == 1:  # to prevent creating too many cars
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            new_y = random.randint(-240, 240)
            new_car.goto(310, new_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
        #     new_x = car.xcor() - STARTING_MOVE_DISTANCE
        #     car.goto(new_x, car.ycor())

    def level_up_speed(self):
        self.car_speed += MOVE_INCREMENT

