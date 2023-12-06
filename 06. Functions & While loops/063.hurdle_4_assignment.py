# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json

# refer to the link above to solve the puzzle with codes below
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    if wall_in_front():
        turn_left()
        move()
        turn_right()
    if wall_in_front():
        turn_left()
        move()
        turn_right()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
        turn_right()
        while not wall_in_front():
            move()
        turn_left()
