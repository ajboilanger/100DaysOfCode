letters = ["a", "b", "c"]

# Adding
letters.append("d")  # adds to end
letters.insert(0, "-")  # adds to indexed position
print(letters)

# Remove
letters.pop()  # removes from end
letters.pop(0)  # removes from indexed position
letters.remove("b")  # removes first occurrence of the object listed
print(letters)

del letters[0:1]  # allows for deletion of a range
print(letters)

letters.clear()  # clears the entire list
print(letters)
