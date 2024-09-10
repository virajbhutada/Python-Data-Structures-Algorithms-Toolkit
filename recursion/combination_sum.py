def combination_sum(candidates, target):
    def backtrack(start, path, target):
        if target == 0:
            result.append(path)
            return
        for i in range(start, len(candidates)):
            if candidates[i] <= target:
                backtrack(i, path + [candidates[i]], target - candidates[i])

    result = []
    backtrack(0, [], target)
    return result

# Test
candidates = [2, 3, 6, 7]
target = 7
print(combination_sum(candidates, target))  # Output: [[2, 2, 3], [7]]
