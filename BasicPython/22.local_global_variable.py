# Example code using local and global variables

# Global variable
global_var = 10


# Function that uses local and global variables
def my_function():
    # Local variable
    local_var = 5

    # Accessing global variable within a function
    global global_var
    global_var = global_var + local_var

    # Printing local and global variables
    print("Local Variable:", local_var)
    print("Global Variable:", global_var)


# Call the function
my_function()

# Printing global variable after function call
print("Global Variable after function call:", global_var)
