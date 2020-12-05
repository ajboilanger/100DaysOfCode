"""
Find the most repeated character in the following sentence.
"""

sentence = list("This is a common interview question")

print(sentence)

char_frequency = {}
for char in sentence:
    if char in char_frequency:
        char_frequency[char] +=
    else:
        char_frequency[char] = 1

print(char_frequency)