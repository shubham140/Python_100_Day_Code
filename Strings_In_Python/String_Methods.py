# Author: Shubham Chawla


"""
In this code snippet we will work all most user string methods available
and its use cases along with that
"""

a = "Shubham Chawla"

# prints string in upper case
print(a.upper())

# prints string in lower case
print(a.lower())

# prints one char in capital form rest all in  lower case
print(a.capitalize())

# returns bool if string is alpha numeric
print(a.isalnum())

# returns bool if string is alpha characters
print(a.isalpha())

# finds first index of char in string
print(a.find("h"))

# replace a string with another string
print(a.replace("Chawla", "chawla"))

# converts string to list
print(a.split())
