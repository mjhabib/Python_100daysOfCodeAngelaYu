from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# game setup
screen = Screen()
screen.listen()
screen.setup(600, 600)
screen.title("My Snake Game")
screen.bgcolor("black")
screen.tracer(0)  # Turn turtle animation off until we call the update method.

snake = Snake()
food = Food()
score = Scoreboard()

# game control
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# initial the game
game_is_on = True
while game_is_on:
    screen.update()  # turn back the animation on after all snakes move
    time.sleep(0.13)  # this delay will allow us to see the changes in real-time
    snake.move()

    # detecting collision with food
    if snake.head.distance(food) < 15:  # our snake is 20px wide and food 10px, so 15px is because to consider a buffer amount too
        food.refresh()  # print another random dot
        score.increase_score()
        snake.extent()

    # detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    # detecting collision with tail
    for segment in snake.segments[1:]:  # loop through every item except the head
        # if snake.head == segment:  # don't count the distance of the head with itself
        #     pass
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

screen.exitonclick()
