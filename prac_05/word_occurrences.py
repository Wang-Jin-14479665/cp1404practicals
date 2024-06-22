"""
Word Occurrences
Estimate: 20 minutes
Actual:    minutes
"""

text = input("Text: ")

words = text.split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

sorted_word_count = dict(sorted(word_count.items()))  # Sort the elements in the dictionary

for word, count in sorted_word_count.items():
    print(f"{word}: {count}")
