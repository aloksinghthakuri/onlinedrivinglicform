# Simple Calculator

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

print("Simple Calculator")
print("Operations: +  -  *  /")

a = float(input("Enter first number: "))
op = input("Enter operator: ")
b = float(input("Enter second number: "))

if op == "+":
    print("Result:", add(a, b))
elif op == "-":
    print("Result:", subtract(a, b))
elif op == "*":
    print("Result:", multiply(a, b))
elif op == "/":
    print("Result:", divide(a, b))
else:
    print("Invalid operator")


