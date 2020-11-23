items = [
    ("Product1", 10),
    ("Product2", 9),
    ("Product3", 12),
]

# prices = list(map(lambda item: item[1], items))
# this does the same as the code in line 7, but is shorter and more efficient
prices = [item[1] for item in items]


# filtered = list(filter(lambda item: item[1] >= 10, items))
# this does the same as the code on line 12, but is shorter and more efficient
filtered = [item for item in items if item[1] >= 10]
print(prices)
print(filtered)
