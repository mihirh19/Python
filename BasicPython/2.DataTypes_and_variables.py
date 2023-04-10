# Example code for variable and data types in Python

# Variables
my_variable = 10                 # An integer variable
my_float_variable = 3.14         # A float variable
my_string_variable = "Hello"     # A string variable

# Lists
my_list = [1, 2, 3, 4, 5, 6]  # A list of integers
my_list.remove(3)                 # Remove an element from the list

# Dictionaries
my_dict = {"name": "John", "age": 25, "city": "New York"}  # A dictionary with key-value pairs
my_dict["gender"] = "Male"        # Add a new key-value pair to the dictionary
my_dict.pop("age")                # Remove a key-value pair from the dictionary

# Tuples
my_tuple = (1, 2, 3, 4, 5)        # A tuple of integers
my_tuple = my_tuple + (6,)        # Concatenate a tuple with another tuple

# String manipulation
my_string = "Hello, World!"
print(my_string.upper())          # Convert the string to uppercase
print(my_string.lower())          # Convert the string to lowercase
print(my_string.split(","))       # Split the string into a list based on a delimiter

# Integer and float operations
a = 10
b = 3
sum = a + b                       # Addition
diff = a - b                      # Subtraction
product = a * b                   # Multiplication
quotient = a / b                 # Division
remainder = a % b                # Modulus
power = a ** b                    # Exponentiation

# Output
print("my_variable:", my_variable)
print("my_float_variable:", my_float_variable)
print("my_string_variable:", my_string_variable)
print("my_list:", my_list)
print("my_dict:", my_dict)
print("my_tuple:", my_tuple)
print("my_string:", my_string)
print("sum:", sum)
print("diff:", diff)
print("product:", product)
print("quotient:", quotient)
print("remainder:", remainder)
print("power:", power)
