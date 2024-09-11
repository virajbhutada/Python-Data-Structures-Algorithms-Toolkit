# List Sorting: Sorting techniques applied to lists

# Basic sorting using the built-in sort() method
my_list = [3, 1, 4, 2, 5]
my_list.sort()  # Sort in ascending order
print("Sorted list:", my_list)  # Output: [1, 2, 3, 4, 5]

# Sorting in descending order
my_list.sort(reverse=True)
print("Sorted in descending order:", my_list)  # Output: [5, 4, 3, 2, 1]

# Sorting using sorted() function (returns a new sorted list)
original_list = [10, 2, 8, 6, 4]
sorted_list = sorted(original_list)
print("Original list:", original_list)  # Output: [10, 2, 8, 6, 4]
print("New sorted list:", sorted_list)  # Output: [2, 4, 6, 8, 10]

# Sorting a list of strings alphabetically
string_list = ['banana', 'apple', 'cherry']
string_list.sort()
print("Sorted string list:", string_list)  # Output: ['apple', 'banana', 'cherry']
