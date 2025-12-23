def merge_arrays(arr1, arr2):
    merged = []
    for i in arr1:
        merged.append(i)
    for j in arr2:
        merged.append(j)
    return merged

arr1 = [10, 20, 30]
arr2 = [40, 50, 60]

print("Merged array:", merge_arrays(arr1, arr2))