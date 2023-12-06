# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

# refer to the link above to solve the puzzle with codes below

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# this is how we escape an infinite loop described in all problem worlds:
while front_is_clear():
    move()
turn_left


while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

