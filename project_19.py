# Project 19: Simple Calculator
# Topic: input + conditions + arithmetic operators

print("Simple Calculator (+, -, *, /)")
print("Type 'quit' anytime to stop.")

while True:
    num1 = input("Enter first number: ").strip()
    if num1.lower() == "quit":
        break
    num2 = input("Enter second number: ").strip()
    if num2.lower() == "quit":
        break
    op = input("Enter operator (+, -, *, /): ").strip()
    if op.lower() == "quit":
        break

    # check if inputs are numbers
    if not (num1.replace(".", "", 1).isdigit() and num2.replace(".", "", 1).isdigit()):
        print("Invalid number. Try again!")
        continue

    num1 = float(num1)
    num2 = float(num2)

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Error: Division by zero ❌")
            continue
        result = num1 / num2
    else:
        print("Invalid operator. Use +, -, * or /")
        continue

    print("Result:", result)
