"""
1. Definne a Class
2. Create object of the Class
3. Class Veriable
4. Define a Class Veriable
5. Access Class Veriable (Directly Using Class name, using Object Name)
6. Update Class Varibale
7. Instance Variable
8. Define a Instance Veriable
9. Access Instance Veriable (Directly Using Class name, using Object Name)
10. Update Instance Variable
"""

class Engineer:          # Class Definition
    """
    Docstring for Engineer
    """
    degree = "B.Tech"    # Class Variable

    def __init__(self, name, age):
        self.name = name  # Instance Variable
        self.age = age    # Instance Variable
engnr1 = Engineer("Biswajit", 31)             # Creates an object of the Engineer class with name as "Biswajit" and age as 31.
print(engnr1.name, engnr1.age, engnr1.degree) # Access instance and class Veriable
engnr2 = Engineer("Aniket", 30)               # Creates an object of the Engineer class with name as "Aniket" and age as 30.
print(engnr2.name, engnr2.age, engnr2.degree) # Access instance and class Veriable

print(Engineer.degree)                        # Access class attribute directly
print ("Engineer.__doc__:", Engineer.__doc__)
print ("Engineer.__name__:", Engineer.__name__)
print ("Engineer.__module__:", Engineer.__module__)
print ("Engineer.__bases__:", Engineer.__bases__)
print ("Engineer.__dict__:", Engineer.__dict__)

# In Python, variables defined in a class can be either class variables or instance variables,
# And, understanding the distinction between them is crucial for object-oriented programming.

# Class Variables: These are the variables that are shared across all instances of a class. 
# It is defined at the class level, outside any methods. All objects of the class share the same value 
# for a class variable unless explicitly overridden in an object.
print(engnr1.degree)     # Access Class Variable via class name or object Name
print(Engineer.degree)
Engineer.degree = "Computer"  # IMPORTANT: Update Class Varibale using Class name, this will update variable in class level.
print("Degree of 'engnr1' is bacame 'Computer': ", engnr1.degree)     # Note: The 'degree' of both 'engnr1' and 'engnr2' will now become 'Computer'
print("Degree of 'engnr2' is bacame 'Computer': ", engnr2.degree)

# Instance Variables: Variables that are unique to each instance (object) of a class.
# These are defined within the __init__ method or other instance methods. Each object maintains its 
# own copy of instance variables, independent of other objects.
print(engnr1.name)     # Access Instance Variable via object Name
print(engnr2.name)
engnr1.name = "Halder" # Update Instance Varibale using object name
print(engnr1.name)     # Note: The 'degree' of 'engnr1'  will now become 'Halder'
print(engnr2.name)     # Note: The 'degree' of 'engnr2' will remain become 'Aniket'