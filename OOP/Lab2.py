# LAB 2 - OOP
# Create the following classes: Animal, Horse and Dog.
# The Animal class should have a method eat ( ) and it should return "eating.. nom.. nom.."
# The Horse class should have a method called neigh ( ) and it should return "neigh! "
# The Dog class should have a method called bark ( ) and it should return "voof voof!"
# And remember that the Horse and Dog class should inherit from the Animal class.

class Animal:
    def eat(self):
        print("Eating.. nom.. nom..")

class Horse(Animal):
    def __init__(self):
        print("Horse is created")
    def neigh(self):
        print("Neigh!")

class Dog(Animal):
    def __init__(self):
        print("Dog is created")
    def bark(self):
        print("voof voof!") 

h = Horse()
h.eat()
h.neigh()

d = Dog()
d.eat()
d.bark()


