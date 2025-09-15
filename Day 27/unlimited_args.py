# How to pass unlimited number of arguments

def add(*args):
    # type of args is tuple
    total = 0
    for n in args:
        total += n
    return total

print(add(1,2,3,4,5))

def calculate(n, **kwargs):
    # type of kwargs is dictionary
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.model)
         