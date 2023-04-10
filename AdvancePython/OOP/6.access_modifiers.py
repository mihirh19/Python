# Class with access modifiers
class MyClass:
    def __init__(self):
        self.public_var = "I am a public variable"  # Public variable
        self._protected_var = "I am a protected variable"  # Protected variable
        self.__private_var = "I am a private variable"  # Private variable

    def public_method(self):
        print("I am a public method")  # Public method

    def _protected_method(self):
        print("I am a protected method")  # Protected method

    def __private_method(self):
        print("I am a private method")  # Private method

    def access_members(self):
        print(self.public_var)  # Access public variable
        print(self._protected_var)  # Access protected variable
        print(self.__private_var)  # Access private variable

        self.public_method()  # Access public method
        self._protected_method()  # Access protected method
        self.__private_method()  # Access private method


# Create object of the class
obj = MyClass()

# Access public variable and method
print(obj.public_var)  # Output: I am a public variable
obj.public_method()  # Output: I am a public method

# Access protected variable and method (conventionally considered as internal use only)
print(obj._protected_var)  # Output: I am a protected variable
obj._protected_method()  # Output: I am a protected method

# Access private variable and method (not recommended)
# Note: Name mangling is applied to private variables and methods
print(obj._MyClass__private_var)  # Output: I am a private variable
obj._MyClass__private_method()  # Output: I am a private method
