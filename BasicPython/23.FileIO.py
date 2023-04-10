"""We then use various file I/O functions to read and manipulate the contents of the file. We first use the read()
function to read the entire file into a string. Then, we use the readline() function to read the file line by line in
a loop. We also use the seek() function to move the file pointer to a specific position in the file, and the tell()
function to get the current position of the file pointer. These functions provide powerful capabilities for reading
and manipulating files in Python."""

# Example code for file I/O in Python

# Create a sample file
with open("example.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")
    f.write("Line 4\n")
    f.write("Line 5\n")

# Reading the file using read() function
with open("example.txt", "r") as f:
    contents = f.read()
    print("Contents of the file using read():")
    print(contents)

# Reading the file using readline() function
with open("example.txt", "r") as f:
    line = f.readline()
    print("Contents of the file using readline():")
    while line:
        print(line.strip())
        line = f.readline()

# Using seek() function to move file pointer
with open("example.txt", "r") as f:
    print("Contents of the file after seek():")
    f.seek(6)  # Move the file pointer to position 6
    contents = f.read()
    print(contents)

# Using tell() function to get current file pointer position
with open("example.txt", "r") as f:
    print("Current file pointer position:", f.tell())
