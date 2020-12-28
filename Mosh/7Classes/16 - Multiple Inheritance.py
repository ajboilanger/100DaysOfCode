class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Employee, Person):
    pass


manager = Manager()
manager.greet()
# This will check to see if the manager class has the Greet object. If not, it will look at the first inheritance class, in this case Employee


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFish(Flyer, Swimmer):
    pass

# A good example of multiple inheritance is shown above, where the class that has multiple inheritances is inheriting from classes that have no similarities
