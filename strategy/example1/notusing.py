""" Not using """

class Animal:
    def __init__(self, name):
        self.name = name
    
    def fly(): 
        print("I can fly")

class Bird(Animal):
    def __init__(self, name):
        super().__init__(name)

    # It is OK to use superclass fly method

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    # Now fly() must be overridden
    
    def fly():
        print("I cannot fly!!!")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    # Do the same thing as Dog

