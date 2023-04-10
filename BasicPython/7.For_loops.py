# For loops in Python

# Example 1: Looping through a sequence of numbers
for i in range(1, 6):  # Range of numbers from 1 to 5 (exclusive)
    print(i)

# Example 2: Looping through a list
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
for fruit in fruits:
    print(fruit)

# Example 3: Looping through a string
name = "John"
for char in name:
    print(char)

# Example 4: Looping through a dictionary
person = {"name": "John", "age": 30, "gender": "male"}
for key, value in person.items():
    print(key, ":", value)

# Example 5: Looping with break and continue statements
for i in range(1, 11):
    if i == 5:
        print("Skipping 5")
        continue
    elif i == 8:
        print("Breaking at 8")
        break
    print(i)
