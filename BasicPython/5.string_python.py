# String operations in Python

# Declaring a string
my_string = "Hello, world!"

# Printing the string
print("my_string:", my_string)

# Accessing characters in a string using index
print("First character:", my_string[0])
print("Last character:", my_string[-1])

# Slicing a string to extract substrings
print("Substring from index 0 to 4:", my_string[0:5])
print("Substring from index 7 to end:", my_string[7:])
print("Substring from index -6 to -2:", my_string[-6:-1])

# Concatenating strings
str1 = "Hello"

str2 = "world"

str3 = str1 + " " + str2
print("Concatenated string:", str3)

# Finding the length of a string
print("Length of my_string:", len(my_string))

# Converting a string to uppercase and lowercase
print("Uppercase:", my_string.upper())
print("Lowercase:", my_string.lower())

# Replacing characters in a string
new_string = my_string.replace("world", "Python")
print("Replaced string:", new_string)

# Checking if a substring is present in a string
substring = "world"
if substring in my_string:
    print(substring, "is present in my_string.")
else:
    print(substring, "is not present in my_string.")

# Splitting a string into a list of substrings
words = my_string.split(", ")
print("List of words:", words)
