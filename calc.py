print("Simple Calculator")
print("Available operators: +, -, *, /")
print("Type q to quit")

while True:
    first_input = input("first number: ")

    if first_input == "q":
        print("bye")
        break

    operator = input("operator: ")

    if operator == "q":
        print("bye")
        break

    second_input = input("second number: ")

    if second_input == "q":
        print("bye")
        break

    try:
        a = int(first_input)
        b = int(second_input)

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

    except ValueError:
        print("please enter numbers only")

    print()
