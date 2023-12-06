from turtle import Turtle, Screen
import random

ran_walk = Turtle()
ran_walk.pensize(10)
ran_walk.speed(7)  # 0-10 which 10 is the fastest

color_list = ["blue", "green yellow", "green", "chocolate", "orange", "dark violet", "hot pink", "orange", "gold", "khaki", "aquamarine", "turquoise", "azure", "black"]
direction = [0, 90, 180, 270]

for _ in range(100):
    ran_walk.setheading(random.choice(direction))
    # left_right = random.randint(0, 1)
    # if left_right == 0:
    #     ran_walk.right(random.choice(direction))
    # elif left_right == 1:
    #     ran_walk.left(random.choice(direction))

    ran_walk.color(random.choice(color_list))
    ran_walk.forward(30)

screen = Screen()
screen.exitonclick()
