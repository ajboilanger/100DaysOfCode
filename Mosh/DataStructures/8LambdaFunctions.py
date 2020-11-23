items = [
    ("Product1", 10),
    ("Product2", 5),
    ("Product3", 1),
]

# def sort_item(item):
#     return item[1]

# the lambda function replaces what is seen on lines 8 and 9.
items.sort(key=lambda item: item[1])
print(items)
