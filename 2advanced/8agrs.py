"""
1. *args: Arbitrary Positional Arguments
2. **kwargs: Arbitrary Keyword Arguments
"""
# Below code shows how *args collects multiple positional arguments into a 
# tuple and how **kwargs collects keyword arguments into a dictionary.

# *args example
def fun(*args):
    return sum(args)

print(fun(5, 10, 15))   

# **kwargs example
def fun(**kwargs):
    for k, val in kwargs.items():
        print(k, val)

fun(a=1, b=2, c=3)

# Using both *args and **kwargs
def student_info(*args, **kwargs):
    print("Subjects:", args)        # Positional arguments
    print("Details:", kwargs)       # Keyword arguments

# Passing subjects as *args and details as **kwargs
student_info("Math", "Science", "English", Name="Alice", Age=20, City="New York")