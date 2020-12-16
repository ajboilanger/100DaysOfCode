# Naming convention for classes is first letter of each word capitalized, with no underscores

class Point:
    # functions should have at least one parameter
    def draw(self):
        print("draw")


point = Point()
print(type(point))
print(isinstance(point, int))
