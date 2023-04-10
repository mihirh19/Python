class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"

    def __eq__(self, other):
        if isinstance(other, MyClass):
            return self.name == other.name and self.age == other.age
        return False

    def __add__(self, other):
        if isinstance(other, MyClass):
            return MyClass(f"{self.name} & {other.name}", self.age + other.age)
        return NotImplemented

    def __len__(self):
        return len(self.name)


# Create objects of MyClass
obj1 = MyClass("John", 25)
obj2 = MyClass("Jane", 30)

# Test __str__ method
print(obj1)  # Output: John, 25 years old

# Test __eq__ method
print(obj1 == obj2)  # Output: False

# Test __add__ method
obj3 = obj1 + obj2
print(obj3.name)  # Output: John & Jane
print(obj3.age)  # Output: 55

# Test __len__ method
print(len(obj1))  # Output: 4
