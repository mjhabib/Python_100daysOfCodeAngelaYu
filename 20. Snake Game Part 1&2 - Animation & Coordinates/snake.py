from turtle import Turtle

MOVE_DISTANCE = 20
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snakes()
        self.head = self.segments[
            0]  # to make our code more readable - the position of this line is important to be after create_snakes()

    def create_snakes(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, last_pos):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(last_pos)
        self.segments.append(new_segment)

    # add a new segment to the snake
    def extent(self):
        self.add_segment(self.segments[-1].position())  # -1 == last segment
        # last_segment = len(self.segments) - 1
        # last_pos = self.segments[last_segment].position()
        # self.add_segment(last_pos)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):  # """***"""
            # reverse loop 2️⃣ >> 1️⃣ >> 0️⃣ (this is the order of creating the snakes from right (0, 0) to left (-40, 0))
            new_x = self.segments[seg - 1].xcor()  # the x coordinate of our second to last snake 2️⃣ 1️⃣ 0️⃣ == 1️⃣
            new_y = self.segments[seg - 1].ycor()  # the y coordinate of our second to last snake 2️⃣ 1️⃣ 0️⃣ == 1️⃣
            self.segments[seg].goto(new_x, new_y)  # 2️⃣
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # to prevent snake to turn its head towards its tail - it's not allowed in the game
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:  # to prevent snake to turn its head towards its tail - it's not allowed in the game
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:  # to prevent snake to turn its head towards its tail - it's not allowed in the game
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:  # to prevent snake to turn its head towards its tail - it's not allowed in the game
            self.head.setheading(RIGHT)


""" ***
here we want our snake[0] to move to position of snake[1] and snake[1] to position of snake[2], that way by controlling the head (snake[2]) others will adopt themselves with new movement. This is how our range should look like: "range(start=2, stop=0, step=-1)", only we can't use the descriptions for our arguments like other functions (keyword arguments).
"""
