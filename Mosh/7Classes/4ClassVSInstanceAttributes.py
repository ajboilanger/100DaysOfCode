class Point:
    default_color = "red"  # class level attribute

    def __init__(self, x, y):
        self.x = x  # instance attribute
        self.y = y  # instance attribute

    def draw(self):
        print(f"Point ({self.x}, {self.y})")  # instance attribute


Point.default_color = "yellow"
point = Point(1, 2)
print(point.default_color)
print(Point.default_color)
point.z = 10
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()


"""
Class level attributes are shared across the entire class. For example, all humans
have two ears and two eyes by default.

Instance level attributes are those which can be attributed to an individual. Example
John has Brown hair. Mary has Blue eyes.
"""
