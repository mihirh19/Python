# If-Else statements in Python

# Declaring variables
x = 10
y = 5

# Example 1: If-Else
if x > y:
    print("x is greater than y")
else:
    print("x is not greater than y")

# Example 2: If-Elif-Else
if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is not greater than y and not equal to y")

# Example 3: Nested If-Else
if x > 0:
    if x % 2 == 0:
        print("x is positive and even")
    else:
        print("x is positive and odd")
else:
    print("x is not positive")

# Example 4: Ternary Operator
result = "x is greater than y" if x > y else "x is not greater than y"
print(result)
