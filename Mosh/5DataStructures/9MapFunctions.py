items = [
    ("Product1", 10),
    ("Product2", 5),
    ("Product3", 1),
]

# prices = []
# for item in items:
#     prices.append(item[1])

# x = map(lambda item: item[1], items)
# for item in x:
#     print(item)

prices = list(map(lambda item: item[1], items))
print(prices)
