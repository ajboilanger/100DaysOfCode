from abc import ABC, abstractmethod


class TextBox:
    def draw(self):
        print("Textbox")


class DropDownList:
    def draw(self):
        print("DropDownList")


def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
textbox = TextBox()
draw([ddl, textbox])

# To achieve polymorphic behavior, you don't necessarily need the base class. Line 16 is simply checking for a draw function within the class, and will iterate over it if found.
# "If it walks like a duck, and quacks like a duck... then it's a duck."
# That said, the base class is good practice to help ensure standards.
