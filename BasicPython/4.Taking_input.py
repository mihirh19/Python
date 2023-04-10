"""
This Python code demonstrates how to take input from the user using the input() function, and how to perform typecasting to convert the input from string to other data types such as integer, float, list, and dictionary.
"""

# Input for integer value
my_int = int(input("Enter an integer: "))
print("You entered:", my_int)

# Input for float value
my_float = float(input("Enter a float: "))
print("You entered:", my_float)

# Input for string value
my_string = input("Enter a string: ")
print("You entered:", my_string)

# Input for list of integers
my_list = input("Enter a list of integers separated by spaces: ")
# Converting input string to list of integers
my_list = list(map(int, my_list.split()))
print("You entered:", my_list)

# Input for dictionary with integer keys and values
my_dict = {}
n = int(input("Enter the number of key-value pairs for the dictionary: "))
for i in range(n):
    key = int(input("Enter key #" + str(i+1) + ": "))
    value = int(input("Enter value #" + str(i+1) + ": "))
    my_dict[key] = value
print("You entered:", my_dict)
