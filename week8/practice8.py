# Another class with init method
class Person:

    # init method or constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Method
    def say_hi(self):
        print('Hello, my name is', self.name)

# Creating different objects

p1 = Person('Enobasi', 17)
p2 = Person('Leela', 19)
p3 = Person('Divine', 18)

p1.say_hi()
p2.say_hi()
p3.say_hi()
