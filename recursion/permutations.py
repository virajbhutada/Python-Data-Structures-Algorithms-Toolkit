def permutations(arr):
    def permute(data, start, end):
        if start == end:
            result.append(data[:])
        else:
            for i in range(start, end + 1):
                data[start], data[i] = data[i], data[start]
                permute(data, start + 1, end)
                data[start], data[i] = data[i], data[start]

    result = []
    permute(arr, 0, len(arr) - 1)
    return result

# Test
arr = [1, 2, 3]
print(permutations(arr))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
