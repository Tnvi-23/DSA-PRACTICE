arr = [10, 25, 3, 99, 45, 67]

# Assume first element is max
maximum = arr[0]

# Traverse the array
for num in arr:
    if num > maximum:
        maximum = num

print("Maximum element is:", maximum)