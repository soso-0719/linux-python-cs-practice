print("Simple Calculator")
print("Available operators: +, -, *, /")

a = int(input("first number: "))
operator = input("operator: ")
b = int(input("second number: "))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    if b == 0:
        result = "cannot divide by zero"
    else:
        result = a / b
else:
    result = "unknown operator"

print("result:", result)
