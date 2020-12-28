class Animal:
    def eat(self):
        print("eat")


class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    # Statement that doesn't do anything, as you cannot have an empty class.
    pass

# Avoid multi-level inheritance as much as possible, and try to limit it to one or two levels
# In the code above, the Chicken is a Bird, which is an Animal. But as chickens "cannot fly" they should be unable to call the fly object.
