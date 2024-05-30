"""
Exercise 3: Print characters from a string that are present at an even index number

Write a program to accept a string from the user and display characters that are present at an even index number.

For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
"""


def string_even_index(string):
    for i in string:
        if string.index(i) % 2 == 0:
            print(i+",", end=" ")
        else:
            pass


string_even_index("pynative")
