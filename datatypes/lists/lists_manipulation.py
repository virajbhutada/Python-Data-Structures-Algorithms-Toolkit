# List Manipulations: Insertion, Deletion, and Reversing

# Inserting elements
my_list = [1, 2, 3, 4]
my_list.insert(2, 10)  # Insert 10 at index 2
print("After insertion:", my_list)  # Output: [1, 2, 10, 3, 4]

# Appending elements
my_list.append(5)  # Append 5 to the end
print("After appending:", my_list)  # Output: [1, 2, 10, 3, 4, 5]

# Deleting elements by value
my_list.remove(10)  # Remove the element 10
print("After removing 10:", my_list)  # Output: [1, 2, 3, 4, 5]

# Deleting elements by index
del my_list[1]  # Remove element at index 1
print("After deleting index 1:", my_list)  # Output: [1, 3, 4, 5]

# Reversing the list
my_list.reverse()
print("After reversing:", my_list)  # Output: [5, 4, 3, 1]
