def greet(name, greeting="Hello", *, age=None, **kwargs):
    """
    Greets a person with an optional greeting and age,
    and additional keyword arguments.
    """
    print(greeting, name + "!")
    if age is not None:
        print("You are", age, "years old.")
    if kwargs:
        print("Additional info:")
        for key, value in kwargs.items():
            print(key + ":", value)


# Example usage of the function


if __name__ == '__main__':
    name = "Alice"
    greet(name)  # Uses the default greeting "Hello"
    greet(name, greeting="Hi")  # Uses a custom greeting "Hi"
    greet(name, age=25)  # Provides an age as a keyword argument
    greet(name, city="New York", country="USA")  # Provides additional keyword arguments
