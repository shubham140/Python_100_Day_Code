"""
Exercise 4: Arrange string characters such that lowercase letters should come first

Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

Given:
str1 = PyNaTive

Expected Output:
yaivePNT
"""


def arrange_string(string):
    new_str_lower = str()
    new_str_upper = str()
    for i in string:
        if i.islower():
            new_str_lower += i
        else:
            new_str_upper += i
    print(new_str_lower + new_str_upper)


arrange_string("PyNaTive")
