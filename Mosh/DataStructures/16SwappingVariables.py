x = 10
y = 11

# this woudl be the traditional way to swap a variable, using a third as a placeholder/backup of one of the two original variables
z = x
x = y
y = z

print("x", x)
print("y", y)

# in python this can be done like so
x = 15
y = 20

x, y = y, x

print("x", x)
print("y", y)

# this happens as we're defining a tuple at the end of line 16
# this means that x, y = y,x is equal to x, y = (20, 15), meaning x = 20 and y = 15 after unpacking it.
