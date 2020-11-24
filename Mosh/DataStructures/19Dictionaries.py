# a dictionary is a collection of key value pairs, such as a phone book (name -> contact info)

point = {"x": 1, "y": 2}  # method 1 to create a dictionary
point = dict(x=1, y=2)  # method 2 to create a dictionary
print(point["x"])  # dictionaries can be accessed by index (prints 1)
point["x"] = 10  # changing the value of a key
point["z"] = 20  # adding a new key value pair
print(point)  # printing the dictionary (prints {'x': 10, 'y': 2, 'z': 20})
if "a" in point:  # you can check to see if keys or values exist in the dictionary
    print(point["a"])  # and then attempt to print them
# you can also set a default value to print should the object not be found (prints 0)
print(point.get("a", 0))
del point["x"]  # deleting a key value pair
print(point)  # printing the dictionary (prints {'y': 2, 'z': 20})
for key, value in point.items():  # you can also loop through dictionaries
    print(key, value)  # this prints (y 2) and (z 20) on separate lines
