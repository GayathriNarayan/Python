# Define instance attributes

class Person:

    counter = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.counter += 1

    def greet(self):
        return f"Hi, it's {self.name}"

person1 = Person('John', 25)
person2 = Person('Jane', 22)
print(f"No. of person = {Person.counter}")
print(person1.greet())
print(person2.greet())
