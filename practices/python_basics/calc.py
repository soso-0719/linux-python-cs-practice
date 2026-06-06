from datetime import datetime

HISTORY_FILE = "history.txt"

def calculate(a, operator, b):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "cannot divide by zero"
        return a / b
    else:
        return "unknown operator"


def save_history(a, operator, b, result):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"{now} | {a} {operator} {b} = {result}\n"

    with open(HISTORY_FILE, "a", encoding="utf-8") as file:
        file.write(line)


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

        result = calculate(a, operator, b)
        print("result:", result)

        save_history(a, operator, b, result)

    except ValueError:
        print("please enter numbers only")

    print()