a = int(input("first_num:"))
operator = input("operator(+,-,*,/):")
b = int(input("Second_num:"))

if operator == "+":
    result = a + b
elif operator == "-":
    result = a - b
elif operator == "*":
    result = a * b
elif operator == "/":
    result = a / b
else:
    result = "unknown operator"

print("result",result)
