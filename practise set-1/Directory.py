# write a python program to print content of the directory using the os module.
import os

# Specify the directory path (use '.' for current directory)
directory_path = '/GITPRACTISE'

# Get list of files and folders in the directory
contents = os.listdir(directory_path)

# Print each item
print("Contents of the directory:")
for item in contents:
    print(item)
