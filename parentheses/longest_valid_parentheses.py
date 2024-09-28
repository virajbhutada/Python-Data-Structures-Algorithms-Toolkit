def longest_valid_parentheses(s):
    max_len = 0
    stack = [-1]
    
    for i, char in enumerate(s):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()
            if stack:
                max_len = max(max_len, i - stack[-1])
            else:
                stack.append(i)
    
    return max_len

# Test
s = "(()))())("
print(longest_valid_parentheses(s))  # Output: 4
