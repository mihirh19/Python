# Example code for decorators in Python

# Define a decorator
def uppercase_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()

    return wrapper


# Define a function
@uppercase_decorator
def greet(name):
    return f"Hello, {name}!"


# Call the decorated function
greeting = greet("John")
print(greeting)
