# simple function
def greet():
    print("Hello")
    print("Hi")
    print("Howdy")


greet()


# function with input
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"Hi {name}")
    print(f"Howdy {name}")


greet_with_name('MJ')


# function with more than one input
def greet_with_name(name, location):  # positional argument
    print(f"Hello {name} from {location}")
    print(f"Hi {name} from {location}")
    print(f"Howdy {name} from {location}")


identity = input("Type your name: ")
place = input("Type your location: ")
greet_with_name(identity, place)


def greet_with_name(stranger, world, job):  # keyword argument
    print(f"Hello {stranger} from {world} busy with {job}.")
    print(f"Hi {stranger} from {world} busy with {job}.")
    print(f"Howdy {stranger} from {world} busy with {job}.")


greet_with_name(job="programmer", world="universe", stranger="Habib")  # in case we mixed things up!
