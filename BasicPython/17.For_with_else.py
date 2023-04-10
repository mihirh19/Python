# Example list of numbers
numbers = [1, 2, 3, 4, 5]

# Looping through the list of numbers
for num in numbers:
    print(num)
    if num == 3:
        print("Found 3!")
        break  # Exiting the loop when 3 is found
else:
    print("Loop completed.")  # Executed when the loop completes without encountering a break statement

# Example list of strings
fruits = ["apple", "banana", "cherry"]

# Looping through the list of fruits
for fruit in fruits:
    if "a" in fruit:
        print(fruit, "contains the letter 'a'.")
        break  # Exiting the loop when a fruit with 'a' is found
else:
    print("No fruit with 'a' found.")  # Executed when the loop completes without encountering a break statement
