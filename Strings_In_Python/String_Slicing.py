# Author: Shubham Chawla

"""
In this code snippet we will check how to slice a string
using positive and negative slicing
"""

# Note 0 is optional in starting of slicing
a = "Harry,Shubham"

print(len(a))
print(a[:5])
print(a[0:5])

print(a[:-3])

print(a[-1:-3]) # This make no sense so not output
"""
in negative slicing take it as 
print(a[len(a)-1:len(a)-3]) this is how python make interpretation and returns output
"""
print(a[-4:-2])
print(a[len(a)-4:len(a)-2])
