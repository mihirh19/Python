"""
What are Generators?
Generators are a type of iterator in Python that allow for the creation of iterable sequences of values on-the-fly, without having to store them all in memory at once. Generators are defined using a special type of function called a generator function, which contains one or more yield statements.

Generator Functions: A generator function is similar to a regular function in Python, but instead of using the return
statement to return a value and terminate the function, it uses the yield statement to produce a value and pause the
function's execution. The generator function can be resumed later from where it left off, allowing for the generation
of values one at a time, on-demand."""


# Generator function to generate Fibonacci sequence
def fibonacci_generator(max):
    a, b = 0, 1
    while a <= max:
        yield a
        a, b = b, a + b


# Using the generator
fibonacci = fibonacci_generator(100)  # Create a generator object
for num in fibonacci:
    print(num)  # Prints Fibonacci numbers up to 100
