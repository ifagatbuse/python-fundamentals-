# Project 14: Find Min & Max in a List
# Topic: Lists + Loops + Conditions

numbers = [12, 45, 7, 34, 89, 2, 19]

# assume the first element is both min and max
min_num = numbers[0]
max_num = numbers[0]

# loop through the list
for n in numbers:
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n

print("Numbers:", numbers)
print("Minimum:", min_num)
print("Maximum:", max_num)
