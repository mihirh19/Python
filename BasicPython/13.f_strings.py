# Variables to be used in the f-string
name = "John"
age = 30
city = "New York"

# Creating an f-string
greeting = f"My name is {name}, I am {age} years old, and I live in {city}."
print(greeting)
# Output: My name is John, I am 30 years old, and I live in New York.

# Using expressions in f-strings
a = 5
b = 10
result = f"The sum of {a} and {b} is {a + b}."
print(result)
# Output: The sum of 5 and 10 is 15.

# Formatting numbers in f-strings
pi = 3.14159
formatted_pi = f"Pi is approximately equal to {pi:.3f}."
print(formatted_pi)
# Output: Pi is approximately equal to 3.142.

# Using f-strings with dictionary
person = {"name": "Alice", "age": 25, "city": "London"}
info = f"My name is {person['name']}, I am {person['age']} years old, and I live in {person['city']}."
print(info)
# Output: My name is Alice, I am 25 years old, and I live in London.
