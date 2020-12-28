class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("eat")
# Animal: Parent or Base class
# Mammal: Child or Sub class


class Mammal(Animal):
    def walk(self):
        print("walk")

# Fish: Child or Sub Class


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
print(isinstance(m, object))
# This determines if the object passed through it is an instance of whatever class. Object works because "m" is an instance of Mammal
# which is an instance of Animal, which is an instance of "object"
print(issubclass(Mammal, object))
# This determines if an object is a subclass of another class. Mammal is a subclass of Animal, which is a subclass of object
# Therefore, mammal is a subclass of object and this returns True.
