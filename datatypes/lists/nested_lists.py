# Nested Lists: Working with lists within lists (2D/3D lists)

# 2D List (List of Lists)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Accessing elements in a 2D list
print("Element at row 1, column 2:", matrix[1][2])  # Output: 6

# Modifying elements in a 2D list
matrix[2][1] = 99
print("Modified matrix:", matrix)

# Iterating through a 2D list
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

# 3D List (List of Lists of Lists)
cube = [
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]],
    [[9, 10], [11, 12]]
]

# Accessing elements in a 3D list
print("Element at depth 2, row 1, column 0:", cube[2][1][0])  # Output: 11
