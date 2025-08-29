# Project 16: Palindrome Checker
# Topic: Strings + Conditions

text = input("Enter a word: ").lower()

# reverse the string
reversed_text = text[::-1]

if text == reversed_text:
    print(text, "is a palindrome ")
else:
    print(text, "is NOT a palindrome ")
