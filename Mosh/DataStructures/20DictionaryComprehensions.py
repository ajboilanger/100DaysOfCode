# values = []

# for x in range(5):
#     values.append(x * 2)
"""
the iterable for this example is range 5
the loop variable is x
the expression is x * 2
[expression for item in items]
the line below is equal to lines 1 through 4 above
"""
list_value = [x * 2 for x in range(5)]
print(list_value)
print(type(list_value))
"""
these comprehensions can be used for sets or dictionaries using comprehensions
a set is just a set of values {1, 2, 3, 4} while a dictionary is a key value
pairing {1: "a", 2: "b", 3: "c", 4: "d"}
"""
dict_value = {x: x * 2 for x in range(5)}
print(dict_value)
print(type(dict_value))
set_value = {x * 2 for x in range(5)}
print(set_value)
print(type(set_value))

# Tuples cannot be created with this expression method
