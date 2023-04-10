class MyClass:
    # Class-level attribute
    class_variable = "I am a class variable"

    # Class method as constructor
    @classmethod
    def from_string(cls, input_string):
        # Extracting values from input string
        name, age, gender = input_string.split(",")
        # Creating a new instance of MyClass
        return cls(name, int(age), gender)

    # Instance method
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Gender: ", self.gender)


# Create object using class method as constructor
input_string = "John,25,Male"
obj = MyClass.from_string(input_string)

# Call instance method to display object attributes
obj.display()

# Access class-level attribute using class name or object
print("Class variable: ", MyClass.class_variable)
print("Class variable: ", obj.class_variable)
