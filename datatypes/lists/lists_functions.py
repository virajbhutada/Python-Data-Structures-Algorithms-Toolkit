# List Functions: Built-in list methods such as append, pop, extend, etc.

# Creating a list
my_list = [1, 2, 3, 4]

# Append: Adds an element at the end
my_list.append(5)
print("After append:", my_list)  # Output: [1, 2, 3, 4, 5]

# Pop: Removes and returns the last element
popped_element = my_list.pop()
print("After pop:", my_list)  # Output: [1, 2, 3, 4]
print("Popped element:", popped_element)  # Output: 5

# Extend: Adds all elements from another list
my_list.extend([6, 7])
print("After extend:", my_list)  # Output: [1, 2, 3, 4, 6, 7]

# Index: Find the position of an element
index_of_3 = my_list.index(3)
print("Index of 3:", index_of_3)  # Output: 2

# Count: Count occurrences of an element
count_of_2 = my_list.count(2)
print("Count of 2:", count_of_2)  # Output: 1

# Clear: Removes all elements from the list
my_list.clear()
print("After clear:", my_list)  # Output: []
