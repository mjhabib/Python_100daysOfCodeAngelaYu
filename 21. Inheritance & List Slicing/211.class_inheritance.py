class Animal:  # our super-class
    def __init__(self):
        self.num_eyes = 2

    def breathing(self):
        print("The animal is breathing ...")


class Fish(Animal):  # calling our super-class (Animal) for inheritance
    def __init__(self):
        super().__init__()  # initializer of our super-class
        
    def breathing(self):  # this is how we can twist an inherited method
        super().breathing()
        print("in this case underwater!")

    def swimming(self):
        print("The fish is swimming ...")


nemo = Fish()
nemo.swimming()
nemo.breathing()
print(f"Fish has {nemo.num_eyes} eyes.\n")

simba = Animal()
simba.breathing()
print(f"Simba has {simba.num_eyes} eyes.\n")
