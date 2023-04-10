class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            raise TypeError("Unsupported operand type for -")

    def __mul__(self, other):
        if isinstance(other, int):
            return Point(self.x * other, self.y * other)
        else:
            raise TypeError("Unsupported operand type for *")


# Create Point objects
p1 = Point(1, 2)
p2 = Point(3, 4)

# Test operator overloading
print(p1)  # Output: (1, 2)
print(p2)  # Output: (3, 4)
print(p1 + p2)  # Output: (4, 6)
print(p1 - p2)  # Output: (-2, -2)
print(p1 * 2)  # Output: (2, 4)
