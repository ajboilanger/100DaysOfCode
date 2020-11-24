# a set is a collection with no duplicates

numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}

# the vertical bar creates a union, and will join them (prints "{1,2,3,4,5}")
print(first | second)  # {1,2,3,4,5}
# you can also print items that are in both the first and second set, which prints "{1}" as it is the only number that exists in both
print(first & second)  # {1}
# you can also find the differences, in this case it shows the objects that the first set has which the second does not
print(first - second)  # {2,3,4}
# you can also find items that are in one or the other, but not both
print(first ^ second)  # {2,3,4,5}
# sets are unordered collections, and cannot be accessed via index
# you can also apply logic to sets
if 1 in first:
    print("yes")
