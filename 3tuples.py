"""
1. Create a Tuple
2. Print Tuple
3. Tuple Slicing
4. Update Tuple
5. Reverse a Tuple
6. Count Occurance of an element in Tuple
7. Delete a Tuple
"""
t = (5, 'Welcome', 7, 'Python')
print("Tuple: ", t)

# 3. Tuple Slicing
print("\n----------Tuple Slicing----------")
print(f"Elements from index 1 to 3 : ", t[1:4])        # characters from index 1 to 3
print(f"Elements from start to index 2 : ", t[:3])     # from start to index 2
print(f"Elements from index 3 to end : ", t[3:])       # from index 3 to end
n = t[0:-1:2] # [start:stop:step]                      # Print every 2nd setp Elements 
print(f"Tuple Slicing: {n}")

# 4. Updating Tuple
#Tuples in Python are immutable, meaning their elements cannot be changed directly after creation.
# To "update" a tuple, you must create a new tuple using workarounds such as converting it to a list, using concatenation, or using slicing and unpacking. 
# Original tuple
fruits = ("apple", "banana", "cherry")
print(f"Original tuple: {fruits}")
y = list(fruits)    # Convert to a list
y[1] = "kiwi"       # Modify the list (e.g., change an element)
fruits = tuple(y)   # Convert back to a tuple
print(f"Updated tuple: {fruits}")
# Original tuple
tup1 = (1, 2, 3, 4, 5)
print(f"Original tuple: {tup1}")
# Update the value at index 2 (which is '3') to '100'
# Slice up to index 2: tup1[:2] gives (1, 2)
# The new value must be a tuple: (100,)
# Slice from index 3 to the end: tup1[3:] gives (4, 5)
tup2 = tup1[:2] + (100,) + tup1[3:]  # Concatenition
print(tup2)
tup3 = (*tup1[:2], 100, *tup1[3:])    # Tup;e Unpacking using '*', then creating a new tuple 'tup3'.
print(tup3)
print(f"Original tuple is still unchanged: {tup1}")      # tup1 is still remain unchanged.


# Delete aTuple
tup4 = (0, 1, 2, 3, 4)
del tup4

