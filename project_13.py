# Project 13: Character Counter
# Topic: Strings + Loops + Dictionary

text = input("Enter a sentence: ").lower()

char_count = {}

for ch in text:
    if ch != " ":  # counting spaces
        if ch in char_count:
            char_count[ch] += 1
        else:
            char_count[ch] = 1

print("\nCharacter frequencies:")
for char, count in char_count.items():
    print(char, ":", count)
