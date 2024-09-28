def is_valid(self, s: str) -> bool:
    stack = []
    for c in s:  # loop through each character in the string
        if c in '([{':  # if the character is an opening bracket
            stack.append(c)  # push it onto the stack
        else:  # if the character is a closing bracket
            if not stack or \
                (c == ')' and stack[-1] != '(') or \
                (c == '}' and stack[-1] != '{') or \
                (c == ']' and stack[-1] != '['):
                    return False  # the string is not valid, so return false
                stack.pop()  # otherwise, pop the opening bracket from the stack
    return not stack