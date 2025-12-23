"""
1. Class Method
2. Static Method
3. Instance Method
"""

"""
Class Method: A method bound to the class itself, defined with "@classmethod"
Can access class attributes and modify them.
Receives 'cls' as the first argument representing the class.
Often used for operations that modify or interact with class-level data.
Can be overridden in subclasses, with 'cls' referring to the subclass.
Typically used when the method needs access to class-level data.
Useful when dealing with class-level functionality and shared attributes.
"""
class MyClass:
    class_variable = 0

    def __init__(self, value):
        self.instance_variable = value

    @classmethod
    def class_method(cls, x):
        cls.class_variable += x
        return cls.class_variable

# Creating instances of the class
obj1 = MyClass(5)
obj2 = MyClass(10)

# Calling the class method
print(MyClass.class_method(3))  # Output: 3
print(MyClass.class_method(7))  # Output: 10


"""
Static Method: A method that does not receive an implicit first argument ('self' or 'cls'), defined with "@staticmethod"
Cannot access or modify class or instance attributes.
No implicit first argument is passed to the method.
Typically used for utility functions that don't depend on instance or class state.
Can be called directly via the class or subclass, but not overridden.
Suitable when the method doesn't rely on instance or class attributes.
Handy for standalone functions related to the class but not dependent on its state.
"""
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

    @staticmethod
    def subtract(x, y):
        return x - y

# Using static methods without creating an instance
print(MathOperations.add(5, 3))        # Output: 8
print(MathOperations.subtract(10, 4))  # Output: 6

"""
Instance Method: A method defined within a class, taking `self` as the first parameter, representing the instance.
A method defined within a class, taking `self` as the first parameter, representing the instance.
Can access and modify instance attributes.
Receives `self` as the first argument representing the instance.
Commonly used for operations specific to individual instances.
Can be overridden in subclasses, with 'self' referring to the subclass instance.
Preferred when the method operates on instance-specific attributes.
Essential for modifying and accessing instance attributes and behaviors.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."


# Creating an instance of the class
person1 = Person("Kishan", 20)

# Calling the instance method
print(person1.introduce())  # Output: Hi, I'm Kishan and I'm 30 years old.

