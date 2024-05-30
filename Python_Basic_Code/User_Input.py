"""
This simple code snippet will show how to take input from users
"""

a = input("Please enter 1st number: ")
b = input("Please enter 2nd number: ")
print(a + b)  # out is not sum of numbers but concat of two number why??

"""
By default it takes input from user in string and that's why in above code concatenation is happening 
to change to int we need to perform explicit conversion below example shows how to do
"""
a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
print(a + b)
# Here actual sum happened
