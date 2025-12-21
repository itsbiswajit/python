"""
1. Create a list            list=[]
2. Print List Element.      print(list)
3. Update List Element      list[index]=new_value
4. Insert element:          list.append(value), list.insert(index, value), list.extend(list1), list + list
5. Delete a list Element:   list.remove(value), l.pop(index), del list[index], del [start_index:end_index]
6. Reverse a list:          list.reverse(), list[::-1]
7. Copy a list:             list.copy()
8. List slicing:            [start:stop:step]
9. List comprehensions      new_list = [i for i in list if i>3]
10. Print Integer-Digit and String-Digits
11. Slicing List
12. Delete a list
"""
# Create List
l=[1, 5, "apple", "83"]
# Print a List
print(f"List: {l}")

# Update the list
l[2]="banana"
print(f"Updated list: {l}")

# Insert into list
# append(), insert(), extend()
l.append("new")
print(f"Added new element at the end: {l}")
l.insert(2,"ins")
print(f"Inserted a new element at index 2: {l}")
l.extend([3, 5, 7])
print("New Extented list: ", l)
l=l+[4, 2, 7]
print("Continated List: ", l)

# Delete from the list
# IMPORTANT: del, pop(), clear(), remove() (Note: In dictionary we dont have remove(), all other method are used in dictionary)
del l[2]                     # del: Remove the item with index '2'
print(f"New list after deleting index 2: {l}")
l1=[2,4,6,7,8]
del l1[2:4]                   # del: remove all the elements from index 2 to 4 (4 is exclusive).
print("New list after deleting from index 2 to 4 (4 is exclusive): ", l1)
del l1                        # del: Delete the whole list
l2=[2,4,6,7,8,3,1]
poped_last_item = l2.pop()    # pop(): Removed the last item from from list 'l2', If we dont pass any argument the by deafult it will remove the last item
print(f"New list after deleting last element: {l2}")
poped_last_item = l2.pop(-1)  # pop(): Removed the last item from from list 'l2', remove the last item by passing the index of last element
dele = l2.pop(4)              # pop(): Remove the index '4' item from list 'l2'
print(f"New list after deleting index 4 element: {l2}")
l2.clear()                    # clear(): Empty the List, l2 will now become '[]'
print("List Became Empty: ", l2)
l.remove("ins")               # remove(): Remove an item by using remove() method. Please note that this method is not available for dictionary.
print(f"New List after delete 'ins': {l}")

# Reverse a List
l=l[::-1]                     # slicing: reverse a list using slicing
print(f"Reverse of the list: {l}")
l.reverse()                   # reverse(): reverse a list using reverse() reverse method.
print(f"Reverse of the list: {l}")

# Copy a list
n=l.copy()                 # Returns a shallow copy of the dictionary
print(f"Copied List: {n}")


# List Comprehensip. Create a new list of all integers from the old list.
c=[i for i in l if isinstance(i, int)] # 'isinstance' checks if i is a integer type. Similarly, you can check string type 'isinstance (i, str)'
print(f"Comprehensip List: {c}")


# Check Integer-Digit and String-Digit. 1 is a digit where "1" is a string digit.
for elem in l:
    if isinstance(elem, int):
        print(f"{elem} is an integer digit")
    elif isinstance(elem, str) and elem.isdigit():
        print(f'"{elem}" is a string digit')
    else:
        print(f"{elem} is not a digit")


# List Slicing
print("\n----------List Slicing----------")
print(f"Elements from index 1 to 3 : ", l[1:4])        # characters from index 1 to 3
print(f"Elements from start to index 2 : ", l[:3])     # from start to index 2
print(f"Elements from index 3 to end : ", l[3:])       # from index 3 to end
n = l[0:-1:2] # [start:stop:step]                     # Print evry 2nd setp Elements 
print(f"List Slicing: {n}")