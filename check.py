def is_prime(n):
    # Step 1: Handle base cases
    if n <= 1:
        return False
    if n == 2:   # 2 is the smallest prime
        return True
    
    # Step 2: Check divisibility up to sqrt(n)
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    
    # Step 3: If no divisor found, it's prime
    return True

# Example usage
num = int(input("Enter the number:"))
if is_prime(num):
    print(num, "is a Prime Number")
else:
    print(num, "is NOT a Prime Number")