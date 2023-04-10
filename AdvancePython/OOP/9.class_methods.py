class MyClass:
    class_variable = "I am a class variable"  # Class variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # Instance variable

    def print_instance_variable(self):
        print("Instance variable:", self.instance_variable)

    @classmethod
    def print_class_variable(cls):
        print("Class variable:", cls.class_variable)

    @classmethod
    def modify_class_variable(cls, new_value):
        cls.class_variable = new_value


# Access class variable
print(MyClass.class_variable)  # Output: I am a class variable

# Create objects of the class
obj1 = MyClass("Instance variable 1")
obj2 = MyClass("Instance variable 2")

# Access and modify instance variables
obj1.print_instance_variable()  # Output: Instance variable: Instance variable 1
obj2.print_instance_variable()  # Output: Instance variable: Instance variable 2

# Access and modify class variable through class and objects
MyClass.print_class_variable()  # Output: Class variable: I am a class variable
obj1.print_class_variable()  # Output: Class variable: I am a class variable

# Modify class variable through class method
MyClass.modify_class_variable("Updated class variable")
MyClass.print_class_variable()  # Output: Class variable: Updated class variable
obj1.print_class_variable()  # Output: Class variable: Updated class variable
obj2.print_class_variable()  # Output: Class variable: Updated class variable
