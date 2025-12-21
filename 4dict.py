"""
1. Create a Dict
2. Print Dictionary Element.
3. Update Dictionary Element
4. Insert element
5. Delete a Dictionary Element
6. Delete Dictionary
7. Copy a Dictionary
8. Dictionary comprehensions
"""
d={1: "I", 2: "am", 3: "Python", 4: "Language", 5: "Learning"}
print()

# Update Dictionary
d["age"] = 22        # Inserting a new key-value pair
d[1] = "Python dict" # Updating an existing value
# Updates the dictionary with the elements from another dictionary. update() method in Dictionary
d1 = {'A': 'Geeks', 'B': 'For', }
d2 = {'B': 'Geeks', 'C': 'Python'}
d1.update(d2)         # update the value of key 'B'
print("Concatinated two dictionary: ", d1)
d1.update(A='Hello')   # using keyword arguments
print("Updated value of 'A' using update() method: ", d1)


# Delete from the Dict
# IMPORTANT: del, pop(), popitem(), clear()(Note: In dictionary we don't have remove(), all other method are used in dictionary)
del d[2]                         # del: Remove the item with key '2'
print(f"New Dict after deleting key 2: {d}")
del d                            # pop(): Delete the whole dictionary
d={1: "I", 2: "am", 3: "Python", 4: "Language"}
key, value = d.popitem()         # pop(): Removed the last item from from dict 'd'.
value = d.pop(3)                 # pop(): Remove the key '3' item from dict 'd'
print(f"New Dict after deleting index 4 element: {d}")
d.clear()                    # clear(): Empty the Dict, d will now become '{}'
print("Dict Became Empty: ", d)

# Iterating through the dictionary items
d={1: "I", 2: "am", 3: "Python", 4: "Language", 5: "Learning"}
for key in d.keys():            # Iterate over keys
    print(key)
for value in d.values():        # Iterate over values
    print(value)
for key, value in d.items():    # Iterate over key-value pairs
    print(f"{key}: {value}")

# Copy a Dict
n=d.copy()               # Returns a shallow copy of the dictionary
print(f"Copied List: {d}")

# Returns the value for the given key
print("Value of key '5': ", d.get(5, "Default Value if dont find"))


# Dictionary comprehensions
# new_dict = {key_expression: value_expression for item in iterable}
squares = {x: x*x for x in range(1, 6)}
keys = ['apple', 'orange', 'banana']
values = [0.40, 0.35, 0.25]
prices = {k: v for k, v in zip(keys, values)}    # Merge two lists into a dictionary
original_dict = {'Jane': 'Python', 'Jade': 'JavaScript', 'John': 'Python', 'Doe': 'JavaScript'}
# Create a new dictionary containing only developers who like Python
python_devs = {name: language for name, language in original_dict.items() if language == 'Python'}
# Output: {'Jane': 'Python', 'John': 'Python'}