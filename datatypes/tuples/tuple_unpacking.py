# Tuple Unpacking: Assigning tuple elements to variables

my_tuple = (1, 2, 3)

# Unpacking the tuple
a, b, c = my_tuple
print("Unpacked values:", a, b, c)  # Output: 1 2 3

# Using '*' for variable-length unpacking
my_tuple2 = (1, 2, 3, 4, 5)
first, *middle, last = my_tuple2
print("First:", first, "Middle:", middle, "Last:", last)  # Output: 1 [2, 3, 4] 5
