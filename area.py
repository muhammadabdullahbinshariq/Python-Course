import math

class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        x = self.length * self.breadth
        print("The area of your rectangle is", x)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        y = self.radius * self.radius * math.pi
        print("The area of your circle is", y)
    
circle = Circle(float(input("Enter the radius of your circle: ")))
circle.area()

rectangle = Rectangle(float(input("Enter the length of your rectangle: ")), float(input("Enter the breadth of your rectangle: ")))
rectangle.area()