def count_even_odd(arr):
    even_count, odd_count = 0, 0
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return even_count, odd_count

arr = [10, 25, 3, 99, 44, 67, 88, 12]
even, odd = count_even_odd(arr)
print("Even:", even, "Odd:", odd)