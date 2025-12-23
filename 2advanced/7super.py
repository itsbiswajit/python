"""
In Python, the super() function is used to call methods from a parent (superclass) inside a
child (subclass). It allows you to extend or override inherited methods while still reusing
the parents functionality.
"""
class Mammal:
    def __init__(self, name):
        print(name, "is a mammal")

class CanFly(Mammal):
    def __init__(self, name):
        print(name, "cannot fly")
        super().__init__(name)

class CanSwim(CanFly):
    def __init__(self, name):
        print(name, "cannot swim")
        super().__init__(name)

class Animal(CanSwim):
    def __init__(self, name):
        super().__init__(name)

dog = Animal("Dog")