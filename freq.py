def frequency(arr):
    freq = {}
    for item in arr:
        if item in freq:
            freq[item] += 1
        else:
            freq[item] = 1
    return freq

arr = [1, 2, 2, 3, 4, 4, 4, 5]
print("Frequency of elements:", frequency(arr))