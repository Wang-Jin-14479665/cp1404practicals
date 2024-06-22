"""
Word Occurrences
Estimate: 20 minutes
Actual:   25minutes
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

longest_word_length = max(len(word) for word in sorted_word_count)  # Find the length of the longest word

for word, count in sorted_word_count.items():
    print(f"{word:<{longest_word_length}}: {count}")
