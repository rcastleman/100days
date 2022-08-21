def add(*args):
    total = 0
    for num in args:
        total += num
    return total

# print(add(1,2,3,4,5,6,7,8,9,10))

def calculate(n,**kwargs):
    n += kwargs['add']
    n *= kwargs['multiply']
    return n

# print(calculate(2,add=3,multiply=5))

class Car:

    def __init__(self,**kw) -> None:
        self.make = kw["make"]
        self.model = kw["model"]
        #get() is better because it returns none instad of erroring
        self.make = kw.get("make")
        self.model = kw.get("model")


my_car = Car(make = "Nissan",model="GTR")

print(f"\nThe model of my car is {my_car.model}\n")

