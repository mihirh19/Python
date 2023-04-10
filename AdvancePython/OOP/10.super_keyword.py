class Parent:
    def __init__(self):
        self.parent_variable = "I am a variable in Parent class"

    def display(self):
        print("Display method in Parent class")


class Child(Parent):
    def __init__(self):
        super().__init__()  # Call the constructor of the parent class
        self.child_variable = "I am a variable in Child class"

    def display(self):
        print("Display method in Child class")

    def display_parent_variable(self):
        print("Parent variable in Child class:", self.parent_variable)


# Create object of Child class
child_obj = Child()

# Access and print Child class variable
print(child_obj.child_variable)  # Output: I am a variable in Child class

# Access and print Parent class variable using super()
print(super(Child, child_obj).parent_variable)  # Output: I am a variable in Parent class

# Call Child class display() method
child_obj.display()  # Output: Display method in Child class

# Call Parent class display() method using super()
super(Child, child_obj).display()  # Output: Display method in Parent class

# Call Child class method to display Parent class variable
child_obj.display_parent_variable()  # Output: Parent variable in Child class: I am a variable in Parent class
