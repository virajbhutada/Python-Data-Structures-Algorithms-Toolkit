# Built-in Dictionary Methods: get(), items(), keys(), values()

my_dict = {"apple": 1, "banana": 2}

# get() method
print("Get value of 'apple':", my_dict.get("apple"))  # Output: 1

# items() method (key-value pairs)
print("Dictionary items:", my_dict.items())  # Output: dict_items([('apple', 1), ('banana', 2)])

# keys() method (keys only)
print("Dictionary keys:", my_dict.keys())  # Output: dict_keys(['apple', 'banana'])

# values() method (values only)
print("Dictionary values:", my_dict.values())  # Output: dict_values([1, 2])
