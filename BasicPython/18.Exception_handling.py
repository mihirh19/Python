# Example code with exception handling
try:
    # Code that may raise an exception
    num1 = 10
    num2 = 0
    result = num1 / num2  # Division by zero, will raise ZeroDivisionError
    print("Result:", result)  # This line will not be executed due to the exception
except ZeroDivisionError:
    print("Error: Division by zero occurred.")  # Exception handling code for ZeroDivisionError
except Exception as e:
    print("Error:", e)  # Generic exception handling code for other types of exceptions
else:
    print("No error occurred.")  # Executed if no exception is raised
finally:
    print("Finally block executed.")  # Always executed, whether an exception is raised or not
