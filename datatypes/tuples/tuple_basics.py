# Introduction to Tuples: Creation, and Immutability

# Creating a tuple
my_tuple = (1, 2, 3)
print("Tuple:", my_tuple)  # Output: (1, 2, 3)

# Tuples are immutable
try:
    my_tuple[0] = 10  # This will raise an error
except TypeError:
    print("Tuples are immutable and cannot be modified.")

# Creating a tuple with one element
single_element_tuple = (1,)
print("Single element tuple:", single_element_tuple)  # Output: (1,)
