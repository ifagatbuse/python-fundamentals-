# Project 15: Count Vowels in a Sentence
# Topic: Strings + Loops + Conditions

text = input("Enter a sentence: ").lower()

vowels = "aeiou"
count = 0

# loop through each character
for ch in text:
    if ch in vowels:
        count += 1

print("Sentence:", text)
print("Number of vowels:", count)
