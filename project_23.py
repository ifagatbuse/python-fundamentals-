# Project 23: Safe Division
# Topic: try/except for robust input handling

def to_float(text: str):
    try:
        return float(text)
    except ValueError:
        return None

a_txt = input("Enter first number: ")
b_txt = input("Enter second number: ")

a = to_float(a_txt)
b = to_float(b_txt)

if a is None or b is None:
    print("Error: Please enter valid numbers.")
else:
    try:
        result = a / b
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
