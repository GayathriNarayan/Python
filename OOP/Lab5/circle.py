# Create classes Circle (receives radius upon initialization) and Rectangle (receives height and width upon initialization) 
# that implement those methods (returning the result)
# And do the same thing as you did with the previous lab (Lab4). Seperate files for different classes.

from shape import *

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius


# Overwrite method calculate_area from shape
    def calculate_area(self):
        return self.radius**2*3.14

# Overwrite method calculate_perimeter from shape   
    def calculate_perimeter(self):
        return 2*self.radius*3.14

NewCircle = Circle(5)
print("Area of a circle is " + str(NewCircle.calculate_area()))
print("Perimeter of a circle is " + str(NewCircle.calculate_perimeter()))
print("\n")