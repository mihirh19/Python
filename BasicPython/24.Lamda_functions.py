# Example code for lambda functions in Python

# Define a lambda function
square = lambda x: x * x

# Use the lambda function
result = square(5)
print("Result of square(5):", result)

# Use the lambda function in a list comprehension
numbers = [1, 2, 3, 4, 5]
squares = [(lambda x: x * x)(num) for num in numbers]
print("Squares of numbers using lambda in list comprehension:", squares)

# Use the lambda function as a key function in sorting
words = ["apple", "banana", "cherry", "date", "fig", "grape"]
words.sort(key=lambda x: len(x))
print("Words sorted by length using lambda as key function:", words)

# Use multiple arguments in a lambda function
addition = lambda x, y: x + y
result = addition(10, 20)
print("Result of addition(10, 20):", result)
