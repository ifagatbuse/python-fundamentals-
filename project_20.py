# Project 20: Multiplication Table Generator
# Topic: loops + formatting

num_text = input("Enter a number to see its multiplication table: ")

if num_text.isdigit():
    num = int(num_text)
    print(f"\nMultiplication Table for {num}:")
    for i in range(1, 11):  # 1 to 10
        print(f"{num} x {i} = {num * i}")
else:
    print("Please enter a valid integer!")
