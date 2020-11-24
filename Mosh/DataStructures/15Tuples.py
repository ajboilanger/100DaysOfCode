# tuples are immutable, meaning objects cannot be added or removed
# real world example would be something where you don't want values accidentally added or removed

# tuples make use of parentheses instead of square brackets
# you can also use no parantheses, "point = 1, 2" would be considered a tuple
# a single object can also be a tuple without parantheses if you add a trailing comma such as "point = 1,"

# creates a tuple with 1, 2, and 3 inside
point = (1, 2, 3)
# prints the object of the point tuple in the first and second index spots (1 and 2)
print(point[0:2])
# unpacks the tuple to x, y, and z
x, y, z = point
# tuples can also be used as below
if 10 in point:
    print("exists")
# as tuples are immutable, trying this will result in a TypeError of 'tuple' object does not support assignment
# point[0] = 10
