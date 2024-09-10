def max_product_subarray(nums):
    max_prod = min_prod = result = nums[0]

    for i in range(1, len(nums)):
        curr = nums[i]
        temp_max = max(curr, max_prod * curr, min_prod * curr)
        min_prod = min(curr, max_prod * curr, min_prod * curr)
        max_prod = temp_max

        result = max(result, max_prod)

    return result

# Test
nums = [2, 3, -2, 4]
print(max_product_subarray(nums))  # Output: 6
