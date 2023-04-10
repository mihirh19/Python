class MyClass:
    @staticmethod
    def static_method():
        print("I am a static method")

    def access_static_method(self):
        MyClass.static_method()  # Access static method


# Access static method without creating object of the class
MyClass.static_method()  # Output: I am a static method

# Create object of the class
obj = MyClass()

# Access static method through object
obj.access_static_method()  # Output: I am a static method
