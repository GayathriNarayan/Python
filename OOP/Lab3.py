# LAB 3 - OOP
# Create the following classes:
# Person
# Staff
# Busdriver
# Person should have one method named walk( ) that should return "walking"
# Staff should have one method called work( ) that should return "working"
# Busdriver should have one method called driving ( ) that returns "diving the bus"
# The Busdriver class should inherit from both Person and Staff 


class Person():
    def walk(self):
        print("Person is walking")

class Staff(Person):
    def work(self):
        print("Staff is working")

class Busdriver(Staff):
    def drive(self):
        print("Driver is driving the bus")


b = Busdriver()
b.walk()
b.work()
b.drive()
