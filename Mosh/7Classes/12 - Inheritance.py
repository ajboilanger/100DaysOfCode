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
m.eat()
print(m.age)
