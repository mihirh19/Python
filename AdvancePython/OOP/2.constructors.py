# Example code for constructors in Python

# Define a class
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Create objects of the Rectangle class
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

# Access object attributes
print("Rectangle 1 width:", rect1.width)
print("Rectangle 1 height:", rect1.height)
print("Rectangle 2 width:", rect2.width)
print("Rectangle 2 height:", rect2.height)

# Call object methods
print("Rectangle 1 area:", rect1.area())
print("Rectangle 1 perimeter:", rect1.perimeter())
print("Rectangle 2 area:", rect2.area())
print("Rectangle 2 perimeter:", rect2.perimeter())
