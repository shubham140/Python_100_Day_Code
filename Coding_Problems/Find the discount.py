"""
Create a function that takes two arguments:
the original price and the discount percentage as integers and returns the final price after the discount.
"""

"""
Examples

dis(1500, 50) ➞ 750.0

dis(89, 20) ➞ 71.2

dis(100, 75) ➞ 25.0
"""


def dis(price, discount):
    a = price - ((discount / 100) * price)
    print(a)


dis(100, 75)
