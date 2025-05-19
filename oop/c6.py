# Challenge
# Finish implementing the empty methods of the Rectangle and Square classes. 
# All squares are rectangles, but not all rectangles are squares.

class Rectangle:
    def __init__(self, length, width):
        self.length = length 
        self.width = width

    def get_area(self):
        area = self.length * self.width
        return area

    def get_perimeter(self):
        perimeter = (2*self.length) + (2*self.width)
        return perimeter

class Square(Rectangle):
    def __init__(self, length):
        self.length = length

    def get_area(self):
        area = self.length ** 2
        return area

    def get_perimeter(self):
        perimeter = 4 * self.length 
        return perimeter
