# Project 12: Word Counter
# Topic: Strings + Loops + Dictionary

text = input("Enter a sentence: ").lower()

words = text.split()
word_count = {}

for w in words:
    if w in word_count:
        word_count[w] += 1
    else:
        word_count[w] = 1

print("\nWord frequencies:")
for word, count in word_count.items():
    print(word, ":", count)
