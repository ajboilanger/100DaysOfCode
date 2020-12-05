numbers = [1, 2, 3]  # creates a list of numbers
print(*numbers)  # the * unpacks the list, and prints each value
print(numbers)  # this prints the default list
print(1, 2, 3)  # this prints the way that the first print statement will

# creates a range of 5 and puts it into a list called "values"
values = list(range(5))
# this also creates a list, without explicitly calling it
values1 = [*range(5), *"Hello"]
print(values)
print(values1)

first = [1, 2]  # creates a list
second = [3]  # creates a list
# combines the two lists above as well as adds new values
two_lists = [*first, "a", *second, *"Hello"]
print(two_lists)


# you can also unpack dictionaries, but that requires two asterisks
third = {"x": 1}
fourth = {"x": 10, "y": 2}
combined = {**third, **fourth, "z": 1}
# if you combine lists like this, and two key value pairs share the same key, it will use the most recent
print(combined)

"""
The unpacking operator can be used to take out (unpack) individual 
values in any iterable.
"""
