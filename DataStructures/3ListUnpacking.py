numbers = [1, 2, 3]
# first = numbers[0]
# second = numbers[1]
# third = numbers[3]
first, second, third = numbers
# Equals what is seen on lines 2, 3, and 4. List unpacking.
# The number of things on the left side of the equation should equal the amount of items in the list
# If you have a long list but only want the first X of them, you can pack the remainder into a separate list called "other"
numbers2 = [1, 2, 3, 4, 4, 4, 4, 4]
first, second, *other = numbers2
print(first)
print(second)
print(other)
numbers3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
first, *other, last = numbers3
print(first, last)
print(other)
