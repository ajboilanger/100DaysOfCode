from sys import getsizeof

values = (x * 2 for x in range(1000000000))
print("gen:", getsizeof(values))

values = [x * 2 for x in range(100000)]
print("list:", getsizeof(values))

"""
Use a generator object when working with a very large or potentially infinite
amount of data. It will allow you to keep the size of the generator consistent
despite the range used. Compared with a list, dict, or set, which will grow
consistently which each additional value in the range.

When using a generator, you're unable to store items in memory so you'll be unable
to get the total number of objects you're working with ahead of time as they're
only generated once iterated upon.
"""
