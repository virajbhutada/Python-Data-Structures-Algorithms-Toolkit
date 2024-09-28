# Dictionary Manipulations: Adding, Removing, and Updating Elements

# Adding new key-value pair
my_dict["date"] = 4
print("After adding:", my_dict)  # Output: {'apple': 1, 'banana': 2, 'cherry': 3, 'date': 4}

# Updating a value
my_dict["apple"] = 10
print("After updating:", my_dict)  # Output: {'apple': 10, 'banana': 2, 'cherry': 3, 'date': 4}

# Removing a key-value pair
del my_dict["banana"]
print("After removing banana:", my_dict)  # Output: {'apple': 10, 'cherry': 3, 'date': 4}
