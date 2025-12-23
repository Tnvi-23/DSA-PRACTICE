def bubble_sort(arr):
    n = len(arr)
    # Traverse through all array elements
    for i in range(n):
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped in inner loop, break
        if not swapped:
            break
    return arr

arr = [64, 34, 25, 12, 22, 11, 90]
print("Sorted array:", bubble_sort(arr))