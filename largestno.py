def second_largest(arr):
    if len(arr) < 2:
        return None  # Not enough elements
    
    first = second = float('-inf')
    
    for num in arr:
        # If current number is greater than the largest
        if num > first:
            second = first
            first = num
        # If current number is between first and second
        elif num > second and num != first:
            second = num
    
    return second if second != float('-inf') else None

arr = [12, 35, 1, 10, 34, 1]
print("Second largest element is:", second_largest(arr))