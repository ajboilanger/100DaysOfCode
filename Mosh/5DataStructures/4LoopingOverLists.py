letters = ["a", "b", "c"]  # this creates a list of the letters a, b, and c.
# for letter in letters:
#     print(letter)
# for letter in enumerate(letters):
#     print(letter)
# this iterates over "letters" and returns each index, and the letter associated with it
for index, letter in enumerate(letters):
    print(index, letter)  # then the index and letter are printed

# the print statement returns the following:
# 0 a
# 1 b
# 2 c
