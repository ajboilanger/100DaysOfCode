# arrays take less memory and perform slightly faster than lists
# 90% of use cases can be solved with lists, don't try to over optimize if not needed

# to start using arrays, you need to import them
from array import array

# arrays are broken down into multiple parts, starting with a typecode
# this typecode means that only objects of that type are allowed into the array
# the example below shows an array with a typecode of 'i' for integer, and attempting to pass a floating point number in results in failure
numbers = array("i", [1, 2, 3])
numbers[0] = 1.0

# use arrays when working with a large sequence of numbers and have performance problems
