# anything I gave a name to, has a 'name-space' which is valid in certain scopes
test = 'global'


def test_function():
    test = 'local'
    print(f"test inside function: {test}")


test_function()  # local
print(f"test outside function: {test}")  # global


# Local Scope:
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()  # 2
# print(potion_strength)  # NameError, name is not defined


# Global Scope
player_health = 10


def game():
    def player():
        print(player_health)  # 10


print(player_health)  # 10


# there is no 'block scope' in python:
game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
# since 'if statement' is a block, we can access its variables
# but 'if statement' inside a function, would return an error
# 'while loops' or 'for statements' are also follow this rule


# how to access a global variable inside a local scope:
counter = 2


def increase_counter():
    # global counter  # it's not recommended to write codes like this
    # counter += 1
    # print(f"access global variable: {counter}")

    return counter + 1


counter = increase_counter()
print(counter)  # but this is recommended instead


# global constants = variables that we don't plan to change
PI = 3.14159
URL = "www.google.com"
TWITTER_HANDLE = "@mjhabib4"  # name-spaces are uppercase


def constant_example():
    print(f"constant address: {URL}")


constant_example()
