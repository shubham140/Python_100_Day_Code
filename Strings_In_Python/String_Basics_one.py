# Author: Shubham Chawla
"""
Strings are most widely used data type in python in this code snippet we will touchbase on basics
of strings
"""
# Strings can be enclosed in single or double quotes
a = "Shubham Chawla"
b = 'Shubham Chawla'

# Multi-line strings are also available in python can be enclosed in triple single of double quotes

c = """Hello everyone
welcome in the word of python"""

print(a)
print(b)
print(c)

# We can get individual characters in string by use of index and index starts with 0 always

print(a[2])

# We can use for loop to iterate over big multi line string to print individual characters.

for _ in c:
    print(_)

