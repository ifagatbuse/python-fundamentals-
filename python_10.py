# Project 10: List Analyzer
# Topic: Functions with Loops

def calculate_sum(numbers):
    total = 0
    for n in numbers:
        total += n
    return total

def calculate_average(numbers):
    return calculate_sum(numbers) / len(numbers)

# test list
nums = [10, 20, 30, 40, 50]

print("Numbers:", nums)
print("Sum:", calculate_sum(nums))
print("Average:", calculate_average(nums))
