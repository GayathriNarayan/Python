from shape import *

class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

# Overwrite method calculate_area from shape
    def calculate_area(self):
        return self.height*self.width

# Overwrite method calculate_perimeter from shape     
    def calculate_perimeter(self):
        return 2*(self.height + self.width)

NewRectangle = Rectangle(10, 20)
print("Area of rectangle is " + str(NewRectangle.calculate_area()))
print("Perimeter of rectangle is " + str(NewRectangle.calculate_perimeter()))