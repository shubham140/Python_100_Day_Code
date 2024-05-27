def calculator():
    d = input("Hey Shubham what operation you wanna perform")
    if d == "+":
        print("You opted addition")
        a = input("Please enter first number")
        b = input("Please enter second number")
        print(int(a) + int(b))
    elif d == "-":
        print("You opted subtraction")
        a = input("Please enter first number")
        b = input("Please enter second number")
        print(a - b)
    elif d == "*":
        print("You opted multiplication")
        a = input("Please enter first number")
        b = input("Please enter second number")
        print(a * b)
    elif d == "//":
        print("You opted floor division")
        a = input("Please enter first number")
        b = input("Please enter second number")
        print(a // b)
    elif d == "**":
        print("You opted floor expo operation")
        a = input("Please enter first number")
        b = input("Please enter second number")
        print(a ** b)

calculator()
