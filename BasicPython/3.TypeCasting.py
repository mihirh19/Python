"""
Typecasting, also known as data type conversion, is the process of converting a value from one data type to another. Python provides built-in functions to perform typecasting between different data types.
"""

# Integer to float
my_int = 10
my_float = float(my_int)    # Typecast integer to float
print("Integer to float:", my_float)

# Float to integer
my_float = 3.14
my_int = int(my_float)      # Typecast float to integer
print("Float to integer:", my_int)

# String to integer
my_string = "123"
my_int = int(my_string)     # Typecast string to integer
print("String to integer:", my_int)

# String to float
my_string = "3.14"
my_float = float(my_string) # Typecast string to float
print("String to float:", my_float)

# Integer to string
my_int = 123
my_string = str(my_int)     # Typecast integer to string
print("Integer to string:", my_string)

# Float to string
my_float = 3.14
my_string = str(my_float)   # Typecast float to string
print("Float to string:", my_string)

# List to tuple
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)   # Typecast list to tuple
print("List to tuple:", my_tuple)

# Tuple to list
my_tuple = (1, 2, 3, 4, 5)
my_list = list(my_tuple)    # Typecast tuple to list
print("Tuple to list:", my_list)

# Dictionary to list of keys, values, or items
my_dict = {"name": "John", "age": 25, "city": "New York"}
keys_list = list(my_dict.keys())        # Typecast dictionary keys to list
values_list = list(my_dict.values())    # Typecast dictionary values to list
items_list = list(my_dict.items())      # Typecast dictionary items to list
print("Dictionary to list of keys:", keys_list)
print("Dictionary to list of values:", values_list)
print("Dictionary to list of items:", items_list)
