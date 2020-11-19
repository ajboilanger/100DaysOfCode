# numbers = [3, 51, 2, 8, 6]
# # numbers.sort()  # sorts in ascending order
# # print(numbers)

# # passing this argument through will sort in reverse order, or descending
# # numbers.sort(reverse=True)
# # print(numbers)

# # print(sorted(numbers, reverse=True))
# print(numbers)

items = [
    ("Product1", 10),
    ("Product2", 5),
    ("Product3", 1),
]


def sort_item(item):
    return item[1]


items.sort(key=sort_item, reverse=True)
print(items)
