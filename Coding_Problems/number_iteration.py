"""
Exercise 2: Print the sum of the current number and the previous number

Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous
number.
"""


def iteration(num):
    for i in range(1, num):
        print("current number is: " + str(i)+"and previous number is "+str(i-1), end=" ")
        print("Sum: " + str(int(i) + int(i - 1)))


iteration(10)
