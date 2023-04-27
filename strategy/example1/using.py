""" Using """

class Fly:
    def fly(): print("I am an animal")

class Flyable(Fly):
    def fly(self): print("I can fly")

class Unflyable(Fly):
    def fly(self): print("I cannot fly!!!")

# Now set these flyability subclasses as objects of original subclasses

class Animal:
    def __init__(self, name, flyability):
        self.name = name
        self.flyability = flyability

    def fly(self):
        self.flyability.fly()
class Bird(Animal):
    def __init__(self, name):
        super().__init__(name, Flyable())
class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, Unflyable())

Bird("Birdy").fly()
Dog("Snoopy").fly()
