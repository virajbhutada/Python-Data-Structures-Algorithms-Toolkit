def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    fib = [0] * (n + 1)
    fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i - 1] + fib[i - 2]

    return fib[n]

# Test
print(fibonacci(10))  # Output: 55
