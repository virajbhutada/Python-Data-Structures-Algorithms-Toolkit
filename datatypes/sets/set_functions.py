# Built-in Set Functions: issubset(), issuperset(), isdisjoint()

set1 = {1, 2, 3}
set2 = {1, 2}
set3 = {4, 5}

# Check if set2 is a subset of set1
print("Is set2 a subset of set1?", set2.issubset(set1))  # Output: True

# Check if set1 is a superset of set2
print("Is set1 a superset of set2?", set1.issuperset(set2))  # Output: True

# Check if set1 and set3 are disjoint
print("Are set1 and set3 disjoint?", set1.isdisjoint(set3))  # Output: True
