def factorial(n):
    """
    Recursive function to calculate the factorial of a number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


# Test the factorial function
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}.")
# Output: The factorial of 5 is 120.
