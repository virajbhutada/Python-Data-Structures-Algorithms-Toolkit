# Built-in String Methods: split(), join(), replace()

my_string = "apple,banana,cherry"

# split() method
fruits = my_string.split(",")
print("Split string:", fruits)  # Output: ['apple', 'banana', 'cherry']

# join() method
joined_string = "-".join(fruits)
print("Joined string:", joined_string)  # Output: apple-banana-cherry

# replace() method
replaced_string = my_string.replace("banana", "orange")
print("Replaced string:", replaced_string)  # Output: apple,orange,cherry
