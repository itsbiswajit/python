"""
1. Create a Set
2. Print set Element.
3. Update Set Element
4. Insert Set element
5. Delete a Set Element
6. Delete Set
7. Copy a Set
8. Set comprehensions
"""
s = {10, 50, 20, "python", "language", "10"} # A set can store a mixture of string, integer, boolean, etc datatypes.
print(s)     # Note: There is no specific order for set elements to be printed

# Update Set Element:
# Set Is immutable, Existing elemnts can not be Updated. 
# Adding a Elements
s.add(25)
print(s)
for i in range(1, 6):
    s.add(i)
print(s)

# Set Method: union() or "|" operator, intersection() or "&" operator, difference() or "-" operator.
# Union: Two sets can be merged using union() function or | operator. 
# Both Hash Table values are accessed and traversed with merge operation perform 
# on them to combine the elements, at the same time duplicates are removed. 
s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6, 7, 8}
s3 = s1.union(s2)            # {1, 2, 3, 4, 5, 6, 7, 8}, Duplicates are removed. 
print("Sets Union using 'union()' method: ", s3)
s4= s1 | s2                  # {1, 2, 3, 4, 5, 6, 7, 8}, Duplicates are removed.
print("Sets Union using '|' operator: ", s4)
# Intersection: This can be done through intersection() or & operator.
# Common Elements are selected. They are similar to iteration over the Hash lists and 
# combining the same values on both the Table.
s3 = s1.intersection(s2)      # {3, 4}, Common Elements in the sets
print("Sets Intersection using 'intersection()' method: ", s3)
s4 = s1 & s2                  # {3, 4}, Common Elements in the sets
print("Sets Intersection using '&' operator: ", s4)
# Diference: To find differences between sets. Similar to finding differences in the linked list.
# This is done through difference() or – operator.
s3 = s1.difference(s2)        # Output: {1, 2}
print("Sets Difference using 'diference()' method: ", s3)
s4 = s1 - s2                  # Output: {1, 2}
print("Sets Difference using '-' operator: ", s4)


# Remove Set elements: remove(), discard(), pop()
s = {1, 2, 3, 4, 5}
s.remove(3) # IMPORTANT: a.remove(3) removes element "3" from the set a and if element is not found then it raises a KeyError.
print("Removed '3' from the set using 'remove()' method: ", s)
s.discard(4)    # Removes element "3" from the set a if it exists.
s.discard(6)    # Does nothing because "6" is not present in set and no error is raised unlike remove().
print("Removed '4' from the set using 'discard()': ", s)
e = s.pop()
print(f"Removed a arbitrary element '{e}' from the set using 'pop()' method: ", s)

s.clear()       # Removes all element and left set empty.
print("Removed all the elemenets from the set: ", s)

del s           # Delete the set()

# Copy: Using the assignment '=' operator (new_set = old_set) does not create a copy;
# it creates a reference to the original set. Changes made to new_set will also affect old_set.
# So, Use copy() method, or set() method to create a new set instance as below.
s = {1, 2, 3}
s1 = s.copy()
print("Copied set: ", s1)
s1 = set(s) # set() constructor creates a new set object.
s.add(5) # It should not change the value of 's1'
print("Copied set: ", s1)
# Using the assignment '=' operator (new_set = old_set) does not create a copy;
# it creates a reference to the original set. Changes made to new_set will also affect old_set.
s1 = s
s.add(4)
print("Added '4' to 's', value of 's1' has changed automatically: ", s1) # Output : {1, 2, 3, 4}