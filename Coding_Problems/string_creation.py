"""
Exercise 1A: Create a string made of the first, middle and last character

Write a program to create a new string made of an input string’s first, middle, and last character.

Given:

str1 = "James"
Expected Output:
Jms
"""


def str_creation(string):
    if len(string) % 2 == 0:
        center = len(string) // 2
        print(center)
    else:
        center = (len(string) - 1) // 2
        print(center)
    first = string[0]
    last = string[-1]
    print(first + string[center] + last)


str_creation("Shubham")
