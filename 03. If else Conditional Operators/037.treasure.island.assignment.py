print("Welcome to the Treasure Island Game :)\n"+"Your mission is to find the treasure.\n")
print("GOOD LUCK AND HAVE FUN ;) \n")
print(r'''
                    ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   \
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\uuu/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              """"-""""""""""""""""""""""""""-""""
''')
print('Type "go" in order to start the game. ')
if input() == 'go':
    print("You are in a middle of a jungle and facing a tiger. Are you going to jump into the river or climb a tree? ")
    print('Type "jump" or "climb". ')
    if input() == 'jump':
        print("Awesome, now, there is a waterfall. Are you gonna dive or hang on to a branch? ")
        print('Type "dive" or "branch". ')
    if input() == 'branch':
        print("Amazing. You're almost there. Now you can see three doors. Which door do you choose? ")
        print('Type "red" or "blue" or "green". ')
    if input() == 'green':
        print("Congratulations. You won the game :) Hooray :)))")
    else:
        print("Sorry, game over!")
else:
    print("You need to start the game in order to play. ")
