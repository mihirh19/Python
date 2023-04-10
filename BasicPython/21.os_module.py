import os

# Example code using os module

# Get the current working directory
current_dir = os.getcwd()
print("Current Directory:", current_dir)

# Create a new directory
new_dir = os.path.join(current_dir, "new_directory")
os.mkdir(new_dir)
print("New Directory Created:", new_dir)

# Change the current working directory
os.chdir(new_dir)
print("Changed Directory:", os.getcwd())

# Create a new file
new_file = os.path.join(new_dir, "new_file.txt")
with open(new_file, "w") as f:
    f.write("Hello, World!")
print("New File Created:", new_file)

# Rename a file
renamed_file = os.path.join(new_dir, "renamed_file.txt")
os.rename(new_file, renamed_file)
print("File Renamed:", renamed_file)

# Check if a file or directory exists
if os.path.exists(renamed_file):
    print("File/Directory Exists.")
else:
    print("File/Directory Does Not Exist.")

# Remove a file
os.remove(renamed_file)
print("File Removed:", renamed_file)

# Remove a directory
os.rmdir(new_dir)
print("Directory Removed:", new_dir)
