"""
1. Public Members: Accessible from anywhere.
2. Protected Members: Accessible within the class and its subclasses.
3. Private Members: Accessible only within the class.
4. Accesing Private Member using a method and name mangling
5. Modifying Private Member using a method
"""

class Dog:
    def __init__(self, name, breed, age):
        self.name = name     # Public attribute
        self._breed = breed  # Protected attribute
        self.__age = age     # Private attribute

    # Public method
    def get_info(self):
        return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

    # Getter and Setter for private attribute
    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Invalid age!")

dog = Dog("Buddy", "Labrador", 3)

print(dog.name)  # Accessing public member
print(dog._breed)  # # Accessing protected member, Accessible but discouraged outside the class
print("Accessing Private member 'age' using getter: ", dog.get_age()) # Accessing private member using getter
print("Accessing Private member 'age' using name mangling: ", dog._Dog__age) # Accessing private member using name mangling

dog.set_age(5) # Modifying private member using setter
print(dog.get_info())

"""
Explanation:
Public Members: Easily accessible, such as name.
Protected Members: Used with a single _, such as _breed. Access is discouraged but allowed in subclasses.
Private Members: Used with __, such as __age. Access requires getter and setter methods.
"""