def fibonacci_iterative(n):
    fib = [0, 1]  # starting values
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[:n]

# Example usage
print(fibonacci_iterative(10))  # First 10 Fibonacci numbers