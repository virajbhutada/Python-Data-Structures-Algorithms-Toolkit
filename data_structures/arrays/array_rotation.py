def rotate_array(arr, d):
    n = len(arr)
    arr[:] = arr[d:n] + arr[0:d]

# Test
arr = [1, 2, 3, 4, 5, 6, 7]
rotate_array(arr, 2)
print(arr)  # Output: [3, 4, 5, 6, 7, 1, 2]
