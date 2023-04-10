# Creating a tuple
fruits = ('apple', 'banana', 'cherry', 'date')

# Accessing an item in the tuple by index
print(fruits[0])  # Output: 'apple'

# Looping through the tuple and printing each item
for fruit in fruits:
    print(fruit)

# Counting the occurrences of an item in the tuple
print(fruits.count('banana'))  # Output: 1

# Finding the index of an item in the tuple
print(fruits.index('cherry'))  # Output: 2

# Converting a tuple to a list
fruits_list = list(fruits)

# Modifying the list created from the tuple
fruits_list[1] = 'grape'

# Converting the list back to a tuple
fruits = tuple(fruits_list)

# Checking if an item is in the tuple
if 'date' in fruits:
    print('date is in the tuple')

# Finding the length of the tuple
print(len(fruits))  # Output: 4
