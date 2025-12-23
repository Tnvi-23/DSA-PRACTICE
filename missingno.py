def find_missing_number(arr, n):
    xor_all = 0
    xor_arr = 0
    
    # XOR from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i
    
    # XOR all elements in array
    for num in arr:
        xor_arr ^= num
    
    return xor_all ^ xor_arr

arr = [1, 2, 4, 5]
n = 5
print("Missing number is:", find_missing_number(arr, n))