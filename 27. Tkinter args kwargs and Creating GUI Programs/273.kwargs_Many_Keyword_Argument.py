# this is how we can specify as many 'keyword arguments' as we want
def calculator(n, **kwargs):
    print(kwargs)  # {'add': 3, 'multiply': 5}
    # we can treat our 'kwargs' as a dict
    for key, value in kwargs.items():
        print(value)  # 3, 5

    # or
    n += kwargs["add"]
    print(n)  # 5
    n *= kwargs["multiply"]
    print(n)  # 25


calculator(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        self.color = kw.get("color")  # we can use get() for optional args


my_car = Car(make="Nissan", model="GT-R")  # description = '**kw' because of the 'kwargs' we used to initialize the class
print(my_car.make)  # Nissan
print(my_car.model)  # GT-R
print(my_car.color)  # None
